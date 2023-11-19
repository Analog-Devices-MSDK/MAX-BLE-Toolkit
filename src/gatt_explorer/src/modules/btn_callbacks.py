from main_app import *
from . import app_settings
from . import ui_methods



def btn_scan_callback(main_window):
    pass

def btn_connect_callback(main_window):
    pass

def btn_theme_callback(main_window):
    #change themes
    if app_settings.THEME == "light":
        app_settings.THEME = "dark"
    else:
        app_settings.THEME = "light"
    ui_methods.set_theme(main_window)

def register_button_callbacks(main_window):
    pass
    try:
        main_window.ui.btn_scan.clicked.connect(lambda: btn_scan_callback(main_window))
        main_window.ui.btn_connect.clicked.connect(lambda: btn_connect_callback(main_window))
        main_window.ui.btn_theme.clicked.connect(lambda: btn_theme_callback(main_window))
    except Exception as e:
        print(e)
    