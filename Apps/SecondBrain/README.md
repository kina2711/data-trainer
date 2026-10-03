# Rabbit Data Learning Portal

A static Web/Desktop portal for three governed surfaces:

- 56 DA/DE roadmaps;
- 645 canonical Second Brain notes;
- lecture packages whose `lesson.yaml` status is `ready-for-owner-review`.

Draft lessons, raw reference files and `3_Toi` content are not indexed.

## Interface direction

The portal uses an operational-workspace layout: compact left rail, searchable
content sidebar, tabbed reading canvas, contextual inspector and a status bar.
The visual direction adapts the Dashboard/Cockpit guidance from
[Prompt-Driven UI](https://github.com/vuhung16au/prompt-driven-ui) to the supplied
Rabbit Data wireframe while retaining the existing static app and governed data.

## Build the shared index

```bash
npm run brain:index
```

## Web app

```bash
npm run brain:web
```

Open `http://127.0.0.1:4310`.

## Desktop app

```bash
npm run brain:desktop
```

Both applications read the same generated `web/data/brain-index.json`. Re-run
`npm run brain:index` after a roadmap, canonical note or publishable lesson changes.
No source PDF, credential, absolute local path or `3_Toi` content is included.

## Vercel

Import the repository with these settings:

```text
Root Directory: Apps/SecondBrain/web
Framework Preset: Other
Build Command: empty
Output Directory: empty (defaults to project root)
Install Command: empty
```

## Validation

```bash
npm run brain:test
```
