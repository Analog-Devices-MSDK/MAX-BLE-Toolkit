from main_app import *
from . import app_settings
from . import ui_methods

def btn_scan_callback(main_window):
    if main_window.ble_scanner.is_scanning:
        main_window.ble_scanner.is_scanning = False
        main_window.ble_scanner.quit()
        main_window.ble_scanner.wait()
        main_window.ui.btn_scan.setText("Scan")
        return
    else:
        main_window.ui.btn_scan.setText("Scanning...")
        main_window.ble_scanner.scan_timeout = 0
        main_window.ble_scanner.start()

def btn_connect_callback(main_window):
    pass

def btn_theme_callback(main_window):
    #change themes
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
        main_window.ui.btn_connect.clicked.connect(lambda: btn_connect_callback(main_window))
        main_window.ui.btn_theme.clicked.connect(lambda: btn_theme_callback(main_window))
        main_window.ui.btn_menu.clicked.connect(lambda: btn_menu_callback(main_window))
    except Exception as e:
        main_window.logger.info(e)
    