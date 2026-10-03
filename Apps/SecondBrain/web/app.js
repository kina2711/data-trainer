import { marked } from "./vendor/marked.esm.js";
import DOMPurify from "./vendor/purify.es.mjs";
import mermaid from "./vendor/mermaid/mermaid.esm.min.mjs";

const state = {
  data: null,
  space: "roadmap",
  query: "",
  program: "",
  filter: "",
  listMode: "all",
  activeId: null,
  activeAsset: "note",
  roadmapsById: new Map(),
  roadmapsByPath: new Map(),
  notesById: new Map(),
  lessonsById: new Map(),
  favorites: new Set(JSON.parse(localStorage.getItem("rabbit-data:favorites") || "[]")),
  recent: JSON.parse(localStorage.getItem("rabbit-data:recent") || "[]"),
};

const $ = (selector) => document.querySelector(selector);
const elements = {
  app: $("#app"), sidebar: $("#sidebar"), search: $("#search-input"), list: $("#content-list"),
  count: $("#result-count"), filter: $("#content-filter"), filterLabel: $("#filter-label"),
  programSwitch: $("#program-switch"), brainModes: $("#brain-modes"), sidebarKicker: $("#sidebar-kicker"),
  sidebarTitle: $("#sidebar-title"), empty: $("#empty-state"), reader: $("#reader"),
  homeKicker: $("#home-kicker"), homeTitle: $("#home-title"), homeDescription: $("#home-description"),
  stats: $("#portal-stats"), title: $("#content-title"), question: $("#content-question"),
  domain: $("#content-domain"), status: $("#content-status"), meta: $("#content-meta"),
  body: $("#content-body"), favorite: $("#favorite-button"), assetTabs: $("#asset-tabs"),
  context: $("#context-panel"), outline: $("#outline"), connections: $("#connections"),
  connectionsTitle: $("#connections-title"), sources: $("#sources"), release: $("#release-label"),
  toast: $("#toast"),
};

const normalize = (value = "") => value.toString().normalize("NFD").replace(/[\u0300-\u036f]/g, "").toLowerCase();
const escapeHtml = (value = "") => value.toString().replace(/[&<>'"]/g, (char) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", "'": "&#39;", '"': "&quot;" }[char]));
const pills = (values) => values.filter(Boolean).map((value) => `<span class="pill">${escapeHtml(value)}</span>`).join("");

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

function preprocessWiki(markdown) {
  return markdown.replace(/\[\[([^\]|]+)(?:\|([^\]]+))?\]\]/g, (_, target, label) => {
    const text = label || target;
    return `<a href="#" class="wikilink" data-wiki="${escapeHtml(target.trim())}">${escapeHtml(text.trim())}</a>`;
  });
}

function searchable(values) {
  return normalize(values.filter(Boolean).join(" "));
}

function prepareData() {
  for (const note of state.data.notes) {
    note._search = searchable([note.title, note.question, note.domain, note.tags.join(" "), note.aliases.join(" "), note.body]);
    state.notesById.set(note.id, note);
  }
  for (const roadmap of state.data.roadmaps) {
    roadmap._search = searchable([roadmap.title, roadmap.programName, roadmap.level, roadmap.body]);
    state.roadmapsById.set(roadmap.id, roadmap);
    state.roadmapsByPath.set(roadmap.path, roadmap);
  }
  for (const lesson of state.data.lessons) {
    lesson._search = searchable([lesson.id, lesson.title, lesson.programName, lesson.centralQuestion, lesson.objective, ...lesson.assets.map((asset) => asset.body)]);
    state.lessonsById.set(lesson.id, lesson);
  }
}

function statCards(items) {
  elements.stats.innerHTML = items.map(([value, label]) => `<div class="stat"><strong>${Number(value).toLocaleString("vi-VN")}</strong><span>${escapeHtml(label)}</span></div>`).join("");
}

