"""
Metamist wrapper to get input samples.
"""

import logging

from cpg_utils.config import get_config

from .metamist import get_metamist, Sequence, AnalysisType, MetamistError
from .targets import Cohort, Sex, PedigreeInfo


_cohort: Cohort | None = None


def get_cohort() -> Cohort:
    """Return the cohort object"""
    global _cohort
    if not _cohort:
        _cohort = create_cohort()
    return _cohort


def create_cohort() -> Cohort:
    """
    Add datasets in the cohort. There exists only one cohort for the workflow run.
    """
    analysis_dataset_name = get_config()['workflow']['dataset']
    dataset_names = get_config()['workflow'].get(
        'input_datasets', [analysis_dataset_name]
    )
    skip_datasets = get_config()['workflow'].get('skip_datasets', [])
    dataset_names = [d for d in dataset_names if d not in skip_datasets]

    cohort = Cohort()
    for dataset_name in dataset_names:
        dataset = cohort.create_dataset(dataset_name)
        logging.info(f'Getting samples for dataset {dataset_name}')
        sample_entries = get_metamist().get_sample_entries(dataset_name)
        for entry in sample_entries:
            dataset.add_sample(
                id=str(entry['id']),
                external_id=str(entry['external_id']),
                meta=entry.get('meta', {}),
            )

    if not cohort.get_datasets():
        msg = 'No datasets populated'
        if 'skip_samples' in get_config()['workflow']:
            msg += ' (after skipping samples)'
        if 'only_samples' in get_config()['workflow']:
            msg += ' (after picking samples)'
        logging.warning(msg)
        return cohort

    if sequencing_type := get_config()['workflow'].get('sequencing_type'):
        _populate_alignment_inputs(cohort, sequencing_type)
        _filter_sequencing_type(cohort, sequencing_type)
    _populate_analysis(cohort)
    _populate_participants(cohort)
    _populate_pedigree(cohort)
    return cohort


def _filter_sequencing_type(cohort: Cohort, sequencing_type: str):
    """
    Filtering to the samples with only requested sequencing types.
    """
    for s in cohort.get_samples():
        if not s.seq_by_type:
            logging.warning(f'{s}: skipping because no sequencing inputs found')
            s.active = False
            continue

        if s.alignment_input_by_seq_type:
            avail_types = list(s.seq_by_type.keys())
            s.alignment_input_by_seq_type = {
                k: v
                for k, v in s.alignment_input_by_seq_type.items()
                if k == sequencing_type
            }
            if not bool(s.alignment_input_by_seq_type):
                logging.warning(
                    f'{s}: skipping because no inputs with data type '
                    f'"{sequencing_type}" found in {avail_types}'
                )
                s.active = False


def _populate_alignment_inputs(
    cohort: Cohort,
    sequencing_type: str,
    check_existence: bool = False,
) -> None:
    """
    Populate sequencing inputs for samples.
    """
    assert cohort.get_sample_ids()

    seq_entries_by_sid = get_metamist().get_sequence_entries_by_sid(
        cohort.get_sample_ids(), sequencing_type=sequencing_type
    )

    # Log sequences without samples, this is a pretty common thing,
    # but useful to log to easier track down samples not processed
    if sids_wo_seq := [
        sid for sid in cohort.get_sample_ids() if sid not in seq_entries_by_sid
    ]:
        msg = f'No {sequencing_type} sequencing data found for samples:\n'
        for ds in cohort.get_datasets():
            ds_sids_wo_seq = [sid for sid in sids_wo_seq if sid in ds.get_sample_ids()]
            msg += (
                f'\t{ds.name}, {len(ds_sids_wo_seq)}/{len(ds.get_samples())} samples: '
                f'{", ".join(ds_sids_wo_seq)}\n'
            )
        logging.info(msg)

    sid_wo_reads = set()
    for sample in cohort.get_samples():
        for entry in seq_entries_by_sid.get(sample.id, []):
            if not entry['meta'].get('reads'):
                sid_wo_reads.add(sample.id)
                continue
            seq = Sequence.parse(entry, check_existence=check_existence)
            sample.seq_by_type[seq.sequencing_type] = seq
            if seq.alignment_input:
                if seq.sequencing_type in sample.alignment_input_by_seq_type:
                    raise MetamistError(
                        f'{sample}: found more than 1 alignment input with '
                        f'sequencing type: {seq.sequencing_type}. Check your '
                        f'input provider to make sure there is only one data source '
                        f'of sequencing type per sample.'
                    )
                sample.alignment_input_by_seq_type[
                    seq.sequencing_type
                ] = seq.alignment_input
    if sid_wo_reads:
        logging.warning(
            f'Found {len(sid_wo_reads)}/{len(cohort.get_samples())} samples with '
            f'no meta/rads in corresponding sequence entries'
        )


