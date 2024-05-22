from __future__ import annotations
from typing import List, Tuple, Optional, Union, Any
import os
from PySide6.QtCore import (
    Qt,
    QRect,
    QSize,
    QRegularExpression,
    QObject,
    QFile,
    QTextStream,
    QIODevice,
    QFileInfo,
    QDir
)
from PySide6.QtWidgets import QWidget, QPlainTextEdit, QTextEdit, QMenu, QFileDialog
from PySide6.QtGui import (
    QColor,
    QPainter,
    QSyntaxHighlighter,
    QTextCharFormat,
    QFontDatabase,
    QTextBlockUserData,
    QTextCursor,
    QFont,
    QTextDocument,
    QPaintEvent,
    QResizeEvent,
    QKeyEvent,
    QKeySequence,
    QTextBlock,
    QAction,
    QShortcut,
    QIcon
)
from .syntax_patterns import *
from .constants import LIGHT_THEME, DARK_THEME
from . import Icons
# from .tabs import tab_updateSaveState

class EditorContextMenu:
    def __init__(self, parent: QCodeEditor):
        self.parent = parent
        self.undoAvailable = False
        self.redoAvailable = False

    def toggleUndo(self, undoAvailable):
        self.undoAvailable = undoAvailable
    
    def toggleRedo(self, redoAvailable):
        self.redoAvailable = redoAvailable

    def createContextMenu(self, pos):
        context = QMenu(self.parent)
        cMenuAction = QAction("Undo", self.parent)
        cMenuAction.triggered.connect(self.parent.undo)
        cMenuAction.setShortcut(QKeySequence.Undo)
        cMenuAction.setEnabled(self.undoAvailable)
        context.addAction(cMenuAction)
        cMenuAction = QAction("Redo", self.parent)
        cMenuAction.triggered.connect(self.parent.redo)
        cMenuAction.setShortcut(QKeySequence.Redo)
        context.addAction(cMenuAction)
        cMenuAction.setEnabled(self.redoAvailable)
        context.addSeparator()
        cMenuAction = QAction("Cut", self.parent)
        cMenuAction.triggered.connect(self.parent.cut)
        cMenuAction.setShortcut(QKeySequence.Cut)
        context.addAction(cMenuAction)
        cMenuAction = QAction("Copy", self.parent)
        cMenuAction.triggered.connect(self.parent.copy)
        cMenuAction.setShortcut(QKeySequence.Copy)
        context.addAction(cMenuAction)
        cMenuAction = QAction("Paste", self.parent)
        cMenuAction.triggered.connect(self.parent.paste)
        cMenuAction.setShortcut(QKeySequence.Paste)
        context.addAction(cMenuAction)
        context.addSeparator()
        cMenuAction = QAction("Select All", self.parent)
        cMenuAction.triggered.connect(self.parent.selectAll)
        cMenuAction.setShortcut(QKeySequence.SelectAll)
        context.addAction(cMenuAction)

        context.exec(self.parent.mapToGlobal(pos))

        
        

class TextBlockData(QTextBlockUserData):
    def __init__(self, *args: Any, **kwargs: Any):
        super().__init__(*args, **kwargs)
        self.nextBlockStartLevel: int = 0

class QLineNumberArea(QWidget):
    def __init__(self, editor: QCodeEditor, theme: Optional[int]):
        super().__init__(editor)
        self.codeEditor: QCodeEditor = editor
        font = QFontDatabase.systemFont(QFontDatabase.FixedFont)
        self.setFont(font)
        if theme is not None:
            self.setTheme(theme)

    def setTheme(self, theme: int) -> None:
        if theme == LIGHT_THEME:
            self.deselectColor = QColor(70, 78, 105)
            self.selectColor = QColor(153, 193, 241)
            self.numAreaColor = QColor(235, 235, 239)
        elif theme == DARK_THEME:
            self.deselectColor = QColor(222, 221, 218)
            self.selectColor = QColor(153, 193, 241)
            self.numAreaColor = QColor(40, 44, 52)

        self.update()

    def sizeHint(self):
        return QSize(self.codeEditor.lineNumberAreaWidth(), 0)
    
    def paintEvent(self, event: QPaintEvent):
        self.codeEditor.lineNumberAreaPaintEvent(event)

