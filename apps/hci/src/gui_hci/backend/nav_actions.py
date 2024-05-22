import os
from PySide6.QtWidgets import QFileDialog, QFrame
from .constants import LIGHT_THEME, DARK_THEME
from .code_editor import QCodeEditor


def nav_createNewFile(main_window, selected_item):
    if selected_item is None:
        selected_item = main_window.ui.filetree.topLevelItem(0)
    main_window.ui.filetree.createNewFile(selected_item, main_window=main_window)


def nav_createNewFolder(main_window, selected_item):
    if selected_item is None:
        selected_item = main_window.ui.filetree.topLevelItem(0)
    main_window.ui.filetree.createNewFolder(selected_item, main_window=main_window)


def nav_closeFolder(main_window):
    main_window.ui.filetree.clearRootDir()


def nav_delete(main_window, clickedItem):
    main_window.ui.filetree.deleteSelectedItem(clickedItem, main_window=main_window)


def nav_rename(main_window, clickedItem):
    main_window.ui.filetree.renameSelectedItem(clickedItem, main_window=main_window)


def nav_openFile(main_window, clickedItem):
    main_window.ui.filetree.openSelectedItem(clickedItem, main_window=main_window)


def nav_openFolder(main_window):
    dirPath = QFileDialog.getExistingDirectory(
        main_window, "Open folder...", os.getcwd()
    )
    if dirPath == "":
        return
    main_window.ui.filetree.setRootDir(dirPath)
