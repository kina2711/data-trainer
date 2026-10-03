import { marked } from "./vendor/marked.esm.js";
import DOMPurify from "./vendor/purify.es.mjs";
import mermaid from "./vendor/mermaid/mermaid.esm.min.mjs";

const state = {
  data: null,
  notesById: new Map(),
  filtered: [],
  activeId: null,
  query: "",
  domain: "",
  mode: "all",
  favorites: new Set(JSON.parse(localStorage.getItem("second-brain:favorites") || "[]")),
  recent: JSON.parse(localStorage.getItem("second-brain:recent") || "[]"),
};

const $ = (selector) => document.querySelector(selector);
const elements = {
  app: $("#app"), search: $("#search-input"), domain: $("#domain-select"), list: $("#note-list"),
  count: $("#result-count"), empty: $("#empty-state"), reader: $("#reader"), title: $("#note-title"),
  question: $("#note-question"), noteDomain: $("#note-domain"), meta: $("#note-meta"), body: $("#note-body"),
  favorite: $("#favorite-button"), context: $("#context-panel"), outline: $("#outline"),
  relationships: $("#relationships"), sources: $("#sources"), stats: $("#brain-stats"),
  release: $("#release-label"), sidebar: $("#sidebar"), toast: $("#toast"),
};

const normalize = (value = "") => value.toString().normalize("NFD").replace(/[\u0300-\u036f]/g, "").toLowerCase();
const escapeHtml = (value = "") => value.replace(/[&<>'"]/g, (char) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", "'": "&#39;", '"': "&quot;" }[char]));
const searchable = (note) => normalize([note.title, note.question, note.domain, note.tags.join(" "), note.aliases.join(" "), note.body].join(" "));

async function loadData() {
  if (window.secondBrainAPI?.loadIndex) return window.secondBrainAPI.loadIndex();
  const response = await fetch("./data/brain-index.json", { cache: "no-store" });
  if (!response.ok) throw new Error(`Không thể nạp chỉ mục (${response.status})`);
  return response.json();
}

function configureMarkdown() {
  const renderer = new marked.Renderer();
  renderer.code = (codeOrToken, language) => {
    const text = typeof codeOrToken === "object" ? codeOrToken.text : codeOrToken;
    const lang = typeof codeOrToken === "object" ? codeOrToken.lang : language;
    if (lang === "mermaid") return `<div class="mermaid">${escapeHtml(text)}</div>`;
    return `<pre><code class="language-${escapeHtml(lang || "text")}">${escapeHtml(text)}</code></pre>`;
  };
  marked.use({ renderer, gfm: true, breaks: false });
  mermaid.initialize({ startOnLoad: false, securityLevel: "strict", theme: "neutral", fontFamily: "Inter, system-ui, sans-serif" });
}

function preprocessMarkdown(markdown) {
  return markdown.replace(/\[\[([^\]|]+)(?:\|([^\]]+))?\]\]/g, (_, target, label) => {
    const text = label || target;
    return `<a href="#" class="wikilink" data-wiki="${escapeHtml(target.trim())}">${escapeHtml(text.trim())}</a>`;
  });
}

function renderStats() {
  const stats = state.data.stats;
  elements.stats.innerHTML = [
    [stats.notes, "note canonical"], [stats.domains, "domain"], [stats.sources, "nguồn"], [stats.retrievalCases, "retrieval case"],
  ].map(([value, label]) => `<div class="stat"><strong>${value.toLocaleString("vi-VN")}</strong><span>${label}</span></div>`).join("");
}

function populateDomains() {
  elements.domain.insertAdjacentHTML("beforeend", state.data.domains.map((item) => `<option value="${escapeHtml(item.name)}">${escapeHtml(item.name)} · ${item.count}</option>`).join(""));
}

function applyFilters() {
  const terms = normalize(state.query).split(/\s+/).filter(Boolean);
  let notes = state.data.notes;
  if (state.domain) notes = notes.filter((note) => note.domain === state.domain);
  if (state.mode === "favorites") notes = notes.filter((note) => state.favorites.has(note.id));
  if (state.mode === "recent") {
    const order = new Map(state.recent.map((id, index) => [id, index]));
    notes = notes.filter((note) => order.has(note.id)).sort((a, b) => order.get(a.id) - order.get(b.id));
  }
  if (terms.length) {
    notes = notes.map((note) => {
      const haystack = note._search;
      const score = terms.reduce((sum, term) => sum + (normalize(note.title).includes(term) ? 8 : 0) + (normalize(note.question).includes(term) ? 5 : 0) + (haystack.includes(term) ? 1 : -100), 0);
      return { note, score };
    }).filter((item) => item.score > -50).sort((a, b) => b.score - a.score || a.note.title.localeCompare(b.note.title, "vi")).map((item) => item.note);
  }
  state.filtered = notes;
  renderList();
}