class QCustomHighlighter(QSyntaxHighlighter):
    def __init__(self, parent: Optional[Union[QObject, QTextDocument]] = None) -> None:
        super().__init__(parent)

        self.rules: List[Tuple[QRegularExpression, QTextCharFormat]] = []
        self.groupRule: QRegularExpression = None
        self.groupStartChars: List[str] = []
        self.groupEndChars: List[str] = []
        self.groupFmts: List[QTextCharFormat] = []
        self.multilineStartRule: QRegularExpression = None
        self.multilineEndRule: QRegularExpression = None
        self.multilineFmt: QTextCharFormat = None
        self.setCurrentBlockState(0)

    def addRule(self, pattern: QRegularExpression, fmt: QTextCharFormat) -> None:
        self.rules.append((pattern, fmt))

    def addMultilineRule(
        self,
        patternStart: QRegularExpression,
        patternEnd: QRegularExpression,
        fmt: QTextCharFormat
    ) -> None:
        self.multilineStartRule = patternStart
        self.multilineEndRule = patternEnd
        self.multilineFmt = fmt

    def addGroupingSet(
        self,
        startChars: Union[List[str], str],
        endChars: Union[List[str], str]
    ) -> None:
        if isinstance(startChars, list):
            self.groupStartChars.extend(startChars)
        else:
            self.groupStartChars.append(startChars)

        if isinstance(endChars, list):
            self.groupEndChars.extend(endChars)
        else:
            self.groupEndChars.append(endChars)

        self.groupRule = QRegularExpression(
            '|'.join([f'\\{x}' for x in self.groupStartChars + self.groupEndChars]))
        
    def addGroupingFormat(self, fmts: Union[List[QTextCharFormat], QTextCharFormat]) -> None:
        if isinstance(fmts, list):
            self.groupFmts.extend(fmts)
        else:
            self.groupFmts.append(fmts)

    def highlightBlock(self, text: str) -> None:
        blockData = TextBlockData()
        currBlock = self.currentBlock()
        level = 0
        if currBlock.previous().isValid():
            if currBlock.previous().userData() is not None:
                level = currBlock.previous().userData().nextBlockStartLevel

        if self.currentBlockState() >= -1:
            for pattern, fmt in self.rules:
                patMatch = pattern.match(text)
                while patMatch.hasMatch():
                    pos = patMatch.capturedStart()
                    length = patMatch.capturedLength()
                    self.setFormat(pos, length, fmt)
                    patMatch = pattern.match(text, pos+length)

            patMatch = self.groupRule.match(text)
            while patMatch.hasMatch():
                if patMatch.captured() in self.groupEndChars:
                    level -= 1
                pos = patMatch.capturedStart()
                length = patMatch.capturedLength()

                self.setFormat(pos, length, self.groupFmts[level%len(self.groupFmts)])
                if patMatch.captured() in self.groupStartChars:
                    level += 1

                patMatch = self.groupRule.match(text, pos+length)

        blockData.nextBlockStartLevel = level
        self.setCurrentBlockUserData(blockData)

        if self.multilineStartRule.match(text).hasMatch() or self.previousBlockState() == 1:
            self.highlightMultiline(text)

    def highlightMultiline(self, text: str) -> None:
        self.setCurrentBlockState(0)
        startPos = 0
        if self.previousBlockState() != 1:
            startPos = self.multilineStartRule.match(text).capturedStart()
        while startPos >= 0:
            endMatch = self.multilineEndRule.match(text)
            endPos = endMatch.capturedStart()
            if endPos == -1:
                self.setCurrentBlockState(1)
                length = len(text) - startPos
            else:
                length = endPos - startPos + endMatch.capturedLength()

            self.setFormat(startPos, length, self.multilineFmt)
            startPos = self.multilineStartRule.match(text, startPos+length).capturedStart()

