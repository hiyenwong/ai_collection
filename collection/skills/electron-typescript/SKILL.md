---
name: electron-typescript
description: Expert guidance for TypeScript, Electron, and Desktop App Development. Use when building desktop applications with Electron, working with IPC, or developing cross-platform desktop apps. Triggers on: electron, desktop app, ipc, main process, renderer process, preload script.
---

# Electron + TypeScript

Expert guidance for TypeScript, Electron, and Desktop App Development.

## Code Style and Structure

- Write concise, type-safe TypeScript code throughout your application
- Structure your project into distinct layers: the main process, renderer processes, and preload scripts
- Organize files by feature, grouping related components, modules, utilities, and styles
- Clearly separate core application logic from UI components to enhance maintainability and testability

## Project Structure

```
electron-app/
├── src/
│   ├── main/           # Main process
│   │   ├── index.ts
│   │   ├── ipc.ts
│   │   └── window.ts
│   ├── preload/        # Preload scripts
│   │   └── index.ts
│   └── renderer/       # Renderer (UI)
│       ├── index.html
│       ├── App.tsx
│       └── components/
├── electron-builder.yml
└── tsconfig.json
```

## Naming Conventions

| Type | Convention | Example |
|------|------------|---------|
| Variables | camelCase | `isWindowOpen` |
| Functions | camelCase | `handleUserEvent` |
| Classes | PascalCase | `MainWindow` |
| Components | PascalCase | `SettingsPanel` |
| Directories | lowercase-hyphen | `main-process` |

## IPC Communication

### Main Process

```typescript
// src/main/ipc.ts
import { ipcMain } from 'electron';

// Handle request-response pattern
ipcMain.handle('get-user-data', async (event, userId) => {
  const user = await database.getUser(userId);
  return user;
});

// Send message to renderer
mainWindow.webContents.send('user-updated', userData);
```

### Preload Script

```typescript
// src/preload/index.ts
import { contextBridge, ipcRenderer } from 'electron';

contextBridge.exposeInMainWorld('electronAPI', {
  getUserData: (userId: string) => 
    ipcRenderer.invoke('get-user-data', userId),
  
  onUserUpdated: (callback: (user: User) => void) => 
    ipcRenderer.on('user-updated', (_, user) => callback(user))
});
```

### Renderer (React)

```typescript
// src/renderer/App.tsx
import { useEffect, useState } from 'react';

declare global {
  interface Window {
    electronAPI: {
      getUserData: (userId: string) => Promise<User>;
      onUserUpdated: (callback: (user: User) => void) => void;
    };
  }
}

function App() {
  const [user, setUser] = useState<User | null>(null);
  
  useEffect(() => {
    window.electronAPI.getUserData('123').then(setUser);
    window.electronAPI.onUserUpdated(setUser);
  }, []);
  
  return <div>{user?.name}</div>;
}
```

## Security Best Practices

### Context Isolation (Required)

```typescript
// ✅ Always enable in BrowserWindow
new BrowserWindow({
  webPreferences: {
    contextIsolation: true,
    nodeIntegration: false,
    preload: path.join(__dirname, 'preload.js')
  }
});
```

### Secure IPC

```typescript
// ✅ Validate all IPC messages
ipcMain.handle('execute-command', (event, command) => {
  if (!isValidCommand(command)) {
    throw new Error('Invalid command');
  }
  return executeCommand(command);
});
```

## Performance Optimization

- Offload heavy computations from the main thread by utilizing background processes or web workers
- Optimize renderer performance by minimizing re-renders and leveraging lazy loading for non-critical modules
- Implement efficient resource management to ensure a smooth, responsive desktop experience
- Use Electron's asynchronous APIs and optimize IPC for fast and secure communication

## Key Conventions

1. Adhere to a "Convention Over Configuration" approach to minimize boilerplate code
2. Prioritize security, performance, and maintainability in every layer of your application
3. Structure your project to clearly separate the main process, renderer processes, and preload scripts
4. Write comprehensive tests and maintain clear documentation for long-term maintenance
5. Leverage Electron's built-in features and extend functionality using established patterns