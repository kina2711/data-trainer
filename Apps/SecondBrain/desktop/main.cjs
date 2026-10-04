const { app, BrowserWindow, ipcMain, shell } = require("electron");
const fs = require("node:fs/promises");
const path = require("node:path");
const { pathToFileURL } = require("node:url");

const appRoot = path.resolve(__dirname, "..");
const webRoot = path.join(appRoot, "web");
const indexPath = path.join(webRoot, "data", "brain-index.json");
const manifestPath = path.resolve(appRoot, "..", "..", "Docs", "Second-Brain", "second-brain-manifest.json");
const appUrl = pathToFileURL(path.join(webRoot, "index.html")).href;
const smokeMode = process.env.SECOND_BRAIN_SMOKE === "1";

ipcMain.handle("brain:load-index", async () => JSON.parse(await fs.readFile(indexPath, "utf8")));
ipcMain.handle("brain:open-book", async (_event, sourceId) => {
  if (typeof sourceId !== "string" || !sourceId.startsWith("src.book.")) {
    return { ok: false, error: "Source ID không hợp lệ." };
  }
  const manifest = JSON.parse(await fs.readFile(manifestPath, "utf8"));
  const source = manifest.source_registry.find((item) => item.source_id === sourceId);
  if (!source?.canonical_path) return { ok: false, error: "Không tìm thấy tệp sách cục bộ." };
  const result = await shell.openPath(source.canonical_path);
  return result ? { ok: false, error: result } : { ok: true };
});

function createWindow() {
  const window = new BrowserWindow({
    width: 1480,
    height: 940,
    minWidth: 960,
    minHeight: 640,
    backgroundColor: "#07101d",
    title: "Rabbit Data Learning Portal",
    autoHideMenuBar: true,
    webPreferences: {
      preload: path.join(__dirname, "preload.cjs"),
      contextIsolation: true,
      nodeIntegration: false,
      sandbox: true,
      devTools: !app.isPackaged,
    },
  });
  window.loadURL(appUrl);
  window.webContents.setWindowOpenHandler(({ url }) => {
    if (/^https?:\/\//i.test(url)) shell.openExternal(url);
    return { action: "deny" };
  });
  window.webContents.on("will-navigate", (event, url) => {
    if (url !== appUrl && !url.startsWith(`${appUrl}#`)) event.preventDefault();
  });
  if (smokeMode) {
    window.webContents.once("did-finish-load", () => {
      setTimeout(async () => {
        try {
          const result = await window.webContents.executeJavaScript(`({
            busy: document.querySelector('#app').getAttribute('aria-busy'),
            itemCount: document.querySelector('#result-count').textContent,
            stats: document.querySelector('#portal-stats').textContent,
            activeSpace: document.querySelector('.space-button.active')?.dataset.space,
            error: document.querySelector('#empty-state h1')?.textContent || ''
          })`);
          if (result.busy !== "false" || result.itemCount !== "56 mục" || result.activeSpace !== "roadmap") {
            throw new Error(JSON.stringify(result));
          }
          console.log(`SECOND_BRAIN_SMOKE ${JSON.stringify(result)}`);
          app.exit(0);
        } catch (error) {
          console.error(`SECOND_BRAIN_SMOKE_FAILED ${error.stack || error}`);
          app.exit(1);
        }
      }, 2200);
    });
  }
}

app.whenReady().then(() => {
  createWindow();
  app.on("activate", () => { if (BrowserWindow.getAllWindows().length === 0) createWindow(); });
});

app.on("window-all-closed", () => { if (process.platform !== "darwin") app.quit(); });