function renderList() {
  elements.count.textContent = `${state.filtered.length.toLocaleString("vi-VN")} note`;
  if (!state.filtered.length) {
    elements.list.innerHTML = `<div class="list-empty">Không tìm thấy note phù hợp.<br>Thử bỏ bớt từ khóa hoặc bộ lọc.</div>`;
    return;
  }
  elements.list.innerHTML = state.filtered.slice(0, 240).map((note) => `<button class="note-card ${note.id === state.activeId ? "active" : ""}" data-note-id="${escapeHtml(note.id)}" role="option" aria-selected="${note.id === state.activeId}"><strong>${escapeHtml(note.title)}</strong><span><span class="domain">${escapeHtml(note.domain)}</span><span>${note.wordCount.toLocaleString("vi-VN")} từ</span></span></button>`).join("");
}

function pushRecent(noteId) {
  state.recent = [noteId, ...state.recent.filter((id) => id !== noteId)].slice(0, 40);
  localStorage.setItem("second-brain:recent", JSON.stringify(state.recent));
}

function relationButton(noteId) {
  const note = state.notesById.get(noteId);
  return note ? `<button class="relation-button" data-note-id="${escapeHtml(note.id)}">${escapeHtml(note.title)}</button>` : "";
}

function renderContext(note) {
  elements.sources.innerHTML = note.sourceIds.map((id) => `<p class="source-id">${escapeHtml(id)}</p>`).join("") || `<p class="source-id">Không có source ID</p>`;
  const groups = [["Xây trên", note.relationships.buildsOn], ["Mở đường cho", note.relationships.prerequisiteOf], ["Liên quan", note.relationships.relatedTo]];
  elements.relationships.innerHTML = groups.filter(([, ids]) => ids.length).map(([label, ids]) => `<div class="relation-group"><strong>${label}</strong>${ids.map(relationButton).join("")}</div>`).join("") || `<p class="source-id">Không có liên kết trực tiếp</p>`;
  const headings = [...elements.body.querySelectorAll("h2, h3")];
  elements.outline.innerHTML = headings.slice(0, 30).map((heading, index) => {
    heading.id = `section-${index}`;
    return `<a href="#section-${index}" class="outline-${heading.tagName.toLowerCase()}">${escapeHtml(heading.textContent)}</a>`;
  }).join("");
}

async function openNote(noteId, updateHash = true) {
  const note = state.notesById.get(noteId);
  if (!note) return;
  state.activeId = note.id;
  pushRecent(note.id);
  elements.empty.hidden = true;
  elements.reader.hidden = false;
  elements.context.hidden = false;
  elements.title.textContent = note.title;
  elements.question.textContent = note.question;
  elements.noteDomain.textContent = note.domain;
  elements.favorite.textContent = state.favorites.has(note.id) ? "★" : "☆";
  elements.favorite.setAttribute("aria-label", state.favorites.has(note.id) ? "Bỏ lưu note" : "Lưu note");
  elements.meta.innerHTML = [note.noteType, `${note.wordCount.toLocaleString("vi-VN")} từ`, `Duyệt ${note.approvedAt}`, ...note.tags.slice(0, 6)].filter(Boolean).map((value) => `<span class="pill">${escapeHtml(value)}</span>`).join("");
  const html = DOMPurify.sanitize(marked.parse(preprocessMarkdown(note.body)), { ADD_ATTR: ["data-wiki", "class"], ADD_TAGS: ["details", "summary"] });
  elements.body.innerHTML = html;
  renderContext(note);
  try { await mermaid.run({ nodes: elements.body.querySelectorAll(".mermaid") }); } catch (error) { showToast("Một sơ đồ không render được; nội dung gốc vẫn được giữ."); console.error(error); }
  renderList();
  elements.sidebar.classList.remove("open");
  if (updateHash) history.replaceState(null, "", `#note=${encodeURIComponent(note.id)}`);
  document.title = `${note.title} · Second Brain`;
  window.scrollTo({ top: 0, behavior: "instant" });
}

