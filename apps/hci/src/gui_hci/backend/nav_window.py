from typing import List, Union, Optional
from pathlib import Path
import os
import sys
from PySide6.QtGui import QFont, QMouseEvent, QDropEvent, QIcon, QPixmap
from PySide6.QtWidgets import (
    QTreeWidgetItem,
    QHeaderView,
    QFileSystemModel,
    QFileIconProvider,
    QTreeWidget,
    QApplication,
    QAbstractItemView,
    QStyledItemDelegate,
    QWidget,
)
from PySide6.QtCore import (
    Qt,
    QDir,
    QFileSystemWatcher,
    QFile,
    QFileInfo,
    QIODevice,
    QTextStream,
    QAbstractItemModel,
    QModelIndex,
    QPersistentModelIndex,
    Signal,
)
from .actions import file_openFile
from .constants import CONFIRMMOVE_MOVE, CONFIRMDELETE_DELETE


class QEditorDelegate(QStyledItemDelegate):
    editingFinished = Signal(QModelIndex)

    def __init__(self, parent):
        super().__init__(parent)

    def setModelData(
        self,
        editor: QWidget,
        model: QAbstractItemModel,
        index: Union[QModelIndex, QPersistentModelIndex],
    ) -> None:
        super().setModelData(editor, model, index)
        if index.column() == 0:
            self.editingFinished.emit(index)


class QCustomIconProvider:
    def __init__(self):
        iconPath = QFileInfo(__file__).absoluteDir()
        iconPath.cdUp()
        iconPath.cd("assets/images/icons/file-icons")
        self.iconPath = iconPath
        self.iconSize = 13

    def icon(self, fileInfo: QFileInfo):
        if fileInfo.isDir():
            pMap = QPixmap(self.iconPath.filePath("folder-neon.svg"))
            pMap = pMap.scaledToHeight(self.iconSize, Qt.SmoothTransformation)
        else:
            if QFileInfo(self.iconPath.filePath(f"{fileInfo.suffix()}.svg")).exists():
                pMap = QPixmap(self.iconPath.filePath(f"{fileInfo.suffix()}.svg"))
            else:
                pMap = QPixmap(self.iconPath.filePath("default.svg"))
            pMap = pMap.scaledToHeight(self.iconSize, Qt.SmoothTransformation)

        return QIcon(pMap)


class QDirectoryTreeItem(QTreeWidgetItem):
    DISPLAY = 0
    RENAME = 1
    NEW_FILE = 2
    NEW_FOLDER = 3

    def __init__(
        self,
        text: Optional[List[str]] = None,
        parent: Optional[QTreeWidgetItem] = None,
        flags: Optional[List[Qt.ItemFlags]] = None,
        indicatorPolicy: Optional[QTreeWidgetItem.ChildIndicatorPolicy] = None,
        nodeState: int = DISPLAY,
    ):
        if parent is not None:
            super().__init__(parent)
            if text is not None:
                for cIdx, cText in enumerate(text):
                    self.setText(cIdx, cText)
        elif text is not None:
            super().__init__(text)

        if flags is not None:
            if isinstance(flags, list):
                combinedFlags = 0
                for val in flags:
                    combinedFlags = combinedFlags | val
            else:
                combinedFlags = flags

            self.setFlags(self.flags() | combinedFlags)

        if indicatorPolicy is not None:
            self.setChildIndicatorPolicy(indicatorPolicy)

        self.currState = nodeState

    def setCurrentNodeState(self, nodeState: int):
        self.currState = nodeState

    def currentNodeState(self) -> int:
        return self.currState


