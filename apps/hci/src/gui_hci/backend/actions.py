import os
from PySide6.QtWidgets import QFileDialog, QFrame
from PySide6.QtCore import (
    QFile,
    QIODevice,
    QTextStream,
    QFileInfo,
    QCoreApplication,
    Qt,
)
from PySide6.QtGui import QKeyEvent
from .constants import LIGHT_THEME, DARK_THEME
from .code_editor import QCodeEditor
from . import Icons


def view_appearance_setColorPalatte(main_window, theme):
    main_window.setTheme(theme)
    main_window.setupIcons()
    main_window.recolorConsole()
    for idx in range(main_window.ui.editor_win.count() - 1):
        main_window.ui.editor_win.widget(idx).setTheme(theme)
        if main_window.ui.editor_win.widget(idx).saveNeeded:
            if theme == LIGHT_THEME:
                main_window.ui.editor_win.setTabIcon(idx, Icons.Light.SaveNeeded)
            else:
                main_window.ui.editor_win.setTabIcon(idx, Icons.Dark.SaveNeeded)
    main_window.ui.actionLight.setChecked(theme == LIGHT_THEME)
    main_window.ui.actionDark.setChecked(theme == DARK_THEME)
    main_window.ui.select_themeMode.setCurrentIndex(theme)


def view_appearance_toggleShowNavbar(main_window, checked):
    main_window.ui.enable_navSidebar.setChecked(checked)
    if checked:
        main_window.ui.context_menu.show()
    else:
        main_window.ui.context_menu.hide()


def view_appearance_toggleShowConsole(main_window, checked):
    if checked:
        main_window.ui.console_win.show()
    else:
        main_window.ui.console_win.hide()


def edit_undo(main_window):
    pressEvent = QKeyEvent(QKeyEvent.KeyPress, Qt.Key_Z, Qt.ControlModifier)
    releaseEvent = QKeyEvent(QKeyEvent.KeyRelease, Qt.Key_Z, Qt.ControlModifier)
    tab = main_window.ui.editor_win.currentWidget()
    QCoreApplication.postEvent(tab, pressEvent)
    QCoreApplication.postEvent(tab, releaseEvent)


def edit_redo(main_window):
    pressEvent = QKeyEvent(
        QKeyEvent.KeyPress, Qt.Key_Z, Qt.ControlModifier | Qt.ShiftModifier
    )
    releaseEvent = QKeyEvent(
        QKeyEvent.KeyRelease, Qt.Key_Z, Qt.ControlModifier | Qt.ShiftModifier
    )
    tab = main_window.ui.editor_win.currentWidget()
    QCoreApplication.postEvent(tab, pressEvent)
    QCoreApplication.postEvent(tab, releaseEvent)


def edit_cut(main_window):
    pressEvent = QKeyEvent(QKeyEvent.KeyPress, Qt.Key_X, Qt.ControlModifier)
    releaseEvent = QKeyEvent(QKeyEvent.KeyRelease, Qt.Key_X, Qt.ControlModifier)
    tab = main_window.ui.editor_win.currentWidget()
    QCoreApplication.postEvent(tab, pressEvent)
    QCoreApplication.postEvent(tab, releaseEvent)


def edit_copy(main_window):
    pressEvent = QKeyEvent(QKeyEvent.KeyPress, Qt.Key_C, Qt.ControlModifier)
    releaseEvent = QKeyEvent(QKeyEvent.KeyRelease, Qt.Key_C, Qt.ControlModifier)
    tab = main_window.ui.editor_win.currentWidget()
    QCoreApplication.postEvent(tab, pressEvent)
    QCoreApplication.postEvent(tab, releaseEvent)


