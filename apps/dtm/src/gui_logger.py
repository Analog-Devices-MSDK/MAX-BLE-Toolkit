import logging
from PySide6.QtCore import Signal, QObject
from PySide6.QtGui import QColor



class CustomFormatter(logging.Formatter):
    COLORS = {
        logging.DEBUG : QColor(),
        logging.INFO : QColor('green'),
        logging.WARNING : QColor('gold'),
        logging.ERROR : QColor('red'),
        logging.CRITICAL : QColor('firebrick')
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
    }
    

    def format(self, record: logging.LogRecord) -> str:
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record), self.COLORS[record.levelno]


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
def setup_guiLogger(main_window, log_level, logger_name='BLE-HCI-GUI'):
    
    console = logging.getLogger(logger_name)
    handler = QLogHandler(main_window.win.console_out)
    formatter = CustomFormatter()
    handler.setFormatter(formatter)
    handler.emitter.log_message.connect(
        lambda data, msg_color: log_consoleBox(main_window, data, msg_color))
    console.addHandler(handler)
    console.setLevel(log_level)

    return logger_name

def log_consoleBox(main_window, data: str, msg_color: QColor):
    current_color = main_window.win.console_out.textColor()
    main_window.win.console_out.setTextColor(msg_color)
    main_window.win.console_out.append(data)
    main_window.win.console_out.setTextColor(current_color)
