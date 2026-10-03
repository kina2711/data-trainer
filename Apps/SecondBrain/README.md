# Second Brain Apps

Private, local-first readers for the canonical Second Brain.

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
`npm run brain:index` after a canonical note changes. No source PDF, credential,
or `3_Toi` content is included in the app index.

## Validation

```bash
npm run brain:test
```
