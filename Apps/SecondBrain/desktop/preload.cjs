const { contextBridge, ipcRenderer } = require("electron");

contextBridge.exposeInMainWorld("secondBrainAPI", Object.freeze({
  loadIndex: () => ipcRenderer.invoke("brain:load-index"),
  platform: process.platform,
}));