function renderHome() {
  elements.reader.hidden = true;
  elements.context.hidden = false;
  elements.empty.hidden = false;
  if (state.space === "roadmap") {
    elements.homeKicker.textContent = "RABBIT DATA LEARNING OS";
    elements.homeTitle.textContent = "Bắt đầu từ lộ trình";
    elements.homeDescription.textContent = "Đi từ đầu ra chương trình tới từng giai đoạn và mô-đun, rồi mở bài giảng đã đủ điều kiện xuất bản.";
    statCards([[state.data.stats.programs, "chương trình"], [state.data.stats.roadmaps, "roadmap"], [state.data.roadmaps.filter((item) => item.level === "module").length, "mô-đun"]]);
  } else if (state.space === "brain") {
    elements.homeKicker.textContent = "CANONICAL KNOWLEDGE";
    elements.homeTitle.textContent = "Second Brain đã kiểm duyệt";
    elements.homeDescription.textContent = "Tìm concept, câu hỏi và mối quan hệ trong lớp Wiki canonical; nguồn thô và dữ liệu cá nhân không được xuất bản.";
    statCards([[state.data.stats.notes, "note canonical"], [state.data.stats.domains, "domain"], [state.data.stats.sources, "nguồn"]]);
  } else {
    elements.homeKicker.textContent = "READY-FOR-OWNER-REVIEW";
    elements.homeTitle.textContent = "Bài giảng đã xây xong";
    elements.homeDescription.textContent = "Mỗi bài có giáo trình, slide, quiz, bài tập và hướng dẫn sau buổi học. Bài nháp không xuất hiện ở đây.";
    statCards([[state.data.stats.lessons, "bài giảng"], [state.data.lessons.reduce((sum, item) => sum + item.sceneCount, 0), "learning scene"], [state.data.lessons.reduce((sum, item) => sum + item.durationMinutes, 0), "phút dự kiến"]]);
  }
  elements.outline.innerHTML = `<p class="source-id">Chọn một mục trong sidebar để mở nội dung đầy đủ và mục lục theo ngữ cảnh.</p>`;
  elements.connectionsTitle.textContent = "Phạm vi xuất bản";
  elements.connections.innerHTML = [
    [state.data.stats.roadmaps, "roadmap"],
    [state.data.stats.notes, "note canonical"],
    [state.data.stats.lessons, "bài giảng hoàn thiện"],
  ].map(([value, label]) => `<p class="source-id"><strong>${Number(value).toLocaleString("vi-VN")}</strong> ${label}</p>`).join("");
  elements.sources.innerHTML = `<p class="source-id">Schema v${state.data.schemaVersion}</p><p class="source-id">Brain v${escapeHtml(state.data.brainVersion)}</p><p class="source-id">Draft, raw source và 3_Toi bị loại khỏi index.</p>`;
  document.title = `${spaceLabel()} · Rabbit Data`;
}

function spaceLabel() {
  return ({ roadmap: "Roadmap", brain: "Second Brain", lessons: "Bài giảng" })[state.space];
}

function setOptions(options) {
  elements.filter.innerHTML = options.map(([value, label]) => `<option value="${escapeHtml(value)}">${escapeHtml(label)}</option>`).join("");
  elements.filter.value = state.filter;
}

function configureSidebar() {
  elements.programSwitch.hidden = state.space === "brain";
  elements.brainModes.hidden = state.space !== "brain";
  if (state.space === "roadmap") {
    elements.sidebarKicker.textContent = "LỘ TRÌNH";
    elements.sidebarTitle.textContent = "Roadmap chương trình";
    elements.filterLabel.textContent = "Cấp roadmap";
    setOptions([["", "Tất cả cấp"], ["program", "Chương trình"], ["phase", "Giai đoạn"], ["module", "Mô-đun"]]);
    elements.search.placeholder = "Tìm trong Roadmap…";
  } else if (state.space === "brain") {
    elements.sidebarKicker.textContent = "TRI THỨC";
    elements.sidebarTitle.textContent = "Second Brain";
    elements.filterLabel.textContent = "Domain";
    setOptions([["", "Tất cả domain"], ...state.data.domains.map((item) => [item.name, `${item.name} · ${item.count}`])]);
    elements.search.placeholder = "Tìm concept, câu hỏi, tag…";
  } else {
    elements.sidebarKicker.textContent = "LỚP HỌC";
    elements.sidebarTitle.textContent = "Bài giảng hoàn thiện";
    elements.filterLabel.textContent = "Trạng thái";
    setOptions([["", "Sẵn sàng owner review"]]);
    elements.search.placeholder = "Tìm bài giảng…";
  }
}

