from configparser import ConfigParser as _ConfigParser
from importlib import resources

__version__ = "2.4.0"

_cfg = _ConfigParser()

with resources.path("reader", "config.cfg") as _path:
    _cfg.read(str(_path))

URL = _cfg.get("feed", "url")
