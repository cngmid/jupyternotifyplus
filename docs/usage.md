# Usage Overview

Once loaded:

    %load_ext jupyternotifyplus

You have two main commands:

- %notifyme — triggers a notification after the cell finishes  
- %notifyme here — triggers a notification immediately at that line  

---

## End-of-cell notification

    %notifyme -t "Done" -m "Cell finished"

---

## Inline notification

    %notifyme here -t "Checkpoint" -m "Step 1 done"

You can use as many inline notifications as you want.
