import os
from pathlib import Path
import sys
import re
from PySide6.QtCore import (QFile, Qt, QTextStream, QRegularExpression)
from PySide6.QtGui import (QColor, QFont, QFontDatabase, QKeySequence,
                           QSyntaxHighlighter, QTextCharFormat)
from PySide6.QtWidgets import (QApplication, QFileDialog, QMainWindow,
    QPlainTextEdit)
import syntax_patterns

bools = syntax_patterns._bool_vals
logics = syntax_patterns._logic_vals
cblocks = syntax_patterns._cblocks_vals
funcs = syntax_patterns._func_vals
cmds = syntax_patterns._cmd_vals
braces = ['\{', '\}', '\(', '\)']

def format(color, style=''):
    if isinstance(color, tuple):
        if len(color) == 4:
            _color = QColor(color[1], color[2], color[3], color[4])
        else:
            _color = QColor(color[1], color[2], color[3])
    else:
        _color = QColor(color)

    _format = QTextCharFormat()
    _format.setForeground(_color)

    if 'BOLD' in style.upper():
        _format.setFontWeight(QFont.Bold)
    if 'ITALIC' in style.upper():
        _format.setFontItalic(True)
    if 'UNDERLINE' in style.upper():
        _format.setFontUnderline(True)

    return _format

STYLES = {
    'LIGHT' : {
        'BOOL' : format(QColor(29, 29, 194)),
        'LOGIC' : format(QColor(29, 29, 194)),
        'CBLOCK' : format(QColor(126, 3, 224)),
        'FUNC' : format(QColor(128, 104, 2)),
        'CMD' : format(QColor(137, 2, 31)),
        'HEX' : format(QColor(68, 68, 70)),
        'STR' : format(QColor(92, 3, 3)),
        'DEV' : format(QColor(17, 80, 166)),
        'ID' : format(QColor(6, 48, 106)),
        'GROUP_1' : format(QColor(103, 73, 4)),
        'GROUP_2' : format(QColor(90, 42, 127)),
        'GROUP_3' : format(QColor(113, 4, 22)),
        'NUM' : format(QColor(12, 88, 74)),
        'COMMENT' : format(QColor(80, 126, 21)),
    },
    'DARK' : {
        'BOOL' : format(QColor(37, 37, 221)),
        'LOGIC' : format(QColor(37, 37, 221)),
        'CBLOCK' : format(QColor(134, 55, 207)),
        'FUNC' : format(QColor(228, 241, 142)),
        'CMD' : format(QColor(251, 35, 82)),
        'HEX' : format(QColor(153, 153, 165)),
        'STR' : format(QColor(194, 112, 45)),
        'DEV' : format(QColor(18, 181, 237)),
        'ID' : format(QColor(209, 209, 248)),
        'GROUP_1' : format(QColor(248, 183, 35)),
        'GROUP_2' : format(QColor(119, 17, 195)),
        'GROUP_3' : format(QColor(218, 1, 37)),
        'NUM' : format(QColor(240, 251, 212)),
        'COMMENT' : format(QColor(90, 140, 28))
    }
}

