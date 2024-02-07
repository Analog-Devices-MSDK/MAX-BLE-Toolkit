import os
from .constants import *
from .gui_logger import create_fileLogger, remove_fileLogger
from PySide6.QtWidgets import QFileDialog

def nav_showExplorer(main_window):
    if main_window.ui.explorer_ind.isVisible():
        main_window.ui.explorer_ind.hide()
        main_window.ui.nav_window.hide()
    elif not main_window.ui.nav_window.isVisible():
        main_window.ui.nav_window.setCurrentIndex(EXPLORER_WIN)
        main_window.ui.explorer_ind.show()
        main_window.ui.nav_window.show()
    else:
        main_window.ui.nav_window.setCurrentIndex(EXPLORER_WIN)
        main_window.ui.reference_ind.hide()
        main_window.ui.settings_ind.hide()
        main_window.ui.explorer_ind.show()

    main_window.logger.info("Showing explorer window")

def nav_showReference(main_window):
    if main_window.ui.reference_ind.isVisible():
        main_window.ui.reference_ind.hide()
        main_window.ui.nav_window.hide()
    elif not main_window.ui.nav_window.isVisible():
        main_window.ui.nav_window.setCurrentIndex(REFERENCE_WIN)
        main_window.ui.reference_ind.show()
        main_window.ui.nav_window.show()
    else:
        main_window.ui.nav_window.setCurrentIndex(REFERENCE_WIN)
        main_window.ui.explorer_ind.hide()
        main_window.ui.settings_ind.hide()
        main_window.ui.reference_ind.show()

def nav_showSettings(main_window):
    if main_window.ui.settings_ind.isVisible():
        main_window.ui.settings_ind.hide()
        main_window.ui.nav_window.hide()
    elif not main_window.ui.nav_window.isVisible():
        main_window.ui.nav_window.setCurrentIndex(SETTINGS_WIN)
        main_window.ui.settings_ind.show()
        main_window.ui.nav_window.show()
    else:
        main_window.ui.nav_window.setCurrentIndex(SETTINGS_WIN)
        main_window.ui.explorer_ind.hide()
        main_window.ui.reference_ind.hide()
        main_window.ui.settings_ind.show()

def console_addLogfile(main_window):
    main_window.ui.logfile_btn.setText("Change log file")
    fname = QFileDialog.getSaveFileName(main_window, "Select/create a logfile", os.getcwd())
    create_fileLogger(main_window, fname[0])

    main_window.ui.logfile_label.setText(f'Log file: {fname[0]}')
    main_window.ui.delete_btn.show()

def console_removeLogfile(main_window):
    main_window.ui.logfile_btn.setText("Add log file")
    remove_fileLogger(main_window)
    main_window.ui.logfile_label.clear()
    main_window.ui.delete_btn.hide()

def register_callbacks(main_window):
    try:
        main_window.ui.explorer_btn.clicked.connect(lambda: nav_showExplorer(main_window))
        main_window.ui.reference_btn.clicked.connect(lambda: nav_showReference(main_window))
        main_window.ui.settings_btn.clicked.connect(lambda: nav_showSettings(main_window))
        main_window.ui.logfile_btn.clicked.connect(lambda: console_addLogfile(main_window))
        main_window.ui.delete_btn.clicked.connect(lambda: console_removeLogfile(main_window))
    except Exception as err:
        print(err)