function matchesQuery(item) {
  const terms = normalize(state.query).split(/\s+/).filter(Boolean);
  return !terms.length || terms.every((term) => item._search.includes(term));
}

function filteredItems() {
  let items;
  if (state.space === "roadmap") {
    items = state.data.roadmaps.filter((item) => (!state.program || item.program === state.program) && (!state.filter || item.level === state.filter));
  } else if (state.space === "brain") {
    items = state.data.notes.filter((item) => !state.filter || item.domain === state.filter);
    if (state.listMode === "favorites") items = items.filter((item) => state.favorites.has(item.id));
    if (state.listMode === "recent") {
      const order = new Map(state.recent.map((id, index) => [id, index]));
      items = items.filter((item) => order.has(item.id)).sort((a, b) => order.get(a.id) - order.get(b.id));
    }
  } else {
    items = state.data.lessons.filter((item) => !state.program || item.program === state.program);
  }
  return items.filter(matchesQuery);
}

function cardMeta(item) {
  if (state.space === "roadmap") {
    const level = ({ program: "Chương trình", phase: `Giai đoạn ${item.phaseNumber}`, module: `Mô-đun ${item.moduleNumber}` })[item.level];
    return `<span class="domain">${item.program}</span><span>${level}</span>`;
  }
  if (state.space === "brain") return `<span class="domain">${escapeHtml(item.domain)}</span><span>${item.wordCount.toLocaleString("vi-VN")} từ</span>`;
  return `<span class="domain">${item.program}</span><span>Bài ${String(item.lessonNumber).padStart(3, "0")}</span><span>${item.durationMinutes}′</span>`;
}

function renderList() {
  const items = filteredItems();
  elements.count.textContent = `${items.length.toLocaleString("vi-VN")} mục`;
  if (!items.length) {
    elements.list.innerHTML = `<div class="list-empty">Không tìm thấy nội dung phù hợp.<br>Thử bỏ bớt từ khóa hoặc bộ lọc.</div>`;
    return;
  }
  elements.list.innerHTML = items.slice(0, 300).map((item) => `<button class="content-card ${item.id === state.activeId ? "active" : ""}" data-item-id="${escapeHtml(item.id)}" type="button" role="option" aria-selected="${item.id === state.activeId}"><strong>${escapeHtml(item.title)}</strong><span>${cardMeta(item)}</span></button>`).join("");
}

function renderMarkdown(markdown, preprocess = false) {
  const source = preprocess ? preprocessWiki(markdown) : markdown;
  const html = DOMPurify.sanitize(marked.parse(source), { ADD_ATTR: ["data-wiki", "class"], ADD_TAGS: ["details", "summary"] });
  elements.body.innerHTML = html;
  return mermaid.run({ nodes: elements.body.querySelectorAll(".mermaid") }).catch((error) => {
    showToast("Một sơ đồ không render được; nội dung gốc vẫn được giữ.");
    console.error(error);
  });
}

function renderOutline() {
  const headings = [...elements.body.querySelectorAll("h2, h3")];
  elements.outline.innerHTML = headings.slice(0, 36).map((heading, index) => {
    heading.id = `section-${index}`;
    return `<a href="#section-${index}" class="outline-${heading.tagName.toLowerCase()}">${escapeHtml(heading.textContent)}</a>`;
  }).join("") || `<p class="source-id">Không có mục con</p>`;
}

function showReader() {
  elements.empty.hidden = true;
  elements.reader.hidden = false;
  elements.context.hidden = false;
  elements.sidebar.classList.remove("open");
  window.scrollTo({ top: 0, behavior: "instant" });
}

function relationButton(id, kind, label) {
  const item = kind === "roadmap" ? state.roadmapsById.get(id) : state.notesById.get(id);
  return item ? `<button class="relation-button" data-open-kind="${kind}" data-open-id="${escapeHtml(id)}" type="button">${escapeHtml(label || item.title)}</button>` : "";
}

