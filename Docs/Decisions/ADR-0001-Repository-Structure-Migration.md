# Repository structure migration contract

Date: 2026-09-25  
Owner approval: kina2711  
Risk: destructive repository reorganisation; all retained content must remain recoverable.

## Objective

Replace the legacy `material/` and `Web/` layout with the approved repository structure:

- `Material/DA|DE/Curriculum/Phase/Module/Lesson`
- mirrored `Roadmap` and `Reference` hierarchies;
- `Artifact/` as the review gate before rebuilding `Web/`;
- `Docs/` for standards, architecture and decisions;
- `Tools/` for curriculum generators, specifications, maps and manifests.

## In scope

- Move all 525 existing lesson scaffolds without rewriting their content.
- Move the 42 roadmap Markdown files and 42 roadmap Draw.io files without changing their wording.
- Preserve and move every file currently under a `ref/` directory.
- Preserve shared datasets.
- Split `.data-2026/` into explicit `Tools/Curriculum/` areas.
- Remove the complete legacy `Web/` tree.
- Consolidate the approved note-format proposal into `Docs/Standards/`.

## Out of scope

- Rewriting roadmap wording or learning objectives.
- Converting lesson bodies to the V4 note format.
- Combining `quiz.md` and `homework.md` into `after-note.md`.
- Creating the Rabbit Data interface or rebuilding the web application.
- Deploying any artifact.

## Protected data

- All files below any legacy `ref/` path.
- All program and module roadmap `.md` and `.drawio` files.
- All 525 lesson directories and their current files.
- Git history and source datasets.

## Acceptance criteria

- Exactly 525 lesson directories exist after migration: 85 DA and 440 DE.
- Every migrated lesson has the same relative file set and byte content as before migration.
- Exactly 42 roadmap Markdown files and 42 roadmap Draw.io files remain present.
- The set, sizes and byte hashes of all protected reference files remain unchanged.
- DE modules map to the ten phases declared in the approved module map.
- DA modules map to four structural phases aligned with its four existing programme milestones.
- The legacy lowercase `material/`, `.data-2026/` and complete legacy `Web/` trees no longer exist.
- No web application is generated before the `Artifact/` review gate.

## Recovery

Tracked files can be restored from Git. Untracked reference files are moved by same-filesystem
rename, never copied and deleted. A before/after manifest records path, size and SHA-256 for every
protected reference file and every lesson file.

## Result

- Migrated 85 DA lessons and 440 DE lessons.
- Preserved 3,150 legacy lesson files, 2,037 reference files and 84 roadmap artifacts byte-for-byte.
- Added one `lesson.yaml` and one `after-note.md` scaffold per lesson.
- Added thin `roadmap.yaml` and `sources.yaml` manifests at lesson level; no roadmap or source text
  was duplicated.
- Removed the complete legacy `Web/` tree from the workspace. Its recoverable migration backup is
  outside the repository and is not part of the new architecture.

## Residual risk

The DA approval ledger contained a stale SHA-256 before this migration. The approved value is
`64391070c20b3ae21c5c6c5124ccd216a1987121d376b9b0f565f4f19ba14801`; the roadmap present before
and after the move hashes to `8bcb29c0f509e1cf3fcd67c7a6fcace8bb06804bd787eb91a1bf11f4969379b0`.
The ledger hash was not replaced because doing so would falsely record a new approval. The owner
must approve the current roadmap version or restore the approved artifact in the roadmap review step.
