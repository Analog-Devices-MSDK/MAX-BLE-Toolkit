from typing import Dict
import logging

from PySide6.QtCore import Signal, QObject
from PySide6.QtGui import QColor

LIGHT_THEME = 0
DARK_THEME = 1


class CustomFormatter(logging.Formatter):
    COLORS = {
        logging.DEBUG: QColor(),
        logging.INFO: QColor("green"),
        logging.WARNING: QColor("gold"),
        logging.ERROR: QColor("red"),
        logging.CRITICAL: QColor("firebrick")
        # Options added after logging initialization:
        #     logging.USER : QColor('dodgerblue')
        #     logging.PRINT : QColor()
    }

    _THEME_COLORS = {
        DARK_THEME: QColor(222, 221, 218),
        LIGHT_THEME: QColor(70, 78, 105),
    }

    format_str: str = (
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s (%(filename)s:%(lineno)d)"
    )
    format_warning: str = "%(levelname)s - %(message)s"
    format_info: str = "%(levelname)s - %(message)s"
    format_debug: str = "%(levelname)s - %(message)s"

    FORMATS = {
        logging.DEBUG: format_debug,
        logging.INFO: format_info,
        logging.WARNING: format_warning,
        logging.ERROR: format_str,
        logging.CRITICAL: format_str,
        # Options added after logging initialization:
        #     logging.USER : "%(levelname)s - %(message)s"
        #     logging.PRINT : "%(message)s"
    }

    @staticmethod
    def getThemeColor(themeId):
        return CustomFormatter._THEME_COLORS[themeId]

    def addLevelFormat(self, lvl: int, lvlColor: QColor, lvlFormat: str):
        self.COLORS[lvl] = lvlColor
        self.FORMATS[lvl] = lvlFormat

    def format(self, record: logging.LogRecord) -> str:
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record), self.COLORS[record.levelno]


class CustomLogfileFormatter(logging.Formatter):
    format_str: str = (
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s (%(filename)s:%(lineno)d)"
    )
    format_warning: str = "%(levelname)s - %(message)s"
    format_info: str = "%(levelname)s - %(message)s"
    format_debug: str = "%(levelname)s - %(message)s"

    FORMATS = {
        logging.DEBUG: format_debug,
        logging.INFO: format_info,
        logging.WARNING: format_warning,
        logging.ERROR: format_str,
        logging.CRITICAL: format_str,
        # Options added after logging initialization:
        #     logging.USER : "%(levelname)s - %(message)s"
        #     logging.PRINT : "%(message)s"
    }

    def addLevelFormat(self, lvl: int, lvlFormat: str):
        self.FORMATS[lvl] = lvlFormat

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)


class QLogEmitter(QObject):
    log_message = Signal(str, QColor)

    def emitSignal(self, msg, color):
        self.log_message.emit(msg, color)


class QLogHandler(logging.Handler):
    def __init__(self, widget):
        super().__init__()
        self.widget = widget
        self.emitter = QLogEmitter()

    def emit(self, record):
        msg, color = self.format(record)
        self.emitter.emitSignal(msg, color)


def create_fileLogger(main_window, fname):
    console = logging.getLogger(main_window.logger_name)

    to_remove = None
    for handler in console.handlers:
        if isinstance(handler, logging.FileHandler):
            to_remove = handler
            break

    if to_remove is not None:
        console.removeHandler(to_remove)

    handler = logging.FileHandler(fname)
    formatter = CustomLogfileFormatter()
    formatter.addLevelFormat(logging.USER, "%(levelname)s - %(message)s")
    formatter.addLevelFormat(logging.PRINT, "%(message)s")
    handler.setFormatter(CustomLogfileFormatter())
    console.addHandler(handler)


def remove_fileLogger(main_window):
    console = logging.getLogger(main_window.logger_name)

    for handler in console.handlers:
        if isinstance(handler, logging.FileHandler):
            to_remove = handler
            break

    console.removeHandler(to_remove)


def _setup_extra_log_levels():
    userLevel = logging.ERROR + 5
    printLevel = logging.CRITICAL + 5
    logging.addLevelName(userLevel, "USER")
    logging.addLevelName(printLevel, "PRINT")

    def userLogForLevel(self, message, *args, **kwargs):
        if self.isEnabledFor(userLevel):
            self._log(userLevel, message, args, **kwargs)

    def printLogForLevel(self, message, *args, **kwargs):
        if self.isEnabledFor(printLevel):
            self._log(printLevel, message, args, **kwargs)

    def userLogToRoot(message, *args, **kwargs):
        kwargs.setdefault("stacklevel", 3)
        logging.log(userLevel, message, *args, **kwargs)

    def printLogToRoot(message, *args, **kwargs):
        kwargs.setdefault("stacklevel", 3)
        logging.log(printLevel, message, *args, **kwargs)

    setattr(logging, "USER", logging.ERROR + 5)
    setattr(logging, "PRINT", logging.CRITICAL + 5)
    setattr(logging.getLoggerClass(), "user", userLogForLevel)
    setattr(logging.getLoggerClass(), "print", printLogForLevel)
    setattr(logging, "user", userLogToRoot)
    setattr(logging, "print", printLogToRoot)


def setup_guiLogger(main_window, log_level, logger_name="BLE-HCI-GUI"):
    _setup_extra_log_levels()
    console = logging.getLogger(logger_name)
    handler = QLogHandler(main_window.ui.console_out)
    formatter = CustomFormatter()
    formatter.addLevelFormat(
        logging.USER, QColor("dodgerblue"), "%(levelname)s - %(message)s"
    )
    formatter.addLevelFormat(logging.PRINT, QColor(), "%(message)s")
    handler.setFormatter(formatter)
    handler.emitter.log_message.connect(
        lambda data, msg_color: log_consoleBox(main_window, data, msg_color)
    )
    console.addHandler(handler)
    console.setLevel(log_level)

    return logger_name


def log_consoleBox(main_window, data: str, msg_color: QColor):
    if not msg_color.isValid():
        msg_color = CustomFormatter.getThemeColor(main_window.theme)
    current_color = main_window.ui.console_out.textColor()
    main_window.ui.console_out.setTextColor(msg_color)
    main_window.ui.console_out.append(data)
    main_window.ui.console_out.setTextColor(current_color)
