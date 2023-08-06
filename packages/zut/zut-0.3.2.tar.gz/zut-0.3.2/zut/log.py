from __future__ import annotations
import logging, logging.config, os, atexit
from .format import BACKGROUND_RED, FOREGROUND_RED

class CountHandler(logging.Handler):
    def __init__(self, level=logging.WARNING):
        self.counts: dict[int, int] = {}
        atexit.register(self.print_counts)
        super().__init__(level=level)

    def print_counts(self):
        msg = ""

        levelnos = sorted(self.counts.keys(), reverse=True)
        for levelno in levelnos:
            msg += (", " if msg else "") + "%s: %d" % (logging.getLevelName(levelno), self.counts[levelno])

        if msg:
            print("Logged " + msg)

    def emit(self, record: logging.LogRecord):
        if record.levelno >= self.level:
            if not record.levelno in self.counts:
                self.counts[record.levelno] = 1
            else:
                self.counts[record.levelno] += 1

def configure_logging(config: dict = None, nocount = False, level = logging.INFO):
    if not config:
        config = {
            "version": 1,
            "disable_existing_loggers": False,
            "formatters": {
                "standard": { 
                    "format": "%(levelname)s [%(name)s] %(message)s"
                },
            },
            "handlers": {
                "console": {
                    "level": "DEBUG",
                    "class": "logging.StreamHandler",
                    "formatter": "standard",
                }
            },
            "loggers": {
                "": { # root logger
                    "handlers": ["console"],
                    "level": os.environ["LOGLEVEL"].upper() if "LOGLEVEL" in os.environ else logging.getLevelName(level),
                },
            },
        }

        if not nocount:
            config["handlers"]["count"] = {
                "level": "WARNING",
                "class": CountHandler.__module__ + '.' + CountHandler.__qualname__,
            }
            for logger in config["loggers"]:
                config["loggers"][logger]["handlers"].append("count")

    # Color logging levels equal or greater than WARNING
    logging.addLevelName(logging.WARNING, FOREGROUND_RED % logging.getLevelName(logging.WARNING))
    logging.addLevelName(logging.ERROR, BACKGROUND_RED % logging.getLevelName(logging.ERROR))
    logging.addLevelName(logging.CRITICAL, BACKGROUND_RED % logging.getLevelName(logging.CRITICAL))

    # Apply configuration
    logging.config.dictConfig(config)
