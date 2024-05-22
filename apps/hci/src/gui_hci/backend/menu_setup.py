from .actions import *
from .nav_actions import *
from .constants import LIGHT_THEME, DARK_THEME
from PySide6.QtCore import Qt, QFileInfo
from PySide6.QtWidgets import QMenu, QTreeWidgetItem
from PySide6.QtGui import QAction, QKeySequence


def setup_menubar(main_window, consoleVisible, navVisible):
    setup_menubarView(main_window, consoleVisible, navVisible)
    setup_menubarFile(main_window)
    setup_menubarEdit(main_window)


def setup_menubarFile(main_window):
    main_window.ui.actionNew_file.triggered.connect(
        lambda: file_createNewFile(main_window)
    )
    main_window.ui.actionOpen_File.triggered.connect(lambda: file_openFile(main_window))
    main_window.ui.actionOpen_Folder.triggered.connect(
        lambda: file_openFolder(main_window)
    )
    main_window.ui.actionSave.triggered.connect(lambda: file_saveFile(main_window))
    main_window.ui.actionSave_as.triggered.connect(lambda: file_saveFileAs(main_window))
    main_window.ui.actionClose_folder.triggered.connect(
        lambda: file_closeFolder(main_window)
    )
    main_window.ui.actionExit.triggered.connect(lambda: file_exitEditor(main_window))


def setup_menubarEdit(main_window):
    main_window.ui.actionPaste.setShortcut(QKeySequence.Paste)
    main_window.ui.actionUndo.setShortcut(QKeySequence.Undo)
    main_window.ui.actionRedo.setShortcut(QKeySequence.Redo)
    main_window.ui.actionCut.setShortcut(QKeySequence.Cut)
    main_window.ui.actionCopy.setShortcut(QKeySequence.Copy)
    main_window.ui.actionPaste.triggered.connect(lambda: edit_paste(main_window))
    main_window.ui.actionUndo.triggered.connect(lambda: edit_undo(main_window))
    main_window.ui.actionRedo.triggered.connect(lambda: edit_redo(main_window))
    main_window.ui.actionCut.triggered.connect(lambda: edit_cut(main_window))
    main_window.ui.actionCopy.triggered.connect(lambda: edit_copy(main_window))


def setup_menubarView(main_window, consoleVisible, navVisible):
    main_window.ui.actionLight.triggered.connect(
        lambda: view_appearance_setColorPalatte(main_window, LIGHT_THEME)
    )
    main_window.ui.actionDark.triggered.connect(
        lambda: view_appearance_setColorPalatte(main_window, DARK_THEME)
    )
    main_window.ui.actionShow_navbar.triggered.connect(
        lambda checked: view_appearance_toggleShowNavbar(main_window, checked)
    )
    main_window.ui.actionShow_console.triggered.connect(
        lambda checked: view_appearance_toggleShowConsole(main_window, checked)
    )

    main_window.ui.actionShow_navbar.setChecked(consoleVisible)
    main_window.ui.actionShow_console.setChecked(navVisible)
    if main_window.theme == LIGHT_THEME:
        main_window.ui.actionLight.setChecked(True)
        main_window.ui.actionDark.setChecked(False)
    elif main_window.theme == DARK_THEME:
        main_window.ui.actionLight.setChecked(False)
        main_window.ui.actionDark.setChecked(True)


def setup_menubarHelp(main_window):
    pass


def setupContextMenus(main_window):
    main_window.ui.filetree.setContextMenuPolicy(Qt.CustomContextMenu)
    main_window.ui.filetree.customContextMenuRequested.connect(
        lambda pos: createFiletreeContextMenu(main_window, pos)
    )


def createFiletreeContextMenu(main_window, pos):
    context = QMenu(main_window.ui.filetree)
    if main_window.ui.filetree.topLevelItemCount() > 0:
        selected_item = main_window.ui.filetree.itemAt(pos)
        if selected_item is None:
            newFile_action = QAction("New File", main_window.ui.filetree)
            newFile_action.triggered.connect(
                lambda: nav_createNewFile(main_window, selected_item)
            )
            newFolder_action = QAction("New Folder", main_window.ui.filetree)
            newFolder_action.triggered.connect(
                lambda: nav_createNewFolder(main_window, selected_item)
            )
            closeFolder_action = QAction("Close Folder", main_window.ui.filetree)
            closeFolder_action.triggered.connect(lambda: nav_closeFolder(main_window))
            context.addAction(newFile_action)
            context.addAction(newFolder_action)
            context.addAction(closeFolder_action)

        elif QFileInfo(selected_item.text(1)).isDir():
            newFile_action = QAction("New File", main_window.ui.filetree)
            newFile_action.triggered.connect(
                lambda: nav_createNewFile(main_window, selected_item)
            )
            newFolder_action = QAction("New Folder", main_window.ui.filetree)
            newFolder_action.triggered.connect(
                lambda: nav_createNewFolder(main_window, selected_item)
            )
            delete_action = QAction("Delete", main_window.ui.filetree)
            delete_action.triggered.connect(
                lambda: nav_delete(main_window, selected_item)
            )
            rename_action = QAction("Rename", main_window.ui.filetree)
            rename_action.triggered.connect(
                lambda: nav_rename(main_window, selected_item)
            )
            context.addAction(newFile_action)
            context.addAction(newFolder_action)
            context.addAction(rename_action)
            context.addAction(delete_action)

        else:
            openFile_action = QAction("Open File", main_window.ui.filetree)
            openFile_action.triggered.connect(
                lambda: nav_openFile(main_window, selected_item)
            )
            delete_action = QAction("Delete", main_window.ui.filetree)
            delete_action.triggered.connect(
                lambda: nav_delete(main_window, selected_item)
            )
            rename_action = QAction("Rename", main_window.ui.filetree)
            rename_action.triggered.connect(
                lambda: nav_rename(main_window, selected_item)
            )
            context.addAction(openFile_action)
            context.addAction(rename_action)
            context.addAction(delete_action)

    else:
        openFolder_action = QAction("Open Folder", main_window.ui.filetree)
        openFolder_action.triggered.connect(lambda: nav_openFolder(main_window))
        context.addAction(openFolder_action)

    context.exec(main_window.ui.filetree.mapToGlobal(pos))
