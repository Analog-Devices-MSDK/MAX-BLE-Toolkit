import os
from .constants import *
from .actions import *
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
    fname = QFileDialog.getSaveFileName(
        main_window, "Select/create a logfile", os.getcwd()
    )
    create_fileLogger(main_window, fname[0])

    main_window.ui.logfile_label.setText(f"Log file: {fname[0]}")
    main_window.ui.delete_btn.show()


def console_removeLogfile(main_window):
    main_window.ui.logfile_btn.setText("Add log file")
    remove_fileLogger(main_window)
    main_window.ui.logfile_label.clear()
    main_window.ui.delete_btn.hide()


def settings_applySettings(main_window):
    settings = {
        "syntaxHighlighting": main_window.ui.enable_syntaxHighlighting.isChecked(),
        "autoCompleteBrackets": main_window.ui.enable_bracketAutoComplete.isChecked(),
        "theme": main_window.ui.select_themeMode.currentIndex(),
        "showConsoleWindow": main_window.ui.enable_consoleWindow.isChecked(),
        "showNavigationSidebar": main_window.ui.enable_navSidebar.isChecked(),
        "notifyOnMove": main_window.ui.enable_notifyOnMove.isChecked(),
        "notifyOnDelete": main_window.ui.enable_notifyOnDelete.isChecked(),
        "notifyOnClose": main_window.ui.enable_notifyCloseWithoutSave.isChecked(),
    }

    main_window.applyNewSettings(settings)


def main_codeBtnPressed(main_window):
    if main_window.script_running:
        main_window.logger.user("Program stop requested.")
        main_window.runner.kill_evt.set()
        # print(main_window.runner.kill_evt.is_set())
    else:
        idx = main_window.ui.editor_win.currentIndex()
        codeTxt = main_window.ui.editor_win.widget(idx).toPlainText()
        main_window.runCode(codeTxt)


def registerCallbacks(main_window):
    try:
        main_window.ui.explorer_btn.clicked.connect(
            lambda: nav_showExplorer(main_window)
        )
        main_window.ui.reference_btn.clicked.connect(
            lambda: nav_showReference(main_window)
        )
        main_window.ui.settings_btn.clicked.connect(
            lambda: nav_showSettings(main_window)
        )
        main_window.ui.logfile_btn.clicked.connect(
            lambda: console_addLogfile(main_window)
        )
        main_window.ui.delete_btn.clicked.connect(
            lambda: console_removeLogfile(main_window)
        )
        main_window.ui.applySettings_btn.clicked.connect(
            lambda: settings_applySettings(main_window)
        )
        main_window.ui.runCode_btn.clicked.connect(
            lambda: main_codeBtnPressed(main_window)
        )
        main_window.saveRequested.activated.connect(lambda: file_saveFile(main_window))
        main_window.saveAsRequested.activated.connect(
            lambda: file_saveFileAs(main_window)
        )
    except Exception as err:
        print(err)
