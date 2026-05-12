<<<<<<< HEAD
## Changelog

### DOCUMENTATION


- startup: permission check on load — left-side banner; remove startup confirmation; docs


### OTHER


- update CHANGELOG


=======
## v0.5.0 — Startup permission check and left‑side permission banner

### Summary
Add a startup permission check that runs when the extension is loaded. The extension now shows a compact, left‑aligned permission banner only when needed and is silent when notification permission is already granted.

### Fixes
- Prevents noisy or redundant UI on extension load when notifications are already allowed.
- Removes the small blue confirmation line that previously appeared on startup.

### Behavior changes
- **Permission granted:** no banner or startup line is shown (silent startup).
- **Permission default:** a compact yellow banner appears on the **left** with **Request** and **Dismiss**. The Request button calls `Notification.requestPermission()` and updates the UI based on the result.
- **Permission denied:** the same left banner appears with **Dismiss** only and a short instruction to enable notifications via the browser lock icon → Site settings → Notifications → Allow.
- When native notifications are unavailable or blocked, the extension falls back to an in‑page toast so messages remain visible.

### Implementation notes
- Startup JS now resolves the top window context (`var w = window; while (w !== w.parent) { w = w.parent; }`) so permission checks and requests operate in the same browsing context the browser uses for site permissions.
- The permission banner uses `position: fixed` with `left: 20px; top: 20px;` to appear near the browser permission UI.
- The blue startup confirmation HTML output was removed to keep the extension silent when permission is granted.

### Docs and tests
- `docs/usage.md` updated with a short **Startup Permission Check** paragraph describing the new behavior.
- Tests added/updated to cover the startup JS behavior and banner logic.

### Notes for maintainers
- If you want to change placement or styling, edit `_INIT_JS` (`showPermissionWarning()` / `showToast()`).
- CI: the Bump Version workflow will create the release tag; Build/Publish and docs workflows remain unchanged.
>>>>>>> 6c8e79f (update CHANGELOG and RELEASE_NOTES)