class QCustomHighlighter(QSyntaxHighlighter):
    def __init__(self, mode, parent=None):
        super().__init__(parent)
        if mode:
            styles = STYLES['DARK']
        else:
            styles = STYLES['LIGHT']

        self.multilineCommentStart = (QRegularExpression('/*'), 1, STYLES['LIGHT']['COMMENT'])
        self.multilineCommentEnd = (QRegularExpression('*/'), 2, STYLES['LIGHT']['COMMENT'])

        rules = []
        rules += [(fr'\b{x}\b', 0, styles['BOOL']) for x in bools]
        rules += [(fr'\b{x}\b', 0, styles['LOGIC']) for x in logics]
        rules += [(fr'\b{x}\b', 0, styles['CBLOCK']) for x in cblocks]
        rules += [(fr'\b{x}\b', 0, styles['FUNC']) for x in funcs]
        rules += [(fr'\b{x}\b', 0, styles['CMD']) for x in cmds]
        rules += [(fr'{x}', 0, styles['GROUP_1']) for x in braces]
        rules += [
            (r'0x', 0, styles['HEX']),
            (r'"[^"\\]*(\\.[^"\\]*)*"', 0, styles['STR']),
            (r"'[^'\\]*(\\.[^'\\]*)*'", 0, styles['STR']),
            (r'[a-zA-Z_]+[a-zA-Z_0-9]*:', 0, styles['DEV']),
            (r'[a-zA-Z_]+[a-zA-Z_0-9]*', 0, styles['ID']),
            (r'\b[+-]?[0-9]+[lL]?\b', 0, styles['NUM']),
            (r'\b[+-]?0[xX][0-9A-Fa-f]+[lL]?\b', 0, styles['NUM']),
            (r'\b[+-]?[0-9]+(?:\.[0-9]+)?(?:[eE][+-]?[0-9]+)?\b', 0, styles['NUM']),
            (r'//.*', 0, styles['COMMENT'])
        ]

        self.rules = [(QRegularExpression(pat), idx, fmt) for (pat, idx, fmt) in rules]

    def highlightBlock(self, text):
        print(text)
        for expression, nth, fmt in self.rules:
            patMatch = expression.match(text, 0)
            while patMatch.hasMatch():
                idx = patMatch.capturedStart(nth)
                length = patMatch.capturedLength(nth)
                self.setFormat(idx, length, fmt)
                patMatch = expression.match(text, idx+length)

        self.setCurrentBlockState(0)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    editor = QPlainTextEdit()
    highlight = QCustomHighlighter(0, parent=editor.document())
    editor.show()

    app.exec()


# class MainWindow(QMainWindow):
#     def __init__(self, parent=None):
#         QMainWindow.__init__(self, parent)

#         self._highlighter = Highlighter()

#         self.setup_file_menu()
#         self.setup_editor()

#         self.setCentralWidget(self._editor)
#         self.setWindowTitle(self.tr("Syntax Highlighter"))

#     def new_file(self):
#         self._editor.clear()

#     def open_file(self, path=""):
#         file_name = path

#         if not file_name:
#             file_name, _ = QFileDialog.getOpenFileName(self, self.tr("Open File"), "",
#                                                        "Python Files (*.py)")

#         if file_name:
#             in_file = QFile(file_name)
#             if in_file.open(QFile.ReadOnly | QFile.Text):
#                 stream = QTextStream(in_file)
#                 self._editor.setPlainText(stream.readAll())

#     def setup_editor(self):
#         class_format = QTextCharFormat()
#         class_format.setFontWeight(QFont.Bold)
#         class_format.setForeground(Qt.blue)
#         pattern = r'^\s*class\s+\w+\(.*$'
#         self._highlighter.add_mapping(pattern, class_format)

#         function_format = QTextCharFormat()
#         function_format.setFontItalic(True)
#         function_format.setForeground(Qt.blue)
#         pattern = r'^\s*def\s+\w+\s*\(.*\)\s*:\s*$'
#         self._highlighter.add_mapping(pattern, function_format)

#         comment_format = QTextCharFormat()
#         comment_format.setBackground(QColor("#77ff77"))
#         self._highlighter.add_mapping(r'^\s*#.*$', comment_format)

#         font = QFontDatabase.systemFont(QFontDatabase.FixedFont)
#         self._editor = QPlainTextEdit()
#         self._editor.setFont(font)
#         self._highlighter.setDocument(self._editor.document())

#     def setup_file_menu(self):
#         file_menu = self.menuBar().addMenu(self.tr("&File"))

#         new_file_act = file_menu.addAction(self.tr("&New..."))
#         new_file_act.setShortcut(QKeySequence(QKeySequence.New))
#         new_file_act.triggered.connect(self.new_file)

#         open_file_act = file_menu.addAction(self.tr("&Open..."))
#         open_file_act.setShortcut(QKeySequence(QKeySequence.Open))
#         open_file_act.triggered.connect(self.open_file)

#         quit_act = file_menu.addAction(self.tr("E&xit"))
#         quit_act.setShortcut(QKeySequence(QKeySequence.Quit))
#         quit_act.triggered.connect(self.close)

#         help_menu = self.menuBar().addMenu("&Help")
#         help_menu.addAction("About &Qt", qApp.aboutQt)


