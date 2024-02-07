import logging
import sys
from PySide6.QtWidgets import QMainWindow, QApplication, QTabBar, QToolButton
from PySide6.QtGui import QIcon, QPixmap, QColor
from PySide6.QtCore import QSize
from PySide6.QtCore import Qt, QObject, Signal, QThread, Slot

from backend import *

class MainWindow(QMainWindow):
    LIGHT = 0
    DARK = 1
    def __init__(self, log_level, mode=LIGHT):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.logger_name = setup_guiLogger(self, log_level)
        self.logger = logging.getLogger(self.logger_name)

        self.setWindowTitle('MAX BLE HCI Editor')
        self.ui.nav_window.setCurrentIndex(0)
        register_callbacks(self)
        # setup_context_menus() TODO: check if needed

        self.theme = None
        self.script_running = False
        self.set_theme(mode)
        self.setup_icons()
        self.show()

    def set_theme(self, mode):
        if mode == self.LIGHT:
            with open('assets/themes/light_theme.qss', 'r', encoding='utf-8') as ss_sheet:
                ss_str = ss_sheet.read()
        else:
            with open('assets/themes/dark_theme.qss', 'r', encoding='utf-8') as ss_sheet:
                ss_str = ss_sheet.read()

        self.setStyleSheet(ss_str)
        self.theme = mode
    
    def setup_icons(self):
        explorer_icon = QIcon()
        reference_icon = QIcon()
        settings_icon = QIcon()
        delete_icon = QIcon()
        newTab_icon = QIcon()

        if self.theme == self.DARK:
            explorer_icon.addPixmap('assets/images/icons/cil-folder.png')
            reference_icon.addPixmap('assets/images/icons/cil-library.png')
            settings_icon.addPixmap('assets/images/icons/cil-settings.png')
            delete_icon.addPixmap('assets/images/icons/cil-x.png')
            logo_icon = QPixmap(
                'assets/images/analog-inv.png').scaledToHeight(100, Qt.SmoothTransformation)
            newTab_icon.addPixmap('assets/images/icons/cil-plus.png')

            btn_ss = '''
            QPushButton {background-color: transparent; border: none;}
            QPushButton:hover {
            color: rgb(255, 255, 255);
            background-color: #464E69;
            padding: 3px;
            }'''

        else:
            explorer_icon.addPixmap('assets/images/icons/cil-folder-inv.png')
            reference_icon.addPixmap('assets/images/icons/cil-library-inv.png')
            settings_icon.addPixmap('assets/images/icons/cil-settings-inv.png')
            delete_icon.addPixmap('assets/images/icons/cil-x-inv.png')
            logo_icon = QPixmap(
                'assets/images/analog.png').scaledToHeight(100, Qt.SmoothTransformation)
            newTab_icon.addPixmap('assets/images/icons/cil-plus-inv.png')

            btn_ss = '''
            QPushButton {background-color: transparent; border: none;}
            QPushButton:hover {
            color: rgb(255, 255, 255);
            background-color: #EBEBEF;
            padding: 3px;
            }'''

        self.ui.explorer_btn.setIcon(explorer_icon)
        self.ui.explorer_btn.setIconSize(QSize(40, 40))
        self.ui.explorer_btn.setText("")
        self.ui.reference_btn.setIcon(reference_icon)
        self.ui.reference_btn.setIconSize(QSize(40, 40))
        self.ui.reference_btn.setText("")
        self.ui.settings_btn.setIcon(settings_icon)
        self.ui.settings_btn.setIconSize(QSize(40, 40))
        self.ui.settings_btn.setText("")
        self.ui.delete_btn.setIcon(delete_icon)
        self.ui.delete_btn.setIconSize(QSize(25, 25))
        self.ui.delete_btn.setText("")

        self.ui.explorer_btn.setStyleSheet(btn_ss)
        self.ui.reference_btn.setStyleSheet(btn_ss)
        self.ui.settings_btn.setStyleSheet(btn_ss)
        self.ui.delete_btn.setStyleSheet(btn_ss)

        self.ui.adi_logo.setPixmap(logo_icon)
        self.ui.adi_logo.setAlignment(Qt.AlignCenter)
        self.ui.adi_logo.setStyleSheet("QLabel {background-color: transparent;}")

        self.ui.newTab_btn = QToolButton()
        self.ui.newTab_btn.setObjectName(u"newTab_btn")
        self.ui.newTab_btn.setIcon(newTab_icon)
        self.ui.newTab_btn.setIconSize(QSize(25, 25))
        self.ui.newTab_btn.setText("")
        self.ui.newTab_btn.setStyleSheet(
            "QToolButton {background-color: transparent; border: none;}")
        self.ui.editor_win.tabBar().setTabButton(1, QTabBar.RightSide, self.ui.newTab_btn)

        self.ui.delete_btn.hide()
        self.ui.reference_ind.hide()
        self.ui.settings_ind.hide()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow(logging.DEBUG, mode=MainWindow.DARK)
    sys.exit(app.exec())