from .version import __version__

def load_ipython_extension(ipython):
    from .notifyme import load_ipython_extension as _load
    _load(ipython)
