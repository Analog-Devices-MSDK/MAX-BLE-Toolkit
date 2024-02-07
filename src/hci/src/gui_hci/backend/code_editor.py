import re
from PySide6.QtCore import Qt, QRect, QSize
from PySide6.QtWidgets import QWidget, QPlainTextEdit
from PySide6.QtGui import QColor, QPainter, QSyntaxHighlighter, QTextCharFormat, QFontDatabase
from syntax_patterns import *

class QLineNumberArea(QWidget):
    def __init__(self, editor):
        super().__init__(editor)
        self.codeEditor = editor

    def sizeHint(self):
        return QSize(self.codeEditor.lineNumberAreaWidth(), 0)
    
    def paintEvent(self, event) -> None:
        self.codeEditor.lineNumberAreaPaintEvent(event)

class QCustomHighlighter(QSyntaxHighlighter):
    def __init__(self, parent=None):
        QSyntaxHighlighter.__init__(self, parent)

        self.keyList = []
        self.mappings = {}
        self.insideMultiline = False
        self.nestLevel = 0

    def add_mapping(self, pattern, format):
        self.keyList.append(pattern)
        self.mappings[pattern] = format

    def add_grouping_pattern(self, patternStart, patternEnd, formats):
        self.groupStart = patternStart
        self.groupEnd = patternEnd
        self.groupFormats = formats
        self.numFormats = len(formats)

    def add_multiline_pattern(self, patternStart, patternEnd, format):
        self.multilineStart = patternStart
        self.multilineEnd = patternEnd
        self.multilineFormat = format

    def highlightBlock(self, text):
        print(text)
        self.setCurrentBlockState(0)
        startIdx = 0
        if self.previousBlockState() != 1:
            startIndex = text.
        # if self.insideMultiline:
        #     endMatch = self.multilineEnd.search(text)
        #     if endMatch:
        #         _, end = endMatch.span()
        #         self.insideMultiline = False
        #     else:
        #         end = len(text)
        #     self.setFormat(0, end, self.multilineFormat)
        # else:
        #     startMatch = self.multilineStart.search(text)
        #     if startMatch:
        #         print('here')
        #         start, _ = startMatch.span()
        #         self.setFormat(start, len(text) - start, self.multilineFormat)
        #         self.insideMultiline = True
        #         return
            
        #     for pattern in self.keyList:
        #         for match in pattern.finditer(text):
        #             start, end = match.span()
        #             self.setFormat(start, end - start, self.mappings[pattern])

