from __future__ import annotations
from typing import Dict, Union, List, Any, Optional
import json
import os
import sys
from PySide6.QtWidgets import QTreeView, QApplication
from PySide6.QtGui import (
    QStandardItemModel,
    QStandardItem,
    QMouseEvent,
    QFont,
    QTextFragment,
    QTextCharFormat,
)
from PySide6.QtCore import (
    QFile,
    QIODevice,
    QTextStream,
    QAbstractItemModel,
    QObject,
    QModelIndex,
    QPersistentModelIndex,
    QDir,
    Qt,
    QFileInfo,
)


class QDeselectableTreeView(QTreeView):
    def __init__(self, parent: Optional[QObject] = None):
        super().__init__(parent)
        self.setDragDropMode(QTreeView.NoDragDrop)
        self.setFocusPolicy(Qt.NoFocus)
        self.alwaysExpandedIndices = []
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.collapsed.connect(self.checkCollapse)

    def mousePressEvent(self, event: QMouseEvent) -> None:
        self.clearSelection()
        return super().mousePressEvent(event)

    def addAlwaysExpandedIdx(self, idx):
        self.alwaysExpandedIndices.append(idx)

    def checkCollapse(self, idx):
        if idx in self.alwaysExpandedIndices:
            self.setExpanded(idx, True)


class QCustomItem(QStandardItem):
    def __init__(self, text):
        super().__init__(text)
        self.setEditable(False)


def populate_referenceTree(main_window):
    model = QStandardItemModel()
    # model = QCustomModel()
    main_window.ui.reftree.setModel(model)
    parentItem = model.invisibleRootItem()

    refDir = QDir(QFileInfo(__file__).absoluteDir().filePath("reference"))
    for entry in refDir.entryInfoList("*.json", filters=QDir.Files):
        jFile = QFile(entry.filePath())
        jFile.open(QIODevice.ReadOnly | QIODevice.ExistingOnly | QIODevice.Text)
        refData = json.loads(QTextStream(jFile).readAll())
        jFile.close()
        if entry.fileName() == "syntax.json":
            parentItem.appendRow(
                buildSyntaxModel(refData, QCustomItem(refData.pop("SECTION_NAME")))
            )
        else:
            parentItem.appendRow(
                buildModel(refData, QCustomItem(refData.pop("SECTION_NAME")))
            )

    for idx_p in range(model.rowCount()):
        cNode = model.item(idx_p)
        if cNode.text() == "HCIScript Syntax":
            continue
        for idx_c in range(cNode.rowCount()):
            tNode = cNode.child(idx_c)
            t0Idx = model.indexFromItem(tNode.child(0))
            t1Idx = model.indexFromItem(tNode.child(1))

            main_window.ui.reftree.setExpanded(t0Idx, True)
            main_window.ui.reftree.setExpanded(t1Idx, True)
            main_window.ui.reftree.addAlwaysExpandedIdx(t0Idx)
            main_window.ui.reftree.addAlwaysExpandedIdx(t1Idx)

    main_window.ui.reftree.setHeaderHidden(True)
    main_window.ui.reftree.setColumnWidth(0, 500)


def buildModel(refDict: Dict[str, Union[str, int]], parent: QStandardItem):
    for key, val in refDict.items():
        if key == "TOOLTIP":
            parent.setToolTip(val)
            continue
        rowItem = QCustomItem(key)
        if isinstance(val, dict):
            parent.appendRow(buildModel(val, rowItem))
        elif val is None:
            rowItem.appendRow(QCustomItem("None"))
            parent.appendRow(rowItem)
        else:
            rowItem.setToolTip(f"Size: {val} bytes")
            parent.appendRow(rowItem)

    return parent


def buildSyntaxModel(refDict: Dict[str, str], parent: QStandardItem):
    structKeys = ["Loops", "Conditionals", "Built-In_Functions"]
    for key in structKeys:
        sectionItem = QCustomItem(key.replace("_", " "))
        structVals = refDict[key]
        for sKey, sVal in structVals.items():
            structItem = QCustomItem(sKey.replace("_", " "))
            structItem.appendRow(QCustomItem(sVal["SYNTAX"]))
            structItem.appendRow(QCustomItem(""))
            exampleItem = QCustomItem("Example:")
            font = exampleItem.font()
            font.setBold(True)
            exampleItem.setFont(font)
            # exampleItem.appendRow(QCustomItem(sVal['Example'].replace('\t', '    ')))
            structItem.appendRow(exampleItem)
            structItem.appendRow(QCustomItem(sVal["Example"].replace("\t", "    ")))
            structItem.appendRow(QCustomItem(""))

            sectionItem.appendRow(structItem)
        parent.appendRow(sectionItem)

    opKeys = ["Mathematical_Operators", "Bitwise_Operators", "Logical_Operators"]
    for key in opKeys:
        sectionItem = QCustomItem(key.replace("_", " "))
        opVals = refDict[key]
        for oKey, oVal in opVals.items():
            sectionItem.appendRow(QCustomItem(" :  ".join([oKey, oVal])))
        parent.appendRow(sectionItem)

    return parent


# def run():
#     app = QApplication(sys.argv)
#     tree = QDeselectableTreeView()
#     model = QStandardItemModel()
#     tree.setModel(model)
#     parentItem = model.invisibleRootItem()

#     refDir = QDir(QFileInfo(__file__).absoluteDir().filePath('reference'))
#     for entry in refDir.entryInfoList('*.json', filters=QDir.Files):
#         jFile = QFile(entry.filePath())
#         jFile.open(QIODevice.ReadOnly | QIODevice.ExistingOnly | QIODevice.Text)
#         refData = json.loads(QTextStream(jFile).readAll())
#         jFile.close()
#         headItem = QStandardItem(refData.pop('SECTION_NAME'))
#         headItem.setEditable(False)
#         parentItem.appendRow(buildModel(refData, headItem))

#     for idx_p in range(model.rowCount()):
#         cNode = model.item(idx_p)
#         for idx_c in range(cNode.rowCount()):
#             tNode = cNode.child(idx_c)
#             t0Idx = model.indexFromItem(tNode.child(0))
#             t1Idx = model.indexFromItem(tNode.child(1))

#             tree.setExpanded(t0Idx, True)
#             tree.setExpanded(t1Idx, True)
#             tree.addAlwaysExpandedIdx(t0Idx)
#             tree.addAlwaysExpandedIdx(t1Idx)

#     tree.setHeaderHidden(True)
#     tree.resizeColumnToContents(0)
#     tree.show()
#     sys.exit(app.exec())
