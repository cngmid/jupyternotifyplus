# Installation

## Install from PyPI (recommended)

Once published, you will be able to install Jupyter Notify Plus with:

    pip install jupyternotifyplus

Until then, install from your local source checkout.

---

## Install from source

Clone or download the repository, then run:

    pip install -e .

This installs the package in editable mode, so changes to the source code are reflected immediately.

---

## Loading the extension

In any Jupyter Notebook:

    %load_ext jupyternotifyplus

You should see a confirmation in the browser console that the notification JavaScript has been initialized.

---

## Verifying installation

Run:

    %notifyme success -t "Installation complete" -m "Jupyter Notify Plus is ready"

If your browser shows a notification, everything is working.

---

## Requirements

- Python 3.8 or later
- Jupyter Notebook or JupyterLab
- A browser that supports the Web Notifications API

No additional dependencies are required.

---

## Uninstalling

To remove the package:

    pip uninstall jupyternotifyplus