# class Highlighter(QSyntaxHighlighter):
#     def __init__(self, parent=None):
#         QSyntaxHighlighter.__init__(self, parent)

#         self._mappings = {}

#     def add_mapping(self, pattern, format):
#         self._mappings[pattern] = format

#     def highlightBlock(self, text):
#         for pattern, format in self._mappings.items():
#             for match in re.finditer(pattern, text):
#                 start, end = match.span()
#                 self.setFormat(start, end - start, format)


# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.resize(640, 512)
#     window.show()
#     window.open_file(os.fspath(Path(__file__).resolve()))
#     sys.exit(app.exec())

# from PySide6.QtCore import Qt, QRect, QSize
# from PySide6.QtWidgets import QWidget, QPlainTextEdit, QTextEdit
# from PySide6.QtGui import QColor, QPainter, QTextFormat


# class QLineNumberArea(QWidget):
#     def __init__(self, editor):
#         super().__init__(editor)
#         self.codeEditor = editor

#     def sizeHint(self):
#         return QSize(self.editor.lineNumberAreaWidth(), 0)

#     def paintEvent(self, event):
#         self.codeEditor.lineNumberAreaPaintEvent(event)


# class QCodeEditor(QPlainTextEdit):
#     def __init__(self, parent=None):
#         super().__init__(parent)
#         self.lineNumberArea = QLineNumberArea(self)
#         self.blockCountChanged.connect(self.updateLineNumberAreaWidth)
#         self.updateRequest.connect(self.updateLineNumberArea)
#         self.cursorPositionChanged.connect(self.highlightCurrentLine)
#         self.updateLineNumberAreaWidth(0)

#     def lineNumberAreaWidth(self):
#         space = 3 + self.fontMetrics().averageCharWidth() * 4
#         return space

#     def updateLineNumberAreaWidth(self, _):
#         self.setViewportMargins(self.lineNumberAreaWidth(), 0, 0, 0)

#     def updateLineNumberArea(self, rect, dy):
#         if dy:
#             self.lineNumberArea.scroll(0, dy)
#         else:
#             self.lineNumberArea.update(0, rect.y(), self.lineNumberArea.width(), rect.height())
#         if rect.contains(self.viewport().rect()):
#             self.updateLineNumberAreaWidth(0)

#     def resizeEvent(self, event):
#         super().resizeEvent(event)
#         cr = self.contentsRect()
#         self.lineNumberArea.setGeometry(QRect(cr.left(), cr.top(), self.lineNumberAreaWidth(), cr.height()))

#     def highlightCurrentLine(self):
#         extraSelections = []
#         if not self.isReadOnly():
#             selection = QTextEdit.ExtraSelection()
#             lineColor = QColor(Qt.yellow).lighter(160)
#             selection.format.setBackground(lineColor)
#             selection.format.setProperty(QTextFormat.FullWidthSelection, True)
#             selection.cursor = self.textCursor()
#             selection.cursor.clearSelection()
#             extraSelections.append(selection)
#         self.setExtraSelections(extraSelections)

#     def lineNumberAreaPaintEvent(self, event):
#         painter = QPainter(self.lineNumberArea)

#         painter.fillRect(event.rect(), Qt.lightGray)

#         block = self.firstVisibleBlock()
#         blockNumber = block.blockNumber()
#         top = self.blockBoundingGeometry(block).translated(self.contentOffset()).top()
#         bottom = top + self.blockBoundingRect(block).height()

#         # Just to make sure I use the right font
#         height = self.fontMetrics().height()
#         while block.isValid() and (top <= event.rect().bottom()):
#             if block.isVisible() and (bottom >= event.rect().top()):
#                 number = str(blockNumber + 1)
#                 painter.setPen(Qt.black)
#                 painter.drawText(0, top, self.lineNumberArea.width(), height, Qt.AlignRight, number)

#             block = block.next()
#             top = bottom
#             bottom = top + self.blockBoundingRect(block).height()
#             blockNumber += 1


# if __name__ == '__main__':
#     import sys
#     from PySide6.QtWidgets import QApplication

#     app = QApplication(sys.argv)
#     codeEditor = QCodeEditor()
#     codeEditor.show()
#     sys.exit(app.exec_())