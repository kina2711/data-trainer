import assert from "node:assert/strict";
import fs from "node:fs";
import path from "node:path";
import test from "node:test";
import { fileURLToPath } from "node:url";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const web = path.join(root, "web");
const rawIndex = fs.readFileSync(path.join(web, "data", "brain-index.json"), "utf8");
const data = JSON.parse(rawIndex);

test("portal index contains the complete governed release", () => {
  assert.equal(data.schemaVersion, 2);
  assert.equal(data.portalVersion, "1.0.0");
  assert.equal(data.brainVersion, "2.0.0");
  assert.equal(data.release.visibility, "private-local-first");
  assert.equal(data.notes.length, 645);
  assert.equal(data.roadmaps.length, 56);
  assert.equal(data.lessons.length, 10);
  assert.equal(rawIndex.includes("/home/"), false, "published index must not contain Linux home paths");
  assert.equal(rawIndex.includes("\\\\Users\\\\"), false, "published index must not contain Windows user paths");
  assert.equal(new Set(data.notes.map((note) => note.id)).size, 645);
  assert.equal(new Set(data.roadmaps.map((item) => item.id)).size, 56);
  assert.equal(new Set(data.lessons.map((item) => item.id)).size, 10);
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

test("roadmap hierarchy is complete and navigable", () => {
  const ids = new Set(data.roadmaps.map((item) => item.id));
  assert.deepEqual(
    Object.fromEntries(["DA", "DE"].map((program) => [program, data.roadmaps.filter((item) => item.program === program).length])),
    { DA: 16, DE: 40 },
  );
  for (const item of data.roadmaps) {
    assert.ok(item.title.length > 5);
    assert.ok(item.body.length > 500);
    if (item.parentId) assert.ok(ids.has(item.parentId), `${item.id} parent ${item.parentId}`);
    for (const childId of item.childIds) assert.ok(ids.has(childId), `${item.id} child ${childId}`);
  }
});

test("only complete owner-review lessons are published", () => {
  for (const lesson of data.lessons) {
    assert.equal(lesson.status, "ready-for-owner-review");
    assert.equal(lesson.assets.length, 5);
    assert.deepEqual(lesson.assets.map((asset) => asset.key), ["note", "slides", "quiz", "homework", "afterNote"]);
    assert.ok(lesson.centralQuestion.length > 10);
    assert.equal(lesson.sceneCount, 9);
    for (const asset of lesson.assets) assert.ok(asset.body.length > 500, `${lesson.id}/${asset.key}`);
  }
});

test("web and desktop entrypoints exist with security controls", () => {
  for (const file of ["index.html", "styles.css", "app.js", "favicon.svg"]) assert.ok(fs.existsSync(path.join(web, file)), file);
  const main = fs.readFileSync(path.join(root, "desktop", "main.cjs"), "utf8");
  const html = fs.readFileSync(path.join(web, "index.html"), "utf8");
  const client = fs.readFileSync(path.join(web, "app.js"), "utf8");
  assert.match(html, /Content-Security-Policy/);
  assert.match(html, /data-space="roadmap"/);
  assert.match(html, /data-space="brain"/);
  assert.match(html, /data-space="lessons"/);
  assert.match(html, /class="left-rail"/);
  assert.match(html, /class="bottom-bar"/);
  assert.match(html, /INSPECTOR/);
  assert.match(client, /typeof codeOrToken === "object"/);
  assert.match(client, /ready-for-owner-review/);
  assert.match(main, /contextIsolation:\s*true/);
  assert.match(main, /nodeIntegration:\s*false/);
  assert.match(main, /sandbox:\s*true/);
  assert.match(main, /setWindowOpenHandler/);
  assert.match(main, /SECOND_BRAIN_SMOKE/);
  assert.match(main, /url !== appUrl/);
});
