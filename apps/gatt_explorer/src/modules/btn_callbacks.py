import sys
from main_app import *
from . import app_settings
from . import ui_methods
from modules import ble

from bleak import BleakClient
from modules.main_ui import Ui_MainWindow

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)
from PySide6.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QAbstractItemView,
    QApplication,
    QCheckBox,
    QFrame,
    QHBoxLayout,
    QHeaderView,
    QLabel,
    QLineEdit,
    QListWidget,
    QListWidgetItem,
    QMainWindow,
    QPushButton,
    QRadioButton,
    QScrollArea,
    QSizePolicy,
    QSlider,
    QSpacerItem,
    QSplitter,
    QStackedWidget,
    QTableWidget,
    QTableWidgetItem,
    QTextEdit,
    QTreeWidget,
    QTreeWidgetItem,
    QVBoxLayout,
    QWidget,
)


def btn_scan_callback(main_window):
    main_window.ble_scanner: ble.BleScanner
    if main_window.ble_scanner.is_scanning:
        main_window.ble_scanner.is_scanning = False
        main_window.ble_scanner.quit()
        main_window.ble_scanner.wait()
        main_window.ui.btn_scan.setText("Scan")
        return
    else:
        main_window.ui.btn_scan.setText("Scanning...")
        if main_window.ui.check_no_timeout.isChecked():
            main_window.ble_scanner.scan_timeout = 0
        else:
            main_window.ble_scanner.scan_timeout = main_window.ui.scanSlider.value()
        main_window.ble_scanner.start()


def do_connect(main_window: Ui_MainWindow):
    current = main_window.ui.list_widget_discovered.currentItem()
    if current is None:
        return
    main_window.ble_client.peer_address = current.text().split(" ")[:-1]
    main_window.ble_client.stay_connect = True
    main_window.ble_client.run()
    main_window.ui.btn_connect.setText("Disconnect")


def btn_connect_callback(main_window: Ui_MainWindow):
    if main_window.ble_client.is_connected:
        main_window.ble_client.stay_connect = False
        main_window.ui.btn_connect.setText("Connect")

    else:
        do_connect(main_window)


def btn_theme_callback(main_window: Ui_MainWindow):
    # change themes
    if app_settings.THEME == "light":
        app_settings.THEME = "dark"
    else:
        app_settings.THEME = "light"
    ui_methods.set_theme(main_window)


def btn_menu_callback(main_window):
    ui_methods.toggleRightBox(main_window)


def register_button_callbacks(main_window):
    try:
        main_window.ui.btn_scan.clicked.connect(lambda: btn_scan_callback(main_window))
        main_window.ui.btn_connect.clicked.connect(
            lambda: btn_connect_callback(main_window)
        )
        main_window.ui.btn_theme.clicked.connect(
            lambda: btn_theme_callback(main_window)
        )
        main_window.ui.btn_menu.clicked.connect(lambda: btn_menu_callback(main_window))
    except Exception as e:
        main_window.logger.info(e)
