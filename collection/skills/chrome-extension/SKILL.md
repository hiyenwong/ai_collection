---
name: chrome-extension
description: Expert guidance for Chrome extension development with Manifest V3. Use when building Chrome extensions, browser extensions, or working with Chrome APIs. Triggers on: chrome extension, browser extension, manifest v3, chrome api, extension development.
---

# Chrome Extension Development

Expert guidance for Chrome extension development with Manifest V3.

## Code Style and Structure

- Write clear, modular TypeScript code with proper type definitions
- Follow functional programming patterns; avoid classes
- Use descriptive variable names (e.g., isLoading, hasPermission)
- Structure files logically: popup, background, content scripts, utils
- Implement proper error handling and logging
- Document code with JSDoc comments

## Architecture and Best Practices

- Strictly follow Manifest V3 specifications
- Divide responsibilities between background, content scripts and popup
- Configure permissions following the principle of least privilege
- Use modern build tools (webpack/vite) for development
- Implement proper version control and change management

## Chrome API Usage

### Storage

```typescript
// Save data
chrome.storage.local.set({ key: value });

// Read data
const { key } = await chrome.storage.local.get('key');

// Listen for changes
chrome.storage.onChanged.addListener((changes, namespace) => {
  if (changes.key) {
    console.log('Key changed:', changes.key.newValue);
  }
});
```

### Tabs

```typescript
// Create tab
const tab = await chrome.tabs.create({ url: 'https://example.com' });

// Query tabs
const tabs = await chrome.tabs.query({ active: true, currentWindow: true });

// Send message to tab
await chrome.tabs.sendMessage(tabId, { action: 'update' });
```

### Runtime (Messaging)

```typescript
// Background script
chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
  if (message.action === 'getData') {
    sendResponse({ data: 'response' });
  }
  return true; // Keep channel open for async response
});

// Content/Popup script
const response = await chrome.runtime.sendMessage({ action: 'getData' });
```

### Alarms (Scheduled Tasks)

```typescript
// Create alarm
chrome.alarms.create('myAlarm', { periodInMinutes: 30 });

// Listen for alarm
chrome.alarms.onAlarm.addListener((alarm) => {
  if (alarm.name === 'myAlarm') {
    // Execute task
  }
});
```

## Security and Privacy

- Implement Content Security Policy (CSP)
- Handle user data securely
- Prevent XSS and injection attacks
- Use secure messaging between components
- Handle cross-origin requests safely
- Implement secure data encryption
- Follow web_accessible_resources best practices

## Performance and Optimization

- Minimize resource usage and avoid memory leaks
- Optimize background script performance
- Implement proper caching mechanisms
- Handle asynchronous operations efficiently
- Monitor and optimize CPU/memory usage

## Manifest V3 Structure

```json
{
  "manifest_version": 3,
  "name": "My Extension",
  "version": "1.0.0",
  "permissions": ["storage", "activeTab"],
  "background": {
    "service_worker": "background.js"
  },
  "content_scripts": [{
    "matches": ["<all_urls>"],
    "js": ["content.js"]
  }],
  "action": {
    "default_popup": "popup.html"
  }
}
```

## Testing and Debugging

- Use Chrome DevTools effectively
- Write unit and integration tests
- Test cross-browser compatibility
- Monitor performance metrics
- Handle error scenarios

## Publishing Checklist

- [ ] Prepare store listings and screenshots
- [ ] Write clear privacy policies
- [ ] Implement update mechanisms
- [ ] Handle user feedback
- [ ] Maintain documentation