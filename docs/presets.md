# Presets

Presets provide default title, message, and icon.

Available presets:

- success  
- warn  
- error  
- failure  

---

## Inline presets

    %notifyme here success "Step completed"
    %notifyme here warn "Something odd happened"

---

## End-of-cell presets

    %notifyme success
    %notifyme failure

---

## Presets with overrides

    %notifyme success -t "Download complete" -m "Futures updated"