async function openRoadmap(id, updateHash = true) {
  const item = state.roadmapsById.get(id);
  if (!item) return;
  state.space = "roadmap";
  state.activeId = id;
  syncSpaceControls();
  showReader();
  elements.domain.textContent = item.programName;
  elements.status.textContent = ({ program: "Chương trình", phase: "Giai đoạn", module: "Mô-đun" })[item.level];
  elements.title.textContent = item.title;
  elements.question.textContent = item.excerpt;
  elements.meta.innerHTML = pills([item.program, item.level, `${item.wordCount.toLocaleString("vi-VN")} từ`]);
  elements.favorite.hidden = true;
  elements.assetTabs.hidden = true;
  await renderMarkdown(item.body);
  renderOutline();
  const parent = item.parentId ? relationButton(item.parentId, "roadmap", "↑ " + state.roadmapsById.get(item.parentId)?.title) : "";
  const children = item.childIds.map((childId) => relationButton(childId, "roadmap")).join("");
  elements.connectionsTitle.textContent = "Cấu trúc lộ trình";
  elements.connections.innerHTML = parent + children || `<p class="source-id">Không có cấp liền kề</p>`;
  elements.sources.innerHTML = `<p class="source-id">${escapeHtml(item.path)}</p>`;
  renderList();
  if (updateHash) history.replaceState(null, "", `#roadmap=${encodeURIComponent(id)}`);
  document.title = `${item.title} · Rabbit Data`;
}

function pushRecent(noteId) {
  state.recent = [noteId, ...state.recent.filter((id) => id !== noteId)].slice(0, 40);
  localStorage.setItem("rabbit-data:recent", JSON.stringify(state.recent));
}

async function openNote(id, updateHash = true) {
  const note = state.notesById.get(id);
  if (!note) return;
  state.space = "brain";
  state.activeId = id;
  pushRecent(id);
  syncSpaceControls();
  showReader();
  elements.domain.textContent = note.domain;
  elements.status.textContent = "Canonical";
  elements.title.textContent = note.title;
  elements.question.textContent = note.question;
  elements.meta.innerHTML = pills([note.noteType, `${note.wordCount.toLocaleString("vi-VN")} từ`, `Duyệt ${note.approvedAt}`, ...note.tags.slice(0, 6)]);
  elements.favorite.hidden = false;
  elements.favorite.textContent = state.favorites.has(id) ? "★" : "☆";
  elements.favorite.setAttribute("aria-label", state.favorites.has(id) ? "Bỏ lưu note" : "Lưu note");
  elements.assetTabs.hidden = true;
  await renderMarkdown(note.body, true);
  renderOutline();
  const groups = [["Xây trên", note.relationships.buildsOn], ["Mở đường cho", note.relationships.prerequisiteOf], ["Liên quan", note.relationships.relatedTo]];
  elements.connectionsTitle.textContent = "Quan hệ tri thức";
  elements.connections.innerHTML = groups.filter(([, ids]) => ids.length).map(([label, ids]) => `<div class="relation-group"><strong>${label}</strong>${ids.map((relation) => relationButton(relation, "brain")).join("")}</div>`).join("") || `<p class="source-id">Không có liên kết trực tiếp</p>`;
  elements.sources.innerHTML = note.sourceIds.map((sourceId) => `<p class="source-id">${escapeHtml(sourceId)}</p>`).join("") || `<p class="source-id">Không có source ID</p>`;
  renderList();
  if (updateHash) history.replaceState(null, "", `#note=${encodeURIComponent(id)}`);
  document.title = `${note.title} · Rabbit Data`;
}