def _populate_analysis(cohort: Cohort) -> None:
    """
    Populate Analysis entries.
    """
    for dataset in cohort.get_datasets():
        gvcf_by_sid = get_metamist().get_analyses_by_sid(
            dataset.get_sample_ids(),
            analysis_type=AnalysisType.GVCF,
            dataset=dataset.name,
        )
        cram_by_sid = get_metamist().get_analyses_by_sid(
            dataset.get_sample_ids(),
            analysis_type=AnalysisType.CRAM,
            dataset=dataset.name,
        )
        for sample in dataset.get_samples():
            if (analysis := gvcf_by_sid.get(sample.id)) and analysis.output:
                assert analysis.output == sample.make_gvcf_path().path, (
                    analysis.output,
                    sample.make_gvcf_path().path,
                )
                sample.gvcf = sample.make_gvcf_path()
            if (analysis := cram_by_sid.get(sample.id)) and analysis.output:
                assert analysis.output == sample.make_cram_path().path, analysis.output
                sample.cram = sample.make_cram_path()


def _populate_participants(cohort: Cohort) -> None:
    """
    Populate Participant entries.
    """
    for dataset in cohort.get_datasets():
        logging.info(f'Reading participants IDs for dataset {dataset}')

        participant_by_sid = get_metamist().get_participant_entries_by_sid(dataset.name)

        for sample in dataset.get_samples():
            if pid := participant_by_sid.get(sample.id):
                sample.participant_id = pid


def _populate_pedigree(cohort: Cohort) -> None:
    """
    Populate pedigree data for samples.
    """
    sample_by_participant_id = dict()
    for s in cohort.get_samples():
        sample_by_participant_id[s.participant_id] = s

    for dataset in cohort.get_datasets():
        logging.info(f'Reading pedigree for dataset {dataset}')
        ped_entries = get_metamist().get_ped_entries(dataset=dataset.name)
        ped_entry_by_participant_id = {}
        for ped_entry in ped_entries:
            part_id = str(ped_entry['individual_id'])
            ped_entry_by_participant_id[part_id] = ped_entry

        sids_wo_ped = []
        for sample in dataset.get_samples():
            if sample.participant_id not in ped_entry_by_participant_id:
                sids_wo_ped.append(sample.id)
                continue

            ped_entry = ped_entry_by_participant_id[sample.participant_id]
            maternal_sample = sample_by_participant_id.get(
                str(ped_entry['maternal_id'])
            )
            paternal_sample = sample_by_participant_id.get(
                str(ped_entry['paternal_id'])
            )
            sample.pedigree = PedigreeInfo(
                sample=sample,
                fam_id=ped_entry['family_id'],
                mom=maternal_sample,
                dad=paternal_sample,
                sex=Sex.parse(str(ped_entry['sex'])),
                phenotype=ped_entry['affected'] or '0',
            )
        if sids_wo_ped:
            logging.warning(
                f'No pedigree data found for '
                f'{len(sids_wo_ped)}/{len(dataset.get_samples())} samples'
            )

    for dataset in cohort.get_datasets():
        samples_with_ped = [s for s in dataset.get_samples() if s.pedigree]
        logging.info(
            f'{dataset.name}: found pedigree info for {len(samples_with_ped)} '
            f'samples out of {len(dataset.get_samples())}'
        )