def edit_paste(main_window):
    pressEvent = QKeyEvent(QKeyEvent.KeyPress, Qt.Key_V, Qt.ControlModifier)
    releaseEvent = QKeyEvent(QKeyEvent.KeyRelease, Qt.Key_V, Qt.ControlModifier)
    tab = main_window.ui.editor_win.currentWidget()
    QCoreApplication.postEvent(tab, pressEvent)
    QCoreApplication.postEvent(tab, releaseEvent)


def file_createNewFile(main_window, filePath=None, idx=None):
    newTab = QCodeEditor(
        theme=main_window.theme,
        parent=main_window.ui.editor_win,
        filePath=filePath,
        useSyntaxHighlighting=main_window.syntaxHighlighting,
        autoCompleteBrackets=main_window.autoCompleteBrackets,
    )
    newTab.setFrameShape(QFrame.NoFrame)
    if filePath is None:
        mangler = 0
        for idx in range(main_window.ui.editor_win.count()):
            if "Untitled" in main_window.ui.editor_win.tabText(idx):
                try:
                    mangler = max(
                        mangler,
                        int(main_window.ui.editor_win.tabText(idx).split("-")[-1]),
                    )
                    mangler += 1
                except ValueError:
                    mangler += 1

        if mangler > 0:
            name = f"Untitled-{mangler}"
        else:
            name = "Untitled"
    else:
        name = filePath.split(os.sep)[-1]

    if idx is None:
        idx = main_window.ui.editor_win.count() - 2
    main_window.ui.editor_win.insertTab(idx, newTab, name)
    main_window.ui.editor_win.setCurrentIndex(idx)


def file_openFile(main_window, filePath=None):
    if filePath is None:
        filePath = QFileDialog.getOpenFileName(
            main_window, "Open file...", os.getcwd()
        )[0]
        if filePath == "":
            return
    idx = main_window.ui.editor_win.currentIndex()
    tab = main_window.ui.editor_win.currentWidget()
    if idx > 0 or tab.filePath is not None or tab.toPlainText() != "":
        idx += 1
        file_createNewFile(main_window, filePath=filePath, idx=idx)
    else:
        main_window.ui.editor_win.setTabText(idx, QFileInfo(filePath).fileName())

    readFile = QFile(filePath)
    readFile.open(QIODevice.ReadOnly | QIODevice.ExistingOnly | QIODevice.Text)
    readStr = QTextStream(readFile).readAll()

    tab = main_window.ui.editor_win.widget(idx)
    tab.setPlainText(readStr)
    tab.saveNeeded = False
    tab.filePath = filePath
    main_window.ui.editor_win.setCurrentIndex(idx)


def file_openFolder(main_window):
    dirPath = QFileDialog.getExistingDirectory(
        main_window, "Open folder...", os.getcwd()
    )
    if dirPath == "":
        return
    main_window.ui.filetree.setRootDir(dirPath)


def file_saveFile(main_window, tab=None):
    if tab is None:
        tab = main_window.ui.editor_win.currentWidget()

    if tab.filePath is None:
        file_saveFileAs(main_window, tab=tab)
        return

    saveFile = QFile(tab.filePath)
    saveFile.open(QIODevice.WriteOnly | QIODevice.Text)
    writeStr = tab.toPlainText()
    QTextStream(saveFile) << writeStr
    saveFile.close()
    tab.document().setModified(False)


def file_saveFileAs(main_window, tab=None):
    if tab is None:
        tab = main_window.ui.editor_win.currentWidget()
    filePath = QFileDialog.getSaveFileName(main_window, "Save as...", os.getcwd())[0]
    if filePath == "":
        return
    tab.setFileSavePath(filePath)

    saveFile = QFile(filePath)
    saveFile.open(QIODevice.WriteOnly | QIODevice.Text | QIODevice.NewOnly)
    writeStr = tab.toPlainText()
    QTextStream(saveFile) << writeStr
    saveFile.close()

    tab.document().setModified(False)


def file_closeFolder(main_window):
    main_window.ui.filetree.clearRootDir()


def file_exitEditor(main_window):
    pass
