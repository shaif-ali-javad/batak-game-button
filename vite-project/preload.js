const { contextBridge, ipcRenderer } = require('electron');

contextBridge.exposeInMainWorld('electron', {
  setFullScreen: (isFullScreen) => ipcRenderer.send('set-fullscreen', isFullScreen),
});
