const { contextBridge, ipcRenderer } = require("electron");

contextBridge.exposeInMainWorld("secondBrainAPI", Object.freeze({
  loadIndex: () => ipcRenderer.invoke("brain:load-index"),
  openBook: (sourceId) => ipcRenderer.invoke("brain:open-book", sourceId),
  platform: process.platform,
}));
