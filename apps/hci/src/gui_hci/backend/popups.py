from PySide6.QtWidgets import QMainWindow, QApplication, QTabBar, QToolButton, QWidget
from PySide6.QtGui import QIcon, QPixmap, QColor, QShowEvent, QResizeEvent
from PySide6.QtCore import QSize, QRect
from PySide6.QtCore import Qt, QObject, Signal, QThread, Slot, QEventLoop, QEvent, QPoint
from .areYouSure_popup import Ui_areYouSure_popup

class PopupSignals(QObject):
    closeAnyways = Signal()
    saveWork = Signal()
    cancelOperation = Signal()
    closeApp = Signal()

class AreYouSurePopUp(QWidget):
    LIGHT = 0
    DARK = 1

    SAVE_NEEDED = 0
    CONFIRM_MOVE = 1
    CONFIRM_DELETE = 2

    SAVENEEDED_NOSAVE = 0
    SAVENEEDED_SAVE = 1
    SAVENEEDED_CANCEL = 2

    CONFIRMDELETE_DELETE = 3
    CONFIRMDELETE_CANCEL = 4

    CONFIRMMOVE_MOVE = 5
    CONFIRMMOVE_CANCEL = 6
    def __init__(self, parent: QMainWindow, mode=LIGHT, fname=None):
        super().__init__()
        self.ui =  Ui_areYouSure_popup()
        self.ui.setupUi(self)
        self.fname = fname
        self.theme = None
        self.set_theme(mode)
        self.xOffset = (parent.width() - self.width()) // 2
        self.yOffset = (parent.height() - self.height()) // 2
        self.basePos = parent.pos()
        self.parentWin = parent

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_DeleteOnClose)
        parent.installEventFilter(self)
        self.loop = QEventLoop(self)

    def setView(self, viewType):
        if viewType == self.SAVE_NEEDED:
            self.ui.popupView.setCurrentIndex(self.SAVE_NEEDED)
            self.setup_saveNeededIcons()
            self.registerCallbacks(self.SAVE_NEEDED)
            return
        
        if viewType == self.CONFIRM_DELETE:
            self.ui.popupView.setCurrentIndex(self.CONFIRM_DELETE)
            self.setup_confirmDeleteIcons()
            self.registerCallbacks(self.CONFIRM_DELETE)
            return
        
        if viewType == self.CONFIRM_MOVE:
            self.ui.popupView.setCurrentIndex(self.CONFIRM_MOVE)
            self.setup_confirmMoveIcons()
            self.registerCallbacks(self.CONFIRM_MOVE)
            return
        
        raise ValueError(f"Invalid view selection: {viewType}")

    def setup_saveNeededIcons(self):
        if self.fname is not None:
            self.ui.saveNeeded_msg1.setText(f"Close {self.fname} without saving changes?")
        else:
            self.ui.saveNeeded_msg1.setText(f"Close window without saving?")

        if self.theme == self.DARK:
            warningIcon = QPixmap('assets/images/icons/warning-icon.png')
        elif self.theme == self.LIGHT:
            warningIcon = QPixmap('assets/images/icons/warning-icon-inv.png')

        warningIcon = warningIcon.scaledToHeight(60, Qt.SmoothTransformation)
        self.ui.saveNeeded_warningIcon.setPixmap(warningIcon)
        self.ui.saveNeeded_warningIcon.setAlignment(Qt.AlignCenter)
        self.ui.saveNeeded_warningIcon.setStyleSheet("QLabel {background-color: transparent;}")

    def setup_confirmDeleteIcons(self):
        self.ui.confirmDelete_msg1.setText(f"Delete {self.fname}?")

        if self.theme == self.DARK:
            warningIcon = QPixmap('assets/images/icons/warning-icon.png')
        elif self.theme == self.LIGHT:
            warningIcon = QPixmap('assets/images/icons/warning-icon-inv.png')

        warningIcon = warningIcon.scaledToHeight(60, Qt.SmoothTransformation)
        self.ui.confirmDelete_warningIcon.setPixmap(warningIcon)
        self.ui.confirmDelete_warningIcon.setAlignment(Qt.AlignCenter)
        self.ui.confirmDelete_warningIcon.setStyleSheet("QLabel {background-color: transparent;}")

    def setup_confirmMoveIcons(self):
        self.ui.confirmMove_msg1.setText(f"Move {self.fname[0]} into {self.fname[1]}?")

        if self.theme == self.DARK:
            warningIcon = QPixmap('assets/images/icons/warning-icon.png')
        elif self.theme == self.LIGHT:
            warningIcon = QPixmap('assets/images/icons/warning-icon-inv.png')

        warningIcon = warningIcon.scaledToHeight(60, Qt.SmoothTransformation)
        self.ui.confirmMove_warningIcon.setPixmap(warningIcon)
        self.ui.confirmMove_warningIcon.setAlignment(Qt.AlignCenter)
        self.ui.confirmMove_warningIcon.setStyleSheet("QLabel {background-color: transparent;}")

    def set_theme(self, mode):
        if mode == self.LIGHT:
            with open('assets/themes/light_theme.qss', 'r', encoding='utf-8') as ss_sheet:
                ss_str = ss_sheet.read()
        else:
            with open('assets/themes/light_theme.qss', 'r', encoding='utf-8') as ss_sheet:
                ss_str = ss_sheet.read()
        
        self.setStyleSheet(ss_str)
        self.theme = mode

    def registerCallbacks(self, popupType):
        if popupType == self.SAVE_NEEDED:
            self.ui.saveNeeded_noSave.clicked.connect(self.close_saveNeeded_noSave)
            self.ui.saveNeeded_save.clicked.connect(self.close_saveNeeded_save)
            self.ui.saveNeeded_cancel.clicked.connect(self.close_saveNeeded_cancel)
            return
        if popupType == self.CONFIRM_DELETE:
            self.ui.confirmDelete_delete.clicked.connect(self.close_confirmDelete_delete)
            self.ui.confirmDelete_cancel.clicked.connect(self.close_confirmDelete_cancel)
            return

        self.ui.confirmMove_move.clicked.connect(self.close_confirmMove_move)
        self.ui.confirmMove_cancel.clicked.connect(self.close_confirmMove_cancel)

    def close_saveNeeded_noSave(self):
        self.loop.exit(self.SAVENEEDED_NOSAVE)
    
    def close_saveNeeded_save(self):
        self.loop.exit(self.SAVENEEDED_SAVE)

    def close_saveNeeded_cancel(self):
        self.loop.exit(self.SAVENEEDED_CANCEL)

    def close_confirmDelete_cancel(self):
        self.loop.exit(self.CONFIRMDELETE_CANCEL)

    def close_confirmDelete_delete(self):
        self.loop.exit(self.CONFIRMDELETE_DELETE)

    def close_confirmMove_cancel(self):
        self.loop.exit(self.CONFIRMMOVE_CANCEL)
    
    def close_confirmMove_move(self):
        self.loop.exit(self.CONFIRMMOVE_MOVE)

    def showEvent(self, event: QShowEvent) -> None:
        self.setGeometry(
            QRect(
                self.basePos.x() + self.xOffset,
                self.basePos.y() + self.yOffset,
                self.width(),
                self.height()
            )
        )

    def eventFilter(self, watched: QObject, event: QEvent) -> bool:
        if event.type() == event.Move:
            self.basePos = event.pos()
            self.setGeometry(
                QRect(
                    self.basePos.x() + self.xOffset,
                    self.basePos.y() + self.yOffset,
                    self.width(), self.height()
                )
            )
        if event.type() == event.Resize:
            self.xOffset = (event.size().width() - self.width()) // 2
            self.yOffset = (event.size().height() - self.height()) // 2
            self.setGeometry(
                QRect(
                    self.basePos.x() + self.xOffset,
                    self.basePos.y() + self.yOffset,
                    self.width(),
                    self.height()
                )
            )

        return super().eventFilter(watched, event)
    
    def exec(self):
        self.show()
        self.raise_()
        res = self.loop.exec_()
        self.close()
        self.parentWin.removeEventFilter(self)
        return res