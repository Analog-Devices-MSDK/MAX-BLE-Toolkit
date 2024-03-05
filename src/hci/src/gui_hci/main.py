from typing import Dict, Any
import logging
import sys
from PySide6.QtWidgets import QMainWindow, QApplication, QTabBar, QToolButton, QFrame
from PySide6.QtGui import QShortcut, QKeySequence, QCloseEvent, QTextCursor, QTextCharFormat
from PySide6.QtCore import QSize, QSettings, QFile, QIODevice, QTextStream
from PySide6.QtCore import Qt, QCoreApplication, QFileInfo, QByteArray, QThread
from backend import *

class MainWindow(QMainWindow):
    LIGHT = 0
    DARK = 1

    def __init__(self, log_level):
        QMainWindow.__init__(self)
        Icons.initIcons()
        self.theme = None
        self.notifyOnMove = None
        self.notifyOnDelete = None
        self.notifyOnClose = None
        self.autoCompleteBrackets = None
        self.syntaxHighlighting = None
        self.ui = None
        self.script_running = False
        openFolder, openTabs, currentTabIdx, consoleVisible, navVisible = self.readSettings()
        self.saveRequested = QShortcut(QKeySequence(QKeySequence.Save), self)
        self.saveAsRequested = QShortcut(QKeySequence(QKeySequence.SaveAs), self)
        self.setupWindow(openFolder, openTabs, currentTabIdx, consoleVisible, navVisible)
        self.logger_name = setup_guiLogger(self, log_level)
        self.logger = logging.getLogger(self.logger_name)
        # self.runner = ScriptRunner(self.logger_name)
        # self.show()

    def closeEvent(self, event: QCloseEvent) -> None:
        self.write_settings()
        event.accept()
        # return super().closeEvent(event)

    def setupWindow(self, openFolder, openTabs, currentTabIdx, consoleVisible, navVisible):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.newTab_btn = QToolButton()
        self.ui.newTab_btn.setObjectName(u"newTab_btn")
        self.ui.runCode_btn = QToolButton()
        self.ui.runCode_btn.setObjectName(u"runCode_btn")
        self.setTheme(self.theme)
        self.setupIcons()
        self.ui.delete_btn.hide()
        self.ui.reference_ind.hide()
        self.ui.settings_ind.hide()
        self.ui.nav_window.setCurrentIndex(0)
        registerCallbacks(self)

        self.setWindowTitle("MAX BLE HCI Editor")
        self.setWindowModality(Qt.NonModal)
        populate_referenceTree(self)
        setupContextMenus(self)
        setup_menubar(self, consoleVisible, navVisible)
        self.ui.console_win.setVisible(consoleVisible)
        self.ui.context_menu.setVisible(navVisible)

        if openFolder != '':
            self.ui.filetree.setRootDir(openFolder)

        if openTabs == {}:
            setup_tabs(self)
        else:
            setup_tabs(self, createStarter=False)
            for idx, (filePath, contents) in enumerate(openTabs.items()):
                if contents == '':
                    newTab = QCodeEditor(
                        theme=self.theme,
                        parent=self.ui.editor_win,
                        filePath=filePath,
                        useSyntaxHighlighting=self.syntaxHighlighting,
                        autoCompleteBrackets=self.autoCompleteBrackets
                    )
                    newTab.setFrameShape(QFrame.NoFrame)
                    readFile = QFile(filePath)
                    readFile.open(QIODevice.ReadOnly | QIODevice.ExistingOnly | QIODevice.Text)
                    readStr = QTextStream(readFile).readAll()
                    newTab.setPlainText(readStr)
                    self.ui.editor_win.insertTab(idx, newTab, QFileInfo(filePath).fileName())
                else:
                    newTab = QCodeEditor(
                        theme=self.theme,
                        parent=self.ui.editor_win,
                        useSyntaxHighlighting=self.syntaxHighlighting,
                        autoCompleteBrackets=self.autoCompleteBrackets
                    )
                    newTab.setFrameShape(QFrame.NoFrame)
                    newTab.setPlainText(contents)
                    self.ui.editor_win.insertTab(idx, newTab, filePath)
                    self.ui.editor_win.widget(idx).document().setModified(True)

        self.ui.editor_win.setCurrentIndex(currentTabIdx)
        self.ui.enable_syntaxHighlighting.setChecked(self.syntaxHighlighting)
        self.ui.enable_bracketAutoComplete.setChecked(self.autoCompleteBrackets)
        self.ui.enable_consoleWindow.setChecked(consoleVisible)
        self.ui.enable_navSidebar.setChecked(navVisible)
        self.ui.enable_notifyOnMove.setChecked(self.notifyOnMove)
        self.ui.enable_notifyOnDelete.setChecked(self.notifyOnDelete)
        self.ui.enable_notifyCloseWithoutSave.setChecked(self.notifyOnClose)
        self.ui.select_themeMode.setCurrentIndex(self.theme)
        

    def write_settings(self):
        settings = QSettings()
        settings.beginGroup("mainWindow")
        settings.setValue("geometry", self.saveGeometry())
        winState = self.windowState()
        if winState & Qt.WindowMinimized:
            settings.setValue("winState", "MINIMIZED")
        elif winState & Qt.WindowMaximized:
            settings.setValue("winState", "MAXIMIZED")
        elif winState & Qt.WindowFullScreen:
            settings.setValue("winState", "FULLSCREEN")
        else:
            settings.setValue("winState", "NOSTATE")
        settings.setValue("theme", self.theme)
        settings.setValue("notifyOnMove", self.notifyOnMove)
        settings.setValue("notifyOnDelete", self.notifyOnDelete)
        settings.setValue("notifyOnClose", self.notifyOnClose)
        settings.endGroup()
        settings.setValue("console/visible", self.ui.console_win.isVisible())
        settings.beginGroup("navPanel")
        settings.setValue("visible", self.ui.context_menu.isVisible())
        settings.setValue("openFolder", self.ui.filetree.rootDir)
        settings.endGroup()
        settings.beginGroup("editor")
        settings.setValue("syntaxHighlighting", self.syntaxHighlighting)
        settings.setValue("autoCompleteBrackets", self.autoCompleteBrackets)
        settings.setValue("currentTabIdx", self.ui.editor_win.currentIndex())
        settings.beginWriteArray("openTabs")
        for idx in range(self.ui.editor_win.count() - 1):
            tab = self.ui.editor_win.widget(idx)
            tabTitle = self.ui.editor_win.tabText(idx)
            settings.setArrayIndex(idx)
            if tab.filePath is None:
                if tab.toPlainText() == '':
                    settings.setValue('filePath', '')
                    settings.setValue('contents', '')
                else:
                    settings.setValue('filePath', tabTitle.replace('*', ''))
                    settings.setValue('contents', tab.toPlainText())
            else:
                settings.setValue('filePath', tab.filePath)
                settings.setValue('contents', '')
        settings.endArray()
        settings.endGroup()

    def readSettings(self):
        settings = QSettings()
        settings.beginGroup("mainWindow")
        geometry = settings.value("geometry", QByteArray())
        winState = settings.value("winState", "NOSTATE", str)
        theme = settings.value("theme", self.LIGHT, int)
        notifyOnMove = settings.value("notifyOnMove", True, bool)
        notifyOnDelete = settings.value("notifyOnDelete", True, bool)
        notifyOnClose = settings.value("notifyOnClose", True, bool)
        settings.endGroup()
        consoleVisible = settings.value("console/visible", True, bool)
        settings.beginGroup("navPanel")
        navVisible = settings.value("visible", True, bool)
        openFolder = settings.value("openFolder", '', str)
        settings.endGroup()
        settings.beginGroup("editor")
        syntaxHighlighting = settings.value("syntaxHighlighting", True, bool)
        autoCompleteBrackets = settings.value("autoCompleteBrackets", True, bool)
        currentTabIdx = settings.value("currentTabIdx", 0, int)
        size = settings.beginReadArray("openTabs")
        openTabs = {}
        for idx in range(size):
            settings.setArrayIndex(idx)
            filePath = settings.value("filePath", '', str)
            contents = settings.value("contents", '', str)
            if filePath == '':
                continue
            openTabs[filePath] = contents
        settings.endArray()
        settings.endGroup()

        if geometry.isEmpty():
            self.setGeometry(0, 0, 1528, 1039)
        else:
            self.restoreGeometry(geometry)

        if winState == 'MINIMIZED':
            self.setWindowState(Qt.WindowMinimized)
        elif winState == 'MAXIMIZED':
            self.setWindowState(Qt.WindowMaximized)
        elif winState == 'FULLSCREEN':
            self.setWindowState(Qt.WindowFullScreen)
        else:
            self.setWindowState(Qt.WindowNoState)
        self.theme = theme
        self.notifyOnMove = notifyOnMove
        self.notifyOnDelete = notifyOnDelete
        self.notifyOnClose = notifyOnClose
        self.syntaxHighlighting = syntaxHighlighting
        self.autoCompleteBrackets = autoCompleteBrackets

        return openFolder, openTabs, currentTabIdx, consoleVisible, navVisible

    def applyNewSettings(self, newSettings: Dict[str, Any]):
        if newSettings['theme'] != self.theme:
            self.setTheme(newSettings['theme'])
            self.setupIcons()
            self.recolorConsole()
            for idx in range(self.ui.editor_win.count() - 1):
                self.ui.editor_win.widget(idx).setTheme(newSettings['theme'])
                if self.ui.editor_win.widget(idx).saveNeeded:
                    self.ui.editor_win.setTabIcon(idx, Icons[newSettings['theme']].SaveNeeded)
            self.ui.actionLight.setChecked(newSettings['theme'] == self.LIGHT)
            self.ui.actionDark.setChecked(newSettings['theme'] == self.DARK)

        if newSettings['syntaxHighlighting'] != self.syntaxHighlighting:
            self.syntaxHighlighting = newSettings['syntaxHighlighting']
            for idx in range(self.ui.editor_win.count() - 1):
                self.ui.editor_win.widget(idx).setSyntaxHighlighting(self.syntaxHighlighting)

        if newSettings['autoCompleteBrackets'] != self.autoCompleteBrackets:
            self.autoCompleteBrackets = newSettings['autoCompleteBrackets']
            for idx in range(self.ui.editor_win.count() - 1):
                self.ui.editor_win.widget(idx).setAutoCompleteBrackets(self.autoCompleteBrackets)

        self.ui.console_win.setVisible(newSettings['showConsoleWindow'])
        self.ui.actionShow_console.setChecked(newSettings['showConsoleWindow'])

        self.ui.context_menu.setVisible(newSettings['showNavigationSidebar'])
        self.ui.actionShow_navbar.setChecked(newSettings['showNavigationSidebar'])

        self.notifyOnMove = newSettings['notifyOnMove']
        self.notifyOnDelete = newSettings['notifyOnDelete']
        self.notifyOnClose = newSettings['notifyOnClose']

    def recolorConsole(self):
        newColor = QTextCharFormat()
        newColor.setForeground(CustomFormatter.getThemeColor(self.theme))
        oldColor = CustomFormatter.getThemeColor(not self.theme)
        self.ui.console_out.moveCursor(QTextCursor.Start, QTextCursor.MoveAnchor)
        while not self.ui.console_out.textCursor().atEnd():
            self.ui.console_out.moveCursor(QTextCursor.StartOfLine, QTextCursor.MoveAnchor)
            self.ui.console_out.moveCursor(QTextCursor.EndOfLine, QTextCursor.KeepAnchor)
            if self.ui.console_out.currentCharFormat().foreground() == oldColor:
                self.ui.console_out.setCurrentCharFormat(newColor)
            self.ui.console_out.moveCursor(QTextCursor.Down, QTextCursor.MoveAnchor)

        self.ui.console_out.update()
        self.ui.console_out.viewport().update()
        

    def setTheme(self, mode):
        if mode == self.LIGHT:
            with open('assets/themes/light_theme.qss', 'r', encoding='utf-8') as ss_sheet:
                ss_str = ss_sheet.read()
        else:
            with open('assets/themes/dark_theme.qss', 'r', encoding='utf-8') as ss_sheet:
                ss_str = ss_sheet.read()

        self.theme = mode
        self.setStyleSheet(ss_str)
    
    def setupIcons(self):
        if self.theme == self.DARK:
            self.ui.explorer_btn.setIcon(Icons.Dark.Explorer)
            self.ui.reference_btn.setIcon(Icons.Dark.Reference)
            self.ui.settings_btn.setIcon(Icons.Dark.Settings)
            self.ui.delete_btn.setIcon(Icons.Dark.Delete)
            self.ui.adi_logo.setPixmap(Icons.Dark.Logo)
            self.ui.newTab_btn.setIcon(Icons.Dark.NewTab)
            self.ui.runCode_btn.setIcon(Icons.Dark.RunCode)

            btn_ss = '''
            QPushButton {background-color: transparent; border: none;}
            QPushButton:hover {
            color: rgb(255, 255, 255);
            background-color: #464E69;
            padding: 3px;
            }'''
            newTabBtn_ss = '''
            QToolButton {background-color: transparent; border: none; border-radius: 4px;}
            QToolButton:hover {background-color: rgb(52, 59, 72);}
            '''
            runCodeBtn_ss = '''
            QToolButton {background-color: transparent; border: none; border-radius: 4px;}
            QToolButton:hover {background-color: #464E69}
            '''

        else:
            self.ui.explorer_btn.setIcon(Icons.Light.Explorer)
            self.ui.reference_btn.setIcon(Icons.Light.Reference)
            self.ui.settings_btn.setIcon(Icons.Light.Settings)
            self.ui.delete_btn.setIcon(Icons.Light.Delete)
            self.ui.adi_logo.setPixmap(Icons.Light.Logo)
            self.ui.newTab_btn.setIcon(Icons.Light.NewTab)
            self.ui.runCode_btn.setIcon(Icons.Light.RunCode)

            btn_ss = '''
            QPushButton {background-color: transparent; border: none;}
            QPushButton:hover {
            color: rgb(255, 255, 255);
            background-color: #EBEBEF;
            padding: 3px;
            }'''
            newTabBtn_ss = '''
            QToolButton {background-color: transparent; border: none; border-radius: 4px;}
            QToolButton:hover {background-color: #EBEBEF;}
            '''
            runCodeBtn_ss = '''
            QToolButton {background-color: transparent; border: none; border-radius: 4px;}
            QToolButton:hover {background-color: #EBEBEF}
            '''

        self.ui.explorer_btn.setIconSize(QSize(40, 40))
        self.ui.explorer_btn.setText("")
        self.ui.reference_btn.setIconSize(QSize(40, 40))
        self.ui.reference_btn.setText("")
        self.ui.settings_btn.setIconSize(QSize(40, 40))
        self.ui.settings_btn.setText("")
        self.ui.delete_btn.setIconSize(QSize(25, 25))
        self.ui.delete_btn.setText("")

        self.ui.explorer_btn.setStyleSheet(btn_ss)
        self.ui.reference_btn.setStyleSheet(btn_ss)
        self.ui.settings_btn.setStyleSheet(btn_ss)
        self.ui.delete_btn.setStyleSheet(btn_ss)

        self.ui.adi_logo.setAlignment(Qt.AlignCenter)
        self.ui.adi_logo.setStyleSheet("QLabel {background-color: transparent;}")
        
        self.ui.newTab_btn.setIconSize(QSize(20, 20))
        self.ui.newTab_btn.setText("")
        self.ui.newTab_btn.setStyleSheet(newTabBtn_ss)

        self.ui.runCode_btn.setIconSize(QSize(20, 20))
        self.ui.runCode_btn.setText("")
        self.ui.runCode_btn.setStyleSheet(runCodeBtn_ss)

    def showSaveNeededDialog(self, fname: str = None):
        if self.notifyOnClose:
            dialog = AreYouSurePopUp(self, mode=self.theme, fname=fname)
            dialog.setView(AreYouSurePopUp.SAVE_NEEDED)
            res = dialog.exec()
            return res
        return AreYouSurePopUp.SAVENEEDED_NOSAVE
    
    def showConfirmMoveDialog(self, source_fname, target_name):
        if self.notifyOnMove:
            dialog = AreYouSurePopUp(self, mode=self.theme, fname=(source_fname, target_name))
            dialog.setView(AreYouSurePopUp.CONFIRM_MOVE)
            res = dialog.exec()
            return res
        return AreYouSurePopUp.CONFIRM_MOVE
    
    def showConfirmDeleteDialog(self, source_fname):
        if self.notifyOnDelete:
            dialog = AreYouSurePopUp(self, mode=self.theme, fname=source_fname)
            dialog.setView(AreYouSurePopUp.CONFIRM_DELETE)
            res = dialog.exec()
            return res
        return AreYouSurePopUp.CONFIRM_DELETE
    
    def runCode(self, codeTxt):
        self.runner = create_runner(codeTxt, self.logger_name)
        self.codeThread = QThread()
        self.runner.moveToThread(self.codeThread)
        self.codeThread.started.connect(self.runner.run)
        self.runner.finished.connect(self.codeThread.exit)
        self.codeThread.finished.connect(self.runner.deleteLater)
        self.codeThread.finished.connect(self.codeFinished)

        self.script_running = True
        if self.theme == self.LIGHT:
            self.ui.runCode_btn.setIcon(Icons.Light.StopCode)
        else:
            self.ui.runCode_btn.setIcon(Icons.Dark.StopCode)
        self.codeThread.start()


    def codeFinished(self):
        self.codeThread.deleteLater()
        self.script_running = False
        if self.theme == self.LIGHT:
            self.ui.runCode_btn.setIcon(Icons.Light.RunCode)
        else:
            self.ui.runCode_btn.setIcon(Icons.Dark.RunCode)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    QCoreApplication.setOrganizationName("AnalogDevices")
    QCoreApplication.setApplicationName("MAX-BLE-HCI-GUIx")
    window = MainWindow(logging.DEBUG)
    window.show()
    sys.exit(app.exec())