class QDirectoryTree(QTreeWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setDragDropMode(QTreeWidget.InternalMove)
        self.setFocusPolicy(Qt.ClickFocus)
        self.setHeaderHidden(True)
        self.itemDoubleClicked.connect(
            lambda clickedItem, _: self.openSelectedItem(clickedItem)
        )
        # self.itemChanged.connect(self._itemNameChange)
        self.watcher: QFileSystemWatcher = QFileSystemWatcher()
        self.editDelegate: QEditorDelegate = QEditorDelegate(parent)
        self.setItemDelegate(self.editDelegate)
        self.editDelegate.editingFinished.connect(self._editDone)
        self.rootDir: str = None
        self.dirs = None
        self.iconProvider = QCustomIconProvider()
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)

    def setRootDir(self, rootDir):
        self.dirs = {}
        self.rootDir = rootDir
        if self.watcher.directories() or self.watcher.files():
            self.watcher.removePaths(self.watcher.directories() + self.watcher.files())
        self.watcher.addPath(rootDir)
        self.watcher.directoryChanged.connect(self._compileStructure)
        self.itemExpanded.connect(lambda item: self._itemStateChange(item, True))
        self.itemCollapsed.connect(lambda item: self._itemStateChange(item, False))
        self._compileStructure(addWatcherDirs=True)
        self.setColumnHidden(1, True)

    def clearRootDir(self):
        self.dirs = None
        if self.watcher.directories() or self.watcher.files():
            self.watcher.removePaths(self.watcher.directories() + self.watcher.files())
        self.rootDir = None
        self.clear()

    def dropEvent(self, event: QDropEvent) -> None:
        main_window = self._getTopLevelParent()
        currItem: QTreeWidgetItem = event.source().currentItem()
        newPosItem = self.itemAt(event.position().toPoint())
        if newPosItem.text(1) in self.watcher.directories():
            res = main_window.showConfirmMoveDialog(
                currItem.text(0), newPosItem.text(0)
            )
            newPath = newPosItem.text(1)
        elif newPosItem.parent().text(0) != currItem.parent().text(0):
            res = main_window.showConfirmMoveDialog(
                currItem.text(0), newPosItem.parent().text(0)
            )
            newPath = newPosItem.parent().text(1)

        if res == CONFIRMMOVE_MOVE:
            QFile.copy(currItem.text(1), f"{newPath}/{currItem.text(0)}")
            QFile.remove(currItem.text(1))
            currItem.setText(1, f"{newPath}/{currItem.text(0)}")

        event.setDropAction(Qt.IgnoreAction)
        super().dropEvent(event)

    def mousePressEvent(self, event: QMouseEvent) -> None:
        self.clearSelection()
        return super().mousePressEvent(event)

    def createNewFolder(self, clickedItem: QDirectoryTreeItem, main_window=None):
        if main_window is None:
            main_window = self._getTopLevelParent()

        fPath = QFileInfo(clickedItem.text(1))
        cNode = QDirectoryTreeItem(
            text=["", fPath.filePath()],
            flags=Qt.ItemIsEditable,
            nodeState=QDirectoryTreeItem.NEW_FOLDER,
        )
        clickedItem.insertChild(0, cNode)
        if not clickedItem.isExpanded():
            clickedItem.setExpanded(True)

        self.editItem(cNode)

    def createNewFile(self, clickedItem: QDirectoryTreeItem, main_window=None):
        if main_window is None:
            main_window = self._getTopLevelParent()

        fPath = QFileInfo(clickedItem.text(1))
        cNode = QDirectoryTreeItem(
            text=["", fPath.filePath()],
            flags=Qt.ItemIsEditable,
            nodeState=QDirectoryTreeItem.NEW_FILE,
        )
        clickedItem.insertChild(0, cNode)
        if not clickedItem.isExpanded():
            clickedItem.setExpanded(True)

        self.editItem(cNode)

    def renameSelectedItem(self, clickedItem: QDirectoryTreeItem, main_window=None):
        clickedItem.setCurrentNodeState(QDirectoryTreeItem.RENAME)
        self.editItem(clickedItem)

    def openSelectedItem(self, clickedItem: QDirectoryTreeItem, main_window=None):
        if main_window is None:
            main_window = self._getTopLevelParent()

        file_openFile(main_window, filePath=clickedItem.text(1))

    def deleteSelectedItem(self, clickedItem: QDirectoryTreeItem, main_window=None):
        if main_window is None:
            main_window = self._getTopLevelParent()

        if QFileInfo(clickedItem.text(1)).isDir():
            res = main_window.showConfirmDeleteDialog(
                f"{clickedItem.text(0)} and its contents"
            )
            if res == CONFIRMDELETE_DELETE:
                self.watcher.removePath(clickedItem.text(1))
                self.dirs.pop(clickedItem.text(1), None)
                QDir(clickedItem.text(1)).removeRecursively()
        else:
            res = main_window.showConfirmDeleteDialog(clickedItem.text(0))
            if res == CONFIRMDELETE_DELETE:
                QFile.remove(clickedItem.text(1))

    def _editDone(self, idx: QModelIndex):
        cNode: QDirectoryTreeItem = self.itemFromIndex(idx)
        if cNode.currentNodeState() == QDirectoryTreeItem.RENAME:
            newFName = cNode.text(0)
            oldPath = QFileInfo(cNode.text(1))
            if oldPath.fileName() == newFName:
                cNode.setCurrentNodeState(QDirectoryTreeItem.DISPLAY)
                return
            if oldPath.isDir():
                QDir(oldPath.filePath()).rename(
                    oldPath.filePath(), f"{oldPath.path()}/{newFName}"
                )
            else:
                QFile.rename(oldPath.filePath(), f"{oldPath.path()}/{newFName}")
        elif cNode.currentNodeState() == QDirectoryTreeItem.NEW_FILE:
            if cNode.text(0) == "":
                cNode.parent().removeChild(cNode)
                return
            fPath = cNode.text(1)
            fName = cNode.text(0)

            newFile = QFile(f"{fPath}/{fName}")
            newFile.open(QIODevice.WriteOnly | QIODevice.Text | QIODevice.NewOnly)
            out = QTextStream(newFile)
            out << ""
            newFile.close()
        elif cNode.currentNodeState() == QDirectoryTreeItem.NEW_FOLDER:
            if cNode.text(0) == "":
                cNode.parent().removeChild(cNode)
                return
            fPath = QDir(cNode.text(1))
            fName = cNode.text(0)
            fPath.mkdir(fName)
            self.watcher.addPath(f"{fPath}/{fName}")

    def _itemStateChange(self, item: QTreeWidgetItem, itemExpanded: bool):
        self.dirs[item.text(1)] = itemExpanded

    def _getTopLevelParent(self):
        currParent = self.nativeParentWidget()
        prevParent = None
        while True:
            prevParent = currParent
            currParent = currParent.nativeParentWidget()
            if currParent is None:
                return prevParent

    def _compileStructure(self, addWatcherDirs: bool = False):
        self.clear()
        self.addTopLevelItem(self._unpackDirectory(QDir(self.rootDir), addWatcherDirs))
        self._checkExpansion(self.topLevelItem(0))
        self.expandItem(self.topLevelItem(0))

    def _unpackDirectory(self, rDir: QDir, addWatcherDirs: bool):
        headNode = QDirectoryTreeItem(
            text=[rDir.dirName(), rDir.path()],
            flags=Qt.ItemIsEditable,
            indicatorPolicy=QTreeWidgetItem.ShowIndicator,
        )
        headNode.setIcon(0, self.iconProvider.icon(QFileInfo(rDir.path())))
        for entry in rDir.entryInfoList():
            if entry.fileName() in [".", ".."] and entry.isDir():
                continue
            if entry.isDir():
                if addWatcherDirs:
                    self.watcher.addPath(entry.filePath())
                idx = 0
                while headNode.child(idx) is not None:
                    if not QFileInfo(headNode.child(idx).text(1)).isDir():
                        break
                    idx += 1
                headNode.insertChild(
                    idx, self._unpackDirectory(QDir(entry.filePath()), addWatcherDirs)
                )
                # headNode.addChild(self._unpackDirectory(QDir(entry.filePath()), addWatcherDirs))
                continue

            childNode = QDirectoryTreeItem(
                text=[entry.fileName(), entry.filePath()], flags=Qt.ItemIsEditable
            )
            childNode.setIcon(0, self.iconProvider.icon(entry))
            headNode.addChild(childNode)

        self.dirs[rDir.path()] = self.dirs.get(rDir.path(), False)
        return headNode

    def _checkExpansion(self, topItem: QTreeWidgetItem):
        for idx in range(topItem.childCount()):
            cItem = topItem.child(idx)
            if QFileInfo(cItem.text(1)).isDir():
                if cItem.childCount() > 0:
                    cItem.setExpanded(self.dirs.get(cItem.text(1), False))
                self._checkExpansion(cItem)
