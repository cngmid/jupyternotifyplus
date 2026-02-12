# Magic Commands

## %notifyme

Triggers a notification after the cell completes.

### Options

- -t : Title  
- -m : Message  
- -o : Include output in message  
- --icon : Custom icon URL  

### Example

    %notifyme -t "Finished" -m "Processing complete"

---

## %notifyme here

Triggers a notification immediately.

    %notifyme here -t "Checkpoint" -m "Step 1 done"