async function openLesson(id, assetKey = state.activeAsset, updateHash = true) {
  const lesson = state.lessonsById.get(id);
  if (!lesson) return;
  const asset = lesson.assets.find((item) => item.key === assetKey) || lesson.assets[0];
  state.space = "lessons";
  state.activeId = id;
  state.activeAsset = asset.key;
  syncSpaceControls();
  showReader();
  elements.domain.textContent = `${lesson.programName} · Bài ${String(lesson.lessonNumber).padStart(3, "0")}`;
  elements.status.textContent = "Owner review";
  elements.title.textContent = lesson.title;
  elements.question.textContent = lesson.centralQuestion || lesson.objective;
  elements.meta.innerHTML = pills([lesson.targetLevel, `${lesson.durationMinutes} phút`, `${lesson.sceneCount} scene`, `P${String(lesson.phaseNumber).padStart(2, "0")}`, `M${String(lesson.moduleNumber).padStart(2, "0")}`]);
  elements.favorite.hidden = true;
  elements.assetTabs.hidden = false;
  elements.assetTabs.innerHTML = lesson.assets.map((item) => `<button class="asset-button ${item.key === asset.key ? "active" : ""}" data-asset-key="${item.key}" type="button">${escapeHtml(item.label)}</button>`).join("");
  await renderMarkdown(asset.body);
  renderOutline();
  const roadmapId = `roadmap.${lesson.program}.P${String(lesson.phaseNumber).padStart(2, "0")}.M${String(lesson.moduleNumber).padStart(2, "0")}`;
  elements.connectionsTitle.textContent = "Điểm nối";
  elements.connections.innerHTML = relationButton(roadmapId, "roadmap", "Mở roadmap mô-đun");
  elements.sources.innerHTML = `<p class="source-id">${escapeHtml(lesson.path)}/${escapeHtml(asset.filename)}</p><p class="source-id">Chỉ xuất bản lesson có status ready-for-owner-review.</p>`;
  renderList();
  if (updateHash) history.replaceState(null, "", `#lesson=${encodeURIComponent(id)}&asset=${encodeURIComponent(asset.key)}`);
  document.title = `${lesson.id} · ${lesson.title} · Rabbit Data`;
}

function syncSpaceControls() {
  document.querySelectorAll(".space-button").forEach((button) => button.classList.toggle("active", button.dataset.space === state.space));
  document.querySelectorAll(".program-button").forEach((button) => button.classList.toggle("active", button.dataset.program === state.program));
  configureSidebar();
  renderList();
}

function switchSpace(space) {
  if (!['roadmap', 'brain', 'lessons'].includes(space)) return;
  state.space = space;
  state.activeId = null;
  state.query = "";
  state.program = "";
  state.filter = "";
  elements.search.value = "";
  syncSpaceControls();
  renderHome();
  history.replaceState(null, "", `#space=${space}`);
}

function findWikiTarget(label) {
  const needle = normalize(label);
  return state.data.notes.find((note) => note.id === label || normalize(note.title) === needle || note.aliases.some((alias) => normalize(alias) === needle));
}

function toggleFavorite() {
  if (state.space !== "brain" || !state.activeId) return;
  if (state.favorites.has(state.activeId)) state.favorites.delete(state.activeId); else state.favorites.add(state.activeId);
  localStorage.setItem("rabbit-data:favorites", JSON.stringify([...state.favorites]));
  elements.favorite.textContent = state.favorites.has(state.activeId) ? "★" : "☆";
  showToast(state.favorites.has(state.activeId) ? "Đã lưu note" : "Đã bỏ lưu");
  renderList();
}

function showToast(message) {
  elements.toast.textContent = message;
  elements.toast.classList.add("show");
  clearTimeout(showToast.timer);
  showToast.timer = setTimeout(() => elements.toast.classList.remove("show"), 2200);
}

