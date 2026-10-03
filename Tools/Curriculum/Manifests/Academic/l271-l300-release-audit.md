# L271-L300 release audit

- Status: completed; awaiting owner semantic review
- Execution order: L271-L275, L276-L280, L281-L285, L286-L290, L291-L295, L296-L300
- Risk tier: R2-standard
- Curriculum artifacts: 30 `note.md` and 30 `after-note.md`
- Knowledge artifacts: 30 Reference notes and 30 matching Wiki notes
- Source records added: 9 official-documentation records
- Manifest: version 1.0.59; 155 sources; 223 notes; 716 retrieval cases
- Deliverable fingerprint: `1e6be288dc07d98e22239be0c3821db66246457c9461e4477a1a8ddf000c3c3d`

## Verification

- Deterministic generation: six batches, `stale=0`
- Batch validators: 6/6 passed; five lessons per batch
- Humanizer: 30/30 marked `humanized-v3`
- Long-paragraph duplication: 0 within notes; 0 across notes
- Canned prose tells: 0
- Knowledge-note formatter: 603 checked; 0 failed
- Knowledge-note source coverage: 223 checked; 0 failed
- Reference/Wiki parity: 30/30
- Word-count range: 3,645-4,155 words per knowledge note
- Obsidian synchronization: non-deleting sync completed; checksum comparison returned no differences

## Approval boundary

The exact artifact set is eligible for curriculum-owner review. It is not production execution evidence: live Airflow, warehouse, Great Expectations, DataHub and OpenLineage labs were not run, and version/configuration-dependent behavior must be checked in the target environment.