class QCodeEditor(QPlainTextEdit):
    def __init__(
        self,
        theme: Optional[int] = None,
        parent: Optional[QWidget] = None,
        filePath: str = None,
        useSyntaxHighlighting: bool = True,
        autoCompleteBrackets: bool = True
    ) -> None:
        super().__init__(parent)
        self.theme : int = theme
        self.lineNumberArea: QLineNumberArea = QLineNumberArea(self, theme)
        self.highlighter: QCustomHighlighter = QCustomHighlighter() if useSyntaxHighlighting else None
        self.groupOpeners = ['(', '{']
        self.groupClosers = [')', '}']
        self.saveNeeded = False
        self.filePath = filePath
        self.contextMenuGenerator = EditorContextMenu(self)
        self.useSyntaxHighlighting = useSyntaxHighlighting
        self.autoCompleteBrackets = autoCompleteBrackets
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.setupSignals(parent)
        self.setLineWrapMode(QPlainTextEdit.NoWrap)
        self.setTabStopDistance(40)
        self.updateLineNumberAreaWidth(0)
        
        font = QFontDatabase.systemFont(QFontDatabase.FixedFont)
        self.setFont(font)

        if theme is not None and useSyntaxHighlighting:
            self.setupSyntaxPatterns()

    def setTheme(self, theme):
        self.theme = theme
        if self.highlighter is not None:
            self.setupSyntaxPatterns()
        self.lineNumberArea.setTheme(theme)
        self.update()
        self.viewport().update()

    def setAutoCompleteBrackets(self, enable: bool):
        self.autoCompleteBrackets = enable

    def setSyntaxHighlighting(self, enable: bool):
        if enable:
            if self.highlighter is None:
                self.highlighter = QCustomHighlighter()
                if self.theme is not None:
                    self.setupSyntaxPatterns()
                # TODO: LOG WARNING?
        else:
            self.highlighter.setDocument(None)
            self.highlighter = None
        self.update()
        self.viewport().update()

    def setFileSavePath(self, filePath: str):
        self.filePath = filePath

    def setupSignals(self, parent) -> None:
        self.blockCountChanged.connect(self.updateLineNumberAreaWidth)
        self.updateRequest.connect(self.updateLineNumberArea)
        self.cursorPositionChanged.connect(
            lambda: self.updateLineNumberArea(self.lineNumberArea.contentsRect(), 0))
        self.customContextMenuRequested.connect(self.contextMenuGenerator.createContextMenu)
        self.redoAvailable.connect(self.contextMenuGenerator.toggleRedo)
        self.undoAvailable.connect(self.contextMenuGenerator.toggleUndo)
        self.undoAvailable.connect(lambda available: self.updateSaveState(available))
        self.modificationChanged.connect(lambda changed: self.saveStateChange(parent, changed))

    def setupSyntaxPatterns(self) -> None:
        if self.theme == LIGHT_THEME:
            textFmts = LIGHT_THEME_TEXTFORMATS
        else:
            textFmts = DARK_THEME_TEXTFORMATS

        self.highlighter.addGroupingSet('(', ')')
        self.highlighter.addGroupingSet('{', '}')
        self.highlighter.addGroupingFormat(
            [textFmts['GROUP_1'], textFmts['GROUP_2'], textFmts['GROUP_3']])
        
        self.highlighter.addRule(ID_PATTERN, textFmts['ID'])
        self.highlighter.addRule(DEV_PATTERN, textFmts['DEV'])
        self.highlighter.addRule(STR_PATTERN, textFmts['STR'])
        self.highlighter.addRule(CMD_PATTERN, textFmts['CMD'])
        self.highlighter.addRule(FUNC_PATTERN, textFmts['FUNC'])
        self.highlighter.addRule(LOGIC_PATTERN, textFmts['LOGIC'])
        self.highlighter.addRule(CBLOCK_PATTERN, textFmts['CBLOCK'])
        self.highlighter.addRule(BOOL_PATTERN, textFmts['BOOL'])
        self.highlighter.addRule(NUM_PATTERN, textFmts['NUM'])
        self.highlighter.addRule(HEX_PATTERN, textFmts['HEX'])
        self.highlighter.addRule(COMMENT_PATTERN, textFmts['COMMENT'])
        
        self.highlighter.addMultilineRule(
            MULTILINE_PATTERN_START, MULTILINE_PATTERN_END, textFmts['COMMENT'])
        
        self.highlighter.setDocument(self.document())

    def lineNumberAreaWidth(self):
        return 3 + self.fontMetrics().averageCharWidth()*4
    
    def saveStateChange(self, parent, changed):
        idx = parent.indexOf(self)
        if changed:
            self.saveNeeded = True
            if self.theme == LIGHT_THEME:
                parent.setTabIcon(idx, Icons.Light.SaveNeeded)
            else:
                parent.setTabIcon(idx, Icons.Dark.SaveNeeded)
            # parent.setTabText(idx, parent.tabText(idx).replace('*', '') + '*')
        else:
            self.saveNeeded = False
            parent.setTabIcon(idx, Icons.NoIcon)
            # parent.setTabText(idx, parent.tabText(idx).replace('*', ''))

    def updateSaveState(self, available):
        if not available:
            if self.saveNeeded:
                self.document().setModified(False)

    def updateLineNumberAreaWidth(self, _):
        self.setViewportMargins(self.lineNumberAreaWidth(), 0, 0, 0)
    
    def updateLineNumberArea(self, rect: QRect, dy: int) -> None:
        if dy:
            self.lineNumberArea.scroll(0, dy)
        else:
            self.lineNumberArea.update(0, rect.y(), self.lineNumberArea.width(), rect.height())

        if rect.contains(self.viewport().rect()):
            self.updateLineNumberAreaWidth(0)

    def lineNumberAreaPaintEvent(self, event: QPaintEvent) -> None:
        painter = QPainter(self.lineNumberArea)
        painter.fillRect(event.rect(), self.lineNumberArea.numAreaColor)

        block = self.firstVisibleBlock()
        blockNumber = block.blockNumber()
        top = self.blockBoundingGeometry(block).translated(self.contentOffset()).top()
        bottom = top + self.blockBoundingRect(block).height()

        height = self.fontMetrics().height()
        
        while block.isValid() and top <= event.rect().bottom():
            if block.isVisible() and bottom >= event.rect().top():
                number = f'{blockNumber + 1}'
                if self.textCursor().blockNumber() == blockNumber:
                    painter.setPen(self.lineNumberArea.selectColor)
                else:
                    painter.setPen(self.lineNumberArea.deselectColor)

                painter.drawText(
                    0, top, self.lineNumberArea.width(), height, Qt.AlignRight, number)
                
            block = block.next()
            top = bottom
            bottom = top + self.blockBoundingRect(block).height()
            blockNumber += 1

    def resizeEvent(self, event: QResizeEvent) -> None:
        super().resizeEvent(event)
        cr = self.contentsRect()
        self.lineNumberArea.setGeometry(
            QRect(cr.left(), cr.top(), self.lineNumberAreaWidth(), cr.height()))

    def keyPressEvent(self, event: QKeyEvent) -> None:
        if self.autoCompleteBrackets:
            options = {
                '{'  : '}',
                '('  : ')',
                '\r' : '\r'
            }
        else:
            options = {
                '\r' : '\r'
            }
        option = options.get(event.text())

        if option is None:
            super().keyPressEvent(event)
            return

        if option == '\r':
            tc = self.textCursor()
            p = tc.position()
            tc.movePosition(QTextCursor.PreviousCharacter, QTextCursor.KeepAnchor)
            leftOk = tc.selectedText() in ['(', '{']
            tc.setPosition(p, QTextCursor.MoveAnchor)
            tc.movePosition(QTextCursor.NextCharacter, QTextCursor.KeepAnchor)
            rightOk = tc.selectedText() in [')', '}']
            
            tabCount = 0
            for idx in range(len(self.textCursor().block().text())):
                if self.textCursor().block().text()[idx] == '\t':
                    tabCount += 1

            super().keyPressEvent(event)
            tc = self.textCursor()
            p = tc.position()
            if leftOk and rightOk:
                self.insertPlainText(option)
                tc.setPosition(p)
                tabCount += 1

            tc.insertText('\t'*tabCount)
            self.setTextCursor(tc)
            return
        
        super().keyPressEvent(event)
        tc = self.textCursor()
        p = tc.position()
        self.insertPlainText(option)
        tc.setPosition(p)
        self.setTextCursor(tc)

    def _getTopLevelParent(self):
        currParent = self.nativeParentWidget()
        prevParent = None
        while True:
            prevParent = currParent
            currParent = currParent.nativeParentWidget()
            if currParent is None:
                return prevParent