function resolveRoadmapLink(href) {
  if (!href || /^(?:https?:|#|mailto:)/.test(href) || state.space !== "roadmap") return null;
  const current = state.roadmapsById.get(state.activeId);
  if (!current) return null;
  const base = new URL(current.path, "https://rabbit.local/");
  const path = decodeURIComponent(new URL(href, base).pathname.replace(/^\//, ""));
  return state.roadmapsByPath.get(path) || null;
}

function bindEvents() {
  let timer;
  elements.search.addEventListener("input", () => {
    clearTimeout(timer);
    timer = setTimeout(() => { state.query = elements.search.value; renderList(); }, 100);
  });
  elements.filter.addEventListener("change", () => { state.filter = elements.filter.value; renderList(); });
  elements.list.addEventListener("click", (event) => {
    const button = event.target.closest("[data-item-id]");
    if (!button) return;
    if (state.space === "roadmap") openRoadmap(button.dataset.itemId);
    else if (state.space === "brain") openNote(button.dataset.itemId);
    else openLesson(button.dataset.itemId, "note");
  });
  document.querySelectorAll(".space-button").forEach((button) => button.addEventListener("click", () => switchSpace(button.dataset.space)));
  document.querySelectorAll(".program-button").forEach((button) => button.addEventListener("click", () => {
    state.program = button.dataset.program;
    document.querySelectorAll(".program-button").forEach((item) => item.classList.toggle("active", item === button));
    renderList();
  }));
  document.querySelectorAll("[data-list-mode]").forEach((button) => button.addEventListener("click", () => {
    state.listMode = button.dataset.listMode;
    document.querySelectorAll("[data-list-mode]").forEach((item) => item.classList.toggle("active", item === button));
    renderList();
  }));
  $("#clear-filters").addEventListener("click", () => {
    state.query = ""; state.program = ""; state.filter = ""; state.listMode = "all";
    elements.search.value = "";
    document.querySelectorAll("[data-list-mode]").forEach((item) => item.classList.toggle("active", item.dataset.listMode === "all"));
    syncSpaceControls();
  });
  elements.connections.addEventListener("click", (event) => {
    const button = event.target.closest("[data-open-kind]");
    if (!button) return;
    if (button.dataset.openKind === "roadmap") openRoadmap(button.dataset.openId);
    else openNote(button.dataset.openId);
  });
  elements.assetTabs.addEventListener("click", (event) => {
    const button = event.target.closest("[data-asset-key]");
    if (button) openLesson(state.activeId, button.dataset.assetKey);
  });
  elements.body.addEventListener("click", (event) => {
    const wiki = event.target.closest("[data-wiki]");
    if (wiki) {
      event.preventDefault();
      const note = findWikiTarget(wiki.dataset.wiki);
      if (note) openNote(note.id); else showToast("Không tìm thấy note đích.");
      return;
    }
    const link = event.target.closest("a[href]");
    const roadmap = link ? resolveRoadmapLink(link.getAttribute("href")) : null;
    if (roadmap) { event.preventDefault(); openRoadmap(roadmap.id); }
  });
  elements.favorite.addEventListener("click", toggleFavorite);
  $("#brand-home").addEventListener("click", (event) => { event.preventDefault(); state.activeId = null; renderHome(); });
  $("#nav-toggle").addEventListener("click", () => elements.sidebar.classList.toggle("open"));
  $("#theme-toggle").addEventListener("click", () => {
    const next = document.documentElement.dataset.theme === "light" ? "dark" : "light";
    document.documentElement.dataset.theme = next;
    localStorage.setItem("rabbit-data:theme", next);
  });
  document.addEventListener("keydown", (event) => {
    if (((event.ctrlKey || event.metaKey) && event.key.toLowerCase() === "k") || (event.key === "/" && !/input|textarea/i.test(document.activeElement.tagName))) {
      event.preventDefault(); elements.search.focus(); elements.search.select();
    }
    if (event.key === "Escape") { elements.search.blur(); elements.sidebar.classList.remove("open"); }
  });
}

async function restoreRoute() {
  const params = new URLSearchParams(location.hash.slice(1));
  if (params.get("roadmap")) return openRoadmap(params.get("roadmap"), false);
  if (params.get("note")) return openNote(params.get("note"), false);
  if (params.get("lesson")) return openLesson(params.get("lesson"), params.get("asset") || "note", false);
  switchSpace(params.get("space") || "roadmap");
}

async function initialize() {
  configureMarkdown();
  document.documentElement.dataset.theme = localStorage.getItem("rabbit-data:theme") || "dark";
  state.data = await loadData();
  prepareData();
  elements.release.textContent = `Portal v${state.data.portalVersion} · ${state.data.stats.lessons} bài sẵn sàng`;
  bindEvents();
  await restoreRoute();
  elements.app.setAttribute("aria-busy", "false");
}

initialize().catch((error) => {
  console.error(error);
  elements.empty.innerHTML = `<h1>Không thể mở Rabbit Data</h1><p>${escapeHtml(error.message)}</p><p>Hãy chạy lại <code>npm run brain:index</code>.</p>`;
  elements.app.setAttribute("aria-busy", "false");
});