function findWikiTarget(label) {
  const needle = normalize(label);
  return state.data.notes.find((note) => note.id === label || normalize(note.title) === needle || note.aliases.some((alias) => normalize(alias) === needle));
}

function showToast(message) {
  elements.toast.textContent = message;
  elements.toast.classList.add("show");
  clearTimeout(showToast.timer);
  showToast.timer = setTimeout(() => elements.toast.classList.remove("show"), 2200);
}

function toggleFavorite() {
  if (!state.activeId) return;
  if (state.favorites.has(state.activeId)) state.favorites.delete(state.activeId); else state.favorites.add(state.activeId);
  localStorage.setItem("second-brain:favorites", JSON.stringify([...state.favorites]));
  elements.favorite.textContent = state.favorites.has(state.activeId) ? "★" : "☆";
  showToast(state.favorites.has(state.activeId) ? "Đã lưu note" : "Đã bỏ lưu");
  if (state.mode === "favorites") applyFilters();
}

function bindEvents() {
  let timer;
  elements.search.addEventListener("input", () => { clearTimeout(timer); timer = setTimeout(() => { state.query = elements.search.value; applyFilters(); }, 120); });
  elements.domain.addEventListener("change", () => { state.domain = elements.domain.value; applyFilters(); });
  elements.list.addEventListener("click", (event) => { const button = event.target.closest("[data-note-id]"); if (button) openNote(button.dataset.noteId); });
  elements.relationships.addEventListener("click", (event) => { const button = event.target.closest("[data-note-id]"); if (button) openNote(button.dataset.noteId); });
  elements.body.addEventListener("click", (event) => { const link = event.target.closest("[data-wiki]"); if (!link) return; event.preventDefault(); const note = findWikiTarget(link.dataset.wiki); if (note) openNote(note.id); else { elements.search.value = link.dataset.wiki; state.query = link.dataset.wiki; applyFilters(); showToast("Không có note đích chính xác; đã chuyển thành tìm kiếm."); } });
  elements.favorite.addEventListener("click", toggleFavorite);
  $("#clear-filters").addEventListener("click", () => { state.query = ""; state.domain = ""; state.mode = "all"; elements.search.value = ""; elements.domain.value = ""; document.querySelectorAll(".tab").forEach((tab) => tab.classList.toggle("active", tab.dataset.mode === "all")); applyFilters(); });
  document.querySelectorAll(".tab").forEach((tab) => tab.addEventListener("click", () => { state.mode = tab.dataset.mode; document.querySelectorAll(".tab").forEach((item) => item.classList.toggle("active", item === tab)); applyFilters(); }));
  $("#nav-toggle").addEventListener("click", () => elements.sidebar.classList.toggle("open"));
  $("#theme-toggle").addEventListener("click", () => { const next = document.documentElement.dataset.theme === "light" ? "dark" : "light"; document.documentElement.dataset.theme = next; localStorage.setItem("second-brain:theme", next); });
  document.addEventListener("keydown", (event) => { if ((event.ctrlKey || event.metaKey) && event.key.toLowerCase() === "k" || event.key === "/" && !/input|textarea/i.test(document.activeElement.tagName)) { event.preventDefault(); elements.search.focus(); elements.search.select(); } if (event.key === "Escape") { elements.search.blur(); elements.sidebar.classList.remove("open"); } });
}

async function initialize() {
  configureMarkdown();
  document.documentElement.dataset.theme = localStorage.getItem("second-brain:theme") || "dark";
  state.data = await loadData();
  state.data.notes.forEach((note) => { note._search = searchable(note); state.notesById.set(note.id, note); });
  elements.release.textContent = `v${state.data.brainVersion} · private`;
  populateDomains(); renderStats(); bindEvents(); applyFilters();
  const noteId = new URLSearchParams(location.hash.slice(1)).get("note");
  if (noteId && state.notesById.has(noteId)) await openNote(noteId, false);
  elements.app.setAttribute("aria-busy", "false");
}

initialize().catch((error) => {
  console.error(error);
  elements.empty.innerHTML = `<h1>Không thể mở Second Brain</h1><p>${escapeHtml(error.message)}</p><p>Hãy chạy lại <code>npm run brain:index</code>.</p>`;
  elements.app.setAttribute("aria-busy", "false");
});
