from PySide6.QtWidgets import QWidget, QGridLayout, QFrame, QTabBar
from PySide6.QtCore import QSize
from .code_editor import QCodeEditor
from .constants import *
from .actions import *


def setup_tabs(main_window, createStarter=True):
    main_window.ui.newTab_btn.clicked.connect(lambda: create_newEditorTab(main_window))
    main_window.ui.editor_win.tabCloseRequested.connect(
        lambda closeIdx: close_editorTab(main_window, closeIdx)
    )

    main_window.ui.editor_win.tabBar().setTabButton(
        0, QTabBar.RightSide, main_window.ui.newTab_btn
    )
    main_window.ui.editor_win.setTabEnabled(0, False)

    main_window.ui.editor_win.setCornerWidget(
        main_window.ui.runCode_btn, Qt.TopRightCorner
    )
    main_window.ui.editor_win.setIconSize(QSize(8, 8))

    if createStarter:
        startTab = QCodeEditor(
            theme=main_window.theme,
            parent=main_window.ui.editor_win,
            useSyntaxHighlighting=main_window.syntaxHighlighting,
            autoCompleteBrackets=main_window.autoCompleteBrackets,
        )
        startTab.setFrameShape(QFrame.NoFrame)
        main_window.ui.editor_win.insertTab(0, startTab, "Untitled")
        main_window.ui.editor_win.setCurrentIndex(0)


def create_newEditorTab(main_window, name=None, idx=None):
    file_createNewFile(main_window, filePath=name, idx=idx)


def close_editorTab(main_window, idx):
    tab = main_window.ui.editor_win.widget(idx)
    res = SAVENEEDED_FALSE
    if tab.saveNeeded:
        if tab.filePath is None and tab.toPlainText() == "":
            res = SAVENEEDED_CLOSE_NOSAVE
        else:
            res = main_window.showSaveNeededDialog(
                fname=main_window.ui.editor_win.tabText(idx)
            )

    if res == SAVENEEDED_CLOSE_CANCEL:
        return
    if res == SAVENEEDED_CLOSE_SAVE:
        file_saveFile(main_window, tab=tab)
        pass
    main_window.ui.editor_win.removeTab(idx)
    tab.deleteLater()

    if main_window.ui.editor_win.count() == 1:
        create_newEditorTab(main_window, idx=0)

    if idx == main_window.ui.editor_win.count() - 1:
        main_window.ui.editor_win.setCurrentIndex(idx - 1)


def tab_updateSaveState(parent, state, tab):
    idx = parent.indexOf(tab)
    if state:
        parent.setTabText(idx, parent.tabText(idx) + "*")
    else:
        parent.setTabText(idx, parent.tabText(idx)[0:-1])