class QCodeEditor(QPlainTextEdit):
    def __init__(self, mode, parent=None):
        super().__init__(parent)
        self.mode = mode
        self.lineNumberArea = QLineNumberArea(self)
        self.highlighter = QCustomHighlighter()
        self.blockCountChanged.connect(self.updateLineNumberAreaWidth)
        self.updateRequest.connect(self.updateLineNumberArea)
        self.cursorPositionChanged.connect(
            lambda: self.updateLineNumberArea(self.lineNumberArea.contentsRect(), 0))
        self.updateLineNumberAreaWidth(0)
        self.setupSyntaxPatterns()

    def setupSyntaxPatterns(self):
        if self.mode:
            theme = DARK_THEME
        else:
            theme = LIGHT_THEME

        # groupingFormat1 = QTextCharFormat()
        # groupingFormat1.setForeground(theme['GROUP_1'])
        # self.highlighter.add_mapping(GROUPING_PATTERN, groupingFormat1)
        # groupingFormat2 = QTextCharFormat()
        # groupingFormat3 = QTextCharFormat()

        idFormat = QTextCharFormat()
        idFormat.setForeground(theme['ID'])
        self.highlighter.add_mapping(ID_PATTERN, idFormat)

        devFormat = QTextCharFormat()
        devFormat.setForeground(theme['DEV'])
        self.highlighter.add_mapping(DEV_PATTERN, devFormat)

        strFormat = QTextCharFormat()
        strFormat.setForeground(theme['STR'])
        self.highlighter.add_mapping(STR_PATTERN, strFormat)

        cmdFormat = QTextCharFormat()
        cmdFormat.setForeground(theme['CMD'])
        self.highlighter.add_mapping(CMD_PATTERN, cmdFormat)

        funcFormat = QTextCharFormat()
        funcFormat.setForeground(theme['FUNC'])
        self.highlighter.add_mapping(FUNC_PATTERN, funcFormat)

        logicFormat = QTextCharFormat()
        logicFormat.setForeground(theme['LOGIC'])
        self.highlighter.add_mapping(LOGIC_PATTERN, logicFormat)

        cblockFormat = QTextCharFormat()
        cblockFormat.setForeground(theme['CBLOCK'])
        self.highlighter.add_mapping(CBLOCK_PATTERN, cblockFormat)

        bool_format = QTextCharFormat()
        bool_format.setForeground(theme['BOOL'])
        self.highlighter.add_mapping(BOOL_PATTERN, bool_format)

        numFormat = QTextCharFormat()
        numFormat.setForeground(theme['NUM'])
        self.highlighter.add_mapping(NUM_PATTERN, numFormat)

        hexFormat = QTextCharFormat()
        hexFormat.setForeground(theme['HEX'])
        self.highlighter.add_mapping(HEX_PATTERN, hexFormat)

        commentFormat = QTextCharFormat()
        commentFormat.setForeground(theme['COMMENT'])
        self.highlighter.add_mapping(COMMENT_PATTERN, commentFormat)

        multilineFormat = QTextCharFormat()
        multilineFormat.setForeground(theme['COMMENT'])
        self.highlighter.add_multiline_pattern(MULTILINE_PATTERN_START, MULTILINE_PATTERN_END, multilineFormat)

        font = QFontDatabase.systemFont(QFontDatabase.FixedFont)
        self.setFont(font)
        self.highlighter.setDocument(self.document())

    def lineNumberAreaWidth(self):
        return 3 + self.fontMetrics().averageCharWidth()*4
    
    def updateLineNumberAreaWidth(self, _):
        self.setViewportMargins(self.lineNumberAreaWidth(), 0, 0, 0)

    def updateLineNumberArea(self, rect, dy):
        if dy:
            self.lineNumberArea.scroll(0, dy)
        else:
            self.lineNumberArea.update(0, rect.y(), self.lineNumberArea.width(), rect.height())

        if rect.contains(self.viewport().rect()):
            self.updateLineNumberAreaWidth(0)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        cr = self.contentsRect()
        self.lineNumberArea.setGeometry(
            QRect(cr.left(), cr.top(), self.lineNumberAreaWidth(), cr.height()))
        
    def lineNumberAreaPaintEvent(self, event):
        painter = QPainter(self.lineNumberArea)
        painter.fillRect(event.rect(), Qt.lightGray)
        
        block = self.firstVisibleBlock()
        blockNumber = block.blockNumber()
        top = self.blockBoundingGeometry(block).translated(self.contentOffset()).top()
        bottom = top + self.blockBoundingRect(block).height()

        height = self.fontMetrics().height()
        deselectColor = QColor(120, 120, 120)
        selectColor = QColor(0, 255, 0)

        while block.isValid() and (top <= event.rect().bottom()):
            if block.isVisible() and (bottom >= event.rect().top()):
                number = f'{blockNumber + 1}'
                if self.textCursor().blockNumber() == blockNumber:
                    painter.setPen(selectColor)
                else:
                    painter.setPen(deselectColor)

                painter.drawText(0, top, self.lineNumberArea.width(), height, Qt.AlignRight, number)

            block = block.next()
            top = bottom
            bottom = top + self.blockBoundingRect(block).height()
            blockNumber += 1

if __name__ == '__main__':
    import sys
    from PySide6.QtWidgets import QApplication

    app = QApplication(sys.argv)
    codeEditor = QCodeEditor(0)
    codeEditor.show()
    sys.exit(app.exec())