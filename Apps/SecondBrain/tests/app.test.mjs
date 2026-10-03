import assert from "node:assert/strict";
import fs from "node:fs";
import path from "node:path";
import test from "node:test";
import { fileURLToPath } from "node:url";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const web = path.join(root, "web");
const data = JSON.parse(fs.readFileSync(path.join(web, "data", "brain-index.json"), "utf8"));

test("canonical index contains the complete private release", () => {
  assert.equal(data.brainVersion, "2.0.0");
  assert.equal(data.release.visibility, "private-local-first");
  assert.equal(data.notes.length, 645);
  assert.equal(new Set(data.notes.map((note) => note.id)).size, 645);
  assert.ok(data.domains.length >= 20);
});

test("every indexed note is readable, canonical and linked", () => {
  const ids = new Set(data.notes.map((note) => note.id));
  for (const note of data.notes) {
    assert.equal(note.status, "canonical");
    assert.ok(note.title.length > 3);
    assert.ok(note.question.length > 8);
    assert.ok(note.body.length > 1000);
    assert.ok(note.sourceIds.length > 0);
    assert.match(note.body, /```mermaid/);
    assert.doesNotMatch(note.body, /Concept key.*`proposed`/);
    assert.doesNotMatch(note.body, /note (?:không|chưa) (?:được )?tính (?:là )?canonical/);
    for (const relation of [...note.relationships.buildsOn, ...note.relationships.prerequisiteOf, ...note.relationships.relatedTo]) assert.ok(ids.has(relation), `${note.id} -> ${relation}`);
  }
});

test("web and desktop entrypoints exist with security controls", () => {
  for (const file of ["index.html", "styles.css", "app.js", "favicon.svg"]) assert.ok(fs.existsSync(path.join(web, file)), file);
  const main = fs.readFileSync(path.join(root, "desktop", "main.cjs"), "utf8");
  const html = fs.readFileSync(path.join(web, "index.html"), "utf8");
  const client = fs.readFileSync(path.join(web, "app.js"), "utf8");
  assert.match(html, /Content-Security-Policy/);
  assert.match(client, /typeof codeOrToken === "object"/);
  assert.match(main, /contextIsolation:\s*true/);
  assert.match(main, /nodeIntegration:\s*false/);
  assert.match(main, /sandbox:\s*true/);
  assert.match(main, /setWindowOpenHandler/);
  assert.match(main, /SECOND_BRAIN_SMOKE/);
  assert.match(main, /url !== appUrl/);
});
