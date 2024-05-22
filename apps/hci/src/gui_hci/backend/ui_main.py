# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)
from PySide6.QtGui import (
    QAction,
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QFrame,
    QGridLayout,
    QHeaderView,
    QLabel,
    QMainWindow,
    QMenu,
    QMenuBar,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QSplitter,
    QStackedWidget,
    QStatusBar,
    QTabWidget,
    QTextEdit,
    QTreeView,
    QVBoxLayout,
    QWidget,
)
from .ref_window import QDeselectableTreeView
from .nav_window import QDirectoryTree


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1528, 1039)
        self.actionNew_file = QAction(MainWindow)
        self.actionNew_file.setObjectName("actionNew_file")
        self.actionOpen_File = QAction(MainWindow)
        self.actionOpen_File.setObjectName("actionOpen_File")
        self.actionOpen_Folder = QAction(MainWindow)
        self.actionOpen_Folder.setObjectName("actionOpen_Folder")
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_as = QAction(MainWindow)
        self.actionSave_as.setObjectName("actionSave_as")
        self.actionClose_folder = QAction(MainWindow)
        self.actionClose_folder.setObjectName("actionClose_folder")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionUndo = QAction(MainWindow)
        self.actionUndo.setObjectName("actionUndo")
        self.actionRedo = QAction(MainWindow)
        self.actionRedo.setObjectName("actionRedo")
        self.actionCut = QAction(MainWindow)
        self.actionCut.setObjectName("actionCut")
        self.actionCopy = QAction(MainWindow)
        self.actionCopy.setObjectName("actionCopy")
        self.actionPaste = QAction(MainWindow)
        self.actionPaste.setObjectName("actionPaste")
        self.actionDefault = QAction(MainWindow)
        self.actionDefault.setObjectName("actionDefault")
        self.actionDefault.setCheckable(True)
        self.actionRefView = QAction(MainWindow)
        self.actionRefView.setObjectName("actionRefView")
        self.actionRefView.setCheckable(True)
        self.actionMAX_BLE_HCI_Documentation = QAction(MainWindow)
        self.actionMAX_BLE_HCI_Documentation.setObjectName(
            "actionMAX_BLE_HCI_Documentation"
        )
        self.actionBLE_Core_Spec = QAction(MainWindow)
        self.actionBLE_Core_Spec.setObjectName("actionBLE_Core_Spec")
        self.actionHCI_GUI_Documentation = QAction(MainWindow)
        self.actionHCI_GUI_Documentation.setObjectName("actionHCI_GUI_Documentation")
        self.actionLight = QAction(MainWindow)
        self.actionLight.setObjectName("actionLight")
        self.actionLight.setCheckable(True)
        self.actionDark = QAction(MainWindow)
        self.actionDark.setObjectName("actionDark")
        self.actionDark.setCheckable(True)
        self.actionShow_console = QAction(MainWindow)
        self.actionShow_console.setObjectName("actionShow_console")
        self.actionShow_console.setCheckable(True)
        self.actionShow_navbar = QAction(MainWindow)
        self.actionShow_navbar.setObjectName("actionShow_navbar")
        self.actionShow_navbar.setCheckable(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_4 = QGridLayout(self.centralwidget)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName("line_2")
        self.line_2.setMinimumSize(QSize(1, 0))
        self.line_2.setMaximumSize(QSize(1, 16777215))
        self.line_2.setLineWidth(0)
        self.line_2.setMidLineWidth(1)
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout_4.addWidget(self.line_2, 0, 2, 1, 1)

        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName("splitter")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setOrientation(Qt.Vertical)
        self.editor_win = QTabWidget(self.splitter)
        self.editor_win.setObjectName("editor_win")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(1)
        sizePolicy1.setHeightForWidth(self.editor_win.sizePolicy().hasHeightForWidth())
        self.editor_win.setSizePolicy(sizePolicy1)
        self.editor_win.setTabShape(QTabWidget.Rounded)
        self.editor_win.setTabsClosable(True)
        self.editor_win.setMovable(True)
        self.quickadd_btn = QWidget()
        self.quickadd_btn.setObjectName("quickadd_btn")
        self.editor_win.addTab(self.quickadd_btn, "")
        self.splitter.addWidget(self.editor_win)
        self.console_win = QFrame(self.splitter)
        self.console_win.setObjectName("console_win")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.console_win.sizePolicy().hasHeightForWidth())
        self.console_win.setSizePolicy(sizePolicy2)
        self.console_win.setBaseSize(QSize(0, 0))
        self.console_win.setFrameShape(QFrame.NoFrame)
        self.console_win.setFrameShadow(QFrame.Raised)
        self.gridLayout_23 = QGridLayout(self.console_win)
        self.gridLayout_23.setObjectName("gridLayout_23")
        self.gridLayout_23.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_24 = QGridLayout()
        self.gridLayout_24.setObjectName("gridLayout_24")
        self.logfile_btn = QPushButton(self.console_win)
        self.logfile_btn.setObjectName("logfile_btn")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.logfile_btn.sizePolicy().hasHeightForWidth())
        self.logfile_btn.setSizePolicy(sizePolicy3)
        self.logfile_btn.setMinimumSize(QSize(115, 0))

        self.gridLayout_24.addWidget(self.logfile_btn, 0, 5, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(
            5, 20, QSizePolicy.Fixed, QSizePolicy.Minimum
        )

        self.gridLayout_24.addItem(self.horizontalSpacer_3, 0, 6, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(
            5, 20, QSizePolicy.Fixed, QSizePolicy.Minimum
        )

        self.gridLayout_24.addItem(self.horizontalSpacer_2, 0, 4, 1, 1)

        self.horizontalSpacer = QSpacerItem(
            5, 20, QSizePolicy.Fixed, QSizePolicy.Minimum
        )

        self.gridLayout_24.addItem(self.horizontalSpacer, 0, 0, 1, 1)

        self.console_out = QTextEdit(self.console_win)
        self.console_out.setObjectName("console_out")
        self.console_out.setFrameShape(QFrame.NoFrame)
        self.console_out.setReadOnly(False)

        self.gridLayout_24.addWidget(self.console_out, 1, 1, 1, 5)

        self.logfile_label = QLabel(self.console_win)
        self.logfile_label.setObjectName("logfile_label")

        self.gridLayout_24.addWidget(self.logfile_label, 0, 2, 1, 1)

        self.label_8 = QLabel(self.console_win)
        self.label_8.setObjectName("label_8")

        self.gridLayout_24.addWidget(self.label_8, 0, 1, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(
            20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed
        )

        self.gridLayout_24.addItem(self.verticalSpacer_4, 2, 1, 1, 1)

        self.delete_btn = QPushButton(self.console_win)
        self.delete_btn.setObjectName("delete_btn")
        sizePolicy3.setHeightForWidth(self.delete_btn.sizePolicy().hasHeightForWidth())
        self.delete_btn.setSizePolicy(sizePolicy3)
        self.delete_btn.setMinimumSize(QSize(25, 25))
        self.delete_btn.setMaximumSize(QSize(25, 25))

        self.gridLayout_24.addWidget(self.delete_btn, 0, 3, 1, 1)

        self.gridLayout_23.addLayout(self.gridLayout_24, 0, 0, 1, 1)

        self.splitter.addWidget(self.console_win)

        self.gridLayout_4.addWidget(self.splitter, 0, 3, 2, 1)

        self.context_menu = QFrame(self.centralwidget)
        self.context_menu.setObjectName("context_menu")
        sizePolicy4 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(
            self.context_menu.sizePolicy().hasHeightForWidth()
        )
        self.context_menu.setSizePolicy(sizePolicy4)
        self.context_menu.setFrameShape(QFrame.NoFrame)
        self.context_menu.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.context_menu)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.context_menu)
        self.widget.setObjectName("widget")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.nav_window = QStackedWidget(self.widget)
        self.nav_window.setObjectName("nav_window")
        sizePolicy4.setHeightForWidth(self.nav_window.sizePolicy().hasHeightForWidth())
        self.nav_window.setSizePolicy(sizePolicy4)
        self.nav_window.setMaximumSize(QSize(274, 16777215))
        self.explorer_win = QWidget()
        self.explorer_win.setObjectName("explorer_win")
        self.verticalLayout_2 = QVBoxLayout(self.explorer_win)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QLabel(self.explorer_win)
        self.label.setObjectName("label")

        self.verticalLayout_2.addWidget(self.label)

        self.filetree = QDirectoryTree(self.explorer_win)
        self.filetree.setObjectName("filetree")
        self.filetree.setFrameShape(QFrame.NoFrame)
        self.filetree.header().setDefaultSectionSize(57)

        self.verticalLayout_2.addWidget(self.filetree)

        self.nav_window.addWidget(self.explorer_win)
        self.reference_win = QWidget()
        self.reference_win.setObjectName("reference_win")
        self.verticalLayout_3 = QVBoxLayout(self.reference_win)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QLabel(self.reference_win)
        self.label_2.setObjectName("label_2")

        self.verticalLayout_3.addWidget(self.label_2)

        self.reftree = QDeselectableTreeView(self.reference_win)
        self.reftree.setObjectName("reftree")
        self.reftree.setFrameShape(QFrame.NoFrame)
        self.reftree.header().setDefaultSectionSize(57)

        self.verticalLayout_3.addWidget(self.reftree)

        self.nav_window.addWidget(self.reference_win)
        self.settings_win = QWidget()
        self.settings_win.setObjectName("settings_win")
        self.verticalLayout_4 = QVBoxLayout(self.settings_win)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_3 = QLabel(self.settings_win)
        self.label_3.setObjectName("label_3")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy5)

        self.verticalLayout_4.addWidget(self.label_3)

        self.settingstree = QFrame(self.settings_win)
        self.settingstree.setObjectName("settingstree")
        self.settingstree.setFrameShape(QFrame.NoFrame)
        self.settingstree.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.settingstree)
        self.gridLayout.setObjectName("gridLayout")
        self.label_14 = QLabel(self.settingstree)
        self.label_14.setObjectName("label_14")
        sizePolicy6 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy6)
        self.label_14.setMinimumSize(QSize(133, 0))
        self.label_14.setMaximumSize(QSize(133, 16777215))
        self.label_14.setWordWrap(True)

        self.gridLayout.addWidget(self.label_14, 13, 0, 1, 1)

        self.applySettings_btn = QPushButton(self.settingstree)
        self.applySettings_btn.setObjectName("applySettings_btn")

        self.gridLayout.addWidget(self.applySettings_btn, 17, 1, 1, 1)

        self.label_13 = QLabel(self.settingstree)
        self.label_13.setObjectName("label_13")

        self.gridLayout.addWidget(self.label_13, 11, 0, 1, 2)

        self.verticalSpacer_6 = QSpacerItem(
            20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed
        )

        self.gridLayout.addItem(self.verticalSpacer_6, 5, 0, 1, 2)

        self.enable_bracketAutoComplete = QCheckBox(self.settingstree)
        self.enable_bracketAutoComplete.setObjectName("enable_bracketAutoComplete")
        self.enable_bracketAutoComplete.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout.addWidget(self.enable_bracketAutoComplete, 3, 1, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(
            20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed
        )

        self.gridLayout.addItem(self.verticalSpacer_5, 10, 0, 1, 2)

        self.line_3 = QFrame(self.settingstree)
        self.line_3.setObjectName("line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_3, 1, 0, 1, 2)

        self.line_5 = QFrame(self.settingstree)
        self.line_5.setObjectName("line_5")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_5, 12, 0, 1, 2)

        self.enable_notifyCloseWithoutSave = QCheckBox(self.settingstree)
        self.enable_notifyCloseWithoutSave.setObjectName(
            "enable_notifyCloseWithoutSave"
        )
        self.enable_notifyCloseWithoutSave.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout.addWidget(self.enable_notifyCloseWithoutSave, 15, 1, 1, 1)

        self.label_16 = QLabel(self.settingstree)
        self.label_16.setObjectName("label_16")
        sizePolicy6.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy6)
        self.label_16.setMinimumSize(QSize(133, 0))
        self.label_16.setMaximumSize(QSize(133, 16777215))
        self.label_16.setWordWrap(True)

        self.gridLayout.addWidget(self.label_16, 15, 0, 1, 1)

        self.label_7 = QLabel(self.settingstree)
        self.label_7.setObjectName("label_7")
        sizePolicy4.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy4)
        self.label_7.setMinimumSize(QSize(0, 0))
        self.label_7.setMaximumSize(QSize(133, 16777215))
        self.label_7.setWordWrap(True)

        self.gridLayout.addWidget(self.label_7, 4, 0, 1, 1)

        self.verticalSpacer_8 = QSpacerItem(
            20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed
        )

        self.gridLayout.addItem(self.verticalSpacer_8, 16, 0, 1, 2)

        self.enable_consoleWindow = QCheckBox(self.settingstree)
        self.enable_consoleWindow.setObjectName("enable_consoleWindow")
        self.enable_consoleWindow.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout.addWidget(self.enable_consoleWindow, 8, 1, 1, 1)

        self.label_4 = QLabel(self.settingstree)
        self.label_4.setObjectName("label_4")

        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 2)

        self.enable_syntaxHighlighting = QCheckBox(self.settingstree)
        self.enable_syntaxHighlighting.setObjectName("enable_syntaxHighlighting")
        self.enable_syntaxHighlighting.setLayoutDirection(Qt.RightToLeft)
        self.enable_syntaxHighlighting.setChecked(False)

        self.gridLayout.addWidget(self.enable_syntaxHighlighting, 2, 1, 1, 1)

        self.label_10 = QLabel(self.settingstree)
        self.label_10.setObjectName("label_10")
        sizePolicy6.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy6)
        self.label_10.setMinimumSize(QSize(133, 0))
        self.label_10.setMaximumSize(QSize(133, 16777215))
        self.label_10.setWordWrap(True)

        self.gridLayout.addWidget(self.label_10, 8, 0, 1, 1)

        self.label_9 = QLabel(self.settingstree)
        self.label_9.setObjectName("label_9")

        self.gridLayout.addWidget(self.label_9, 6, 0, 1, 2)

        self.enable_notifyOnDelete = QCheckBox(self.settingstree)
        self.enable_notifyOnDelete.setObjectName("enable_notifyOnDelete")
        self.enable_notifyOnDelete.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout.addWidget(self.enable_notifyOnDelete, 14, 1, 1, 1)

        self.label_6 = QLabel(self.settingstree)
        self.label_6.setObjectName("label_6")
        sizePolicy6.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy6)
        self.label_6.setMinimumSize(QSize(133, 0))
        self.label_6.setMaximumSize(QSize(133, 16777215))
        self.label_6.setWordWrap(True)

        self.gridLayout.addWidget(self.label_6, 3, 0, 1, 1)

        self.label_5 = QLabel(self.settingstree)
        self.label_5.setObjectName("label_5")
        sizePolicy6.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy6)
        self.label_5.setMinimumSize(QSize(133, 0))
        self.label_5.setMaximumSize(QSize(133, 16777215))
        self.label_5.setWordWrap(True)

        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)

        self.label_15 = QLabel(self.settingstree)
        self.label_15.setObjectName("label_15")
        sizePolicy6.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy6)
        self.label_15.setMinimumSize(QSize(133, 0))
        self.label_15.setMaximumSize(QSize(133, 16777215))
        self.label_15.setWordWrap(True)

        self.gridLayout.addWidget(self.label_15, 14, 0, 1, 1)

        self.label_11 = QLabel(self.settingstree)
        self.label_11.setObjectName("label_11")
        sizePolicy6.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy6)
        self.label_11.setMinimumSize(QSize(133, 0))
        self.label_11.setMaximumSize(QSize(133, 16777215))
        self.label_11.setWordWrap(True)

        self.gridLayout.addWidget(self.label_11, 9, 0, 1, 1)

        self.select_themeMode = QComboBox(self.settingstree)
        self.select_themeMode.addItem("")
        self.select_themeMode.addItem("")
        self.select_themeMode.setObjectName("select_themeMode")
        self.select_themeMode.setFrame(True)

        self.gridLayout.addWidget(self.select_themeMode, 4, 1, 1, 1)

        self.enable_notifyOnMove = QCheckBox(self.settingstree)
        self.enable_notifyOnMove.setObjectName("enable_notifyOnMove")
        self.enable_notifyOnMove.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout.addWidget(self.enable_notifyOnMove, 13, 1, 1, 1)

        self.enable_navSidebar = QCheckBox(self.settingstree)
        self.enable_navSidebar.setObjectName("enable_navSidebar")
        self.enable_navSidebar.setLayoutDirection(Qt.RightToLeft)

        self.gridLayout.addWidget(self.enable_navSidebar, 9, 1, 1, 1)

        self.line_4 = QFrame(self.settingstree)
        self.line_4.setObjectName("line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_4, 7, 0, 1, 2)

        self.verticalSpacer_7 = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.gridLayout.addItem(self.verticalSpacer_7, 18, 0, 1, 2)

        self.verticalLayout_4.addWidget(self.settingstree)

        self.nav_window.addWidget(self.settings_win)

        self.verticalLayout.addWidget(self.nav_window)

        self.adi_logo = QLabel(self.widget)
        self.adi_logo.setObjectName("adi_logo")
        sizePolicy7 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.adi_logo.sizePolicy().hasHeightForWidth())
        self.adi_logo.setSizePolicy(sizePolicy7)

        self.verticalLayout.addWidget(self.adi_logo)

        self.gridLayout_3.addWidget(self.widget, 0, 2, 1, 1)

        self.nav_bar = QFrame(self.context_menu)
        self.nav_bar.setObjectName("nav_bar")
        sizePolicy6.setHeightForWidth(self.nav_bar.sizePolicy().hasHeightForWidth())
        self.nav_bar.setSizePolicy(sizePolicy6)
        self.nav_bar.setMinimumSize(QSize(60, 0))
        self.nav_bar.setMaximumSize(QSize(60, 16777215))
        self.nav_bar.setFrameShape(QFrame.NoFrame)
        self.nav_bar.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.nav_bar)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalSpacer_3 = QSpacerItem(
            20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed
        )

        self.gridLayout_2.addItem(self.verticalSpacer_3, 1, 1, 1, 1)

        self.reference_btn = QPushButton(self.nav_bar)
        self.reference_btn.setObjectName("reference_btn")
        sizePolicy3.setHeightForWidth(
            self.reference_btn.sizePolicy().hasHeightForWidth()
        )
        self.reference_btn.setSizePolicy(sizePolicy3)
        self.reference_btn.setMinimumSize(QSize(40, 40))
        self.reference_btn.setMaximumSize(QSize(40, 40))

        self.gridLayout_2.addWidget(self.reference_btn, 2, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(
            20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed
        )

        self.gridLayout_2.addItem(self.verticalSpacer_2, 3, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.gridLayout_2.addItem(self.verticalSpacer, 5, 1, 1, 1)

        self.explorer_btn = QPushButton(self.nav_bar)
        self.explorer_btn.setObjectName("explorer_btn")
        sizePolicy3.setHeightForWidth(
            self.explorer_btn.sizePolicy().hasHeightForWidth()
        )
        self.explorer_btn.setSizePolicy(sizePolicy3)
        self.explorer_btn.setMinimumSize(QSize(40, 40))
        self.explorer_btn.setMaximumSize(QSize(40, 40))

        self.gridLayout_2.addWidget(self.explorer_btn, 0, 1, 1, 1)

        self.settings_btn = QPushButton(self.nav_bar)
        self.settings_btn.setObjectName("settings_btn")
        sizePolicy3.setHeightForWidth(
            self.settings_btn.sizePolicy().hasHeightForWidth()
        )
        self.settings_btn.setSizePolicy(sizePolicy3)
        self.settings_btn.setMinimumSize(QSize(40, 40))
        self.settings_btn.setMaximumSize(QSize(40, 40))

        self.gridLayout_2.addWidget(self.settings_btn, 4, 1, 1, 1)

        self.explorer_ind = QFrame(self.nav_bar)
        self.explorer_ind.setObjectName("explorer_ind")
        self.explorer_ind.setFrameShape(QFrame.VLine)
        self.explorer_ind.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.explorer_ind, 0, 0, 1, 1)

        self.reference_ind = QFrame(self.nav_bar)
        self.reference_ind.setObjectName("reference_ind")
        self.reference_ind.setFrameShape(QFrame.VLine)
        self.reference_ind.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.reference_ind, 2, 0, 1, 1)

        self.settings_ind = QFrame(self.nav_bar)
        self.settings_ind.setObjectName("settings_ind")
        self.settings_ind.setFrameShape(QFrame.VLine)
        self.settings_ind.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.settings_ind, 4, 0, 1, 1)

        self.gridLayout_3.addWidget(self.nav_bar, 0, 0, 1, 1)

        self.line = QFrame(self.context_menu)
        self.line.setObjectName("line")
        self.line.setMinimumSize(QSize(1, 0))
        self.line.setMaximumSize(QSize(1, 16777215))
        self.line.setLineWidth(0)
        self.line.setMidLineWidth(1)
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout_3.addWidget(self.line, 0, 1, 1, 1)

        self.gridLayout_4.addWidget(self.context_menu, 0, 0, 1, 2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(QRect(0, 0, 1528, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuView = QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuColor_palatte = QMenu(self.menuView)
        self.menuColor_palatte.setObjectName("menuColor_palatte")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionNew_file)
        self.menuFile.addAction(self.actionOpen_File)
        self.menuFile.addAction(self.actionOpen_Folder)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_as)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionClose_folder)
        self.menuFile.addAction(self.actionExit)
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionRedo)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionCut)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        self.menuView.addAction(self.menuColor_palatte.menuAction())
        self.menuView.addAction(self.actionShow_console)
        self.menuView.addAction(self.actionShow_navbar)
        self.menuColor_palatte.addAction(self.actionLight)
        self.menuColor_palatte.addAction(self.actionDark)
        self.menuHelp.addAction(self.actionHCI_GUI_Documentation)
        self.menuHelp.addAction(self.actionMAX_BLE_HCI_Documentation)
        self.menuHelp.addAction(self.actionBLE_Core_Spec)

        self.retranslateUi(MainWindow)

        self.editor_win.setCurrentIndex(0)
        self.nav_window.setCurrentIndex(2)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "MainWindow", None)
        )
        self.actionNew_file.setText(
            QCoreApplication.translate("MainWindow", "New file", None)
        )
        self.actionOpen_File.setText(
            QCoreApplication.translate("MainWindow", "Open File", None)
        )
        self.actionOpen_Folder.setText(
            QCoreApplication.translate("MainWindow", "Open Folder", None)
        )
        self.actionSave.setText(QCoreApplication.translate("MainWindow", "Save", None))
        self.actionSave_as.setText(
            QCoreApplication.translate("MainWindow", "Save as", None)
        )
        self.actionClose_folder.setText(
            QCoreApplication.translate("MainWindow", "Close folder", None)
        )
        self.actionExit.setText(QCoreApplication.translate("MainWindow", "Exit", None))
        self.actionUndo.setText(QCoreApplication.translate("MainWindow", "Undo", None))
        self.actionRedo.setText(QCoreApplication.translate("MainWindow", "Redo", None))
        self.actionCut.setText(QCoreApplication.translate("MainWindow", "Cut", None))
        self.actionCopy.setText(QCoreApplication.translate("MainWindow", "Copy", None))
        self.actionPaste.setText(
            QCoreApplication.translate("MainWindow", "Paste", None)
        )
        self.actionDefault.setText(
            QCoreApplication.translate("MainWindow", "Sidebar (Default)", None)
        )
        self.actionRefView.setText(
            QCoreApplication.translate("MainWindow", "Always Show Reference", None)
        )
        self.actionMAX_BLE_HCI_Documentation.setText(
            QCoreApplication.translate("MainWindow", "MAX BLE HCI Documentation", None)
        )
        self.actionBLE_Core_Spec.setText(
            QCoreApplication.translate("MainWindow", "BLE Core Spec", None)
        )
        self.actionHCI_GUI_Documentation.setText(
            QCoreApplication.translate("MainWindow", "HCI GUI Documentation", None)
        )
        self.actionLight.setText(
            QCoreApplication.translate("MainWindow", "Light", None)
        )
        self.actionDark.setText(QCoreApplication.translate("MainWindow", "Dark", None))
        self.actionShow_console.setText(
            QCoreApplication.translate("MainWindow", "Show console", None)
        )
        self.actionShow_navbar.setText(
            QCoreApplication.translate("MainWindow", "Show navigation bar", None)
        )
        self.editor_win.setTabText(self.editor_win.indexOf(self.quickadd_btn), "")
        self.logfile_btn.setText(
            QCoreApplication.translate("MainWindow", "Add log file", None)
        )
        self.logfile_label.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", "Console", None))
        self.delete_btn.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", "Explorer", None))
        self.label_2.setText(
            QCoreApplication.translate("MainWindow", "HCI Reference", None)
        )
        self.label_3.setText(QCoreApplication.translate("MainWindow", "Settings", None))
        self.label_14.setText(
            QCoreApplication.translate("MainWindow", "Confirm File/Folder Move", None)
        )
        self.applySettings_btn.setText(
            QCoreApplication.translate("MainWindow", "Apply Settings", None)
        )
        self.label_13.setText(
            QCoreApplication.translate("MainWindow", "Notifications", None)
        )
        self.enable_bracketAutoComplete.setText("")
        self.enable_notifyCloseWithoutSave.setText("")
        self.label_16.setText(
            QCoreApplication.translate("MainWindow", "Confirm Close Without Save", None)
        )
        self.label_7.setText(QCoreApplication.translate("MainWindow", "Theme", None))
        self.enable_consoleWindow.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", "Editor", None))
        self.enable_syntaxHighlighting.setText("")
        self.label_10.setText(
            QCoreApplication.translate("MainWindow", "Show Console Window", None)
        )
        self.label_9.setText(
            QCoreApplication.translate("MainWindow", "View/Layout", None)
        )
        self.enable_notifyOnDelete.setText("")
        self.label_6.setText(
            QCoreApplication.translate("MainWindow", "Auto-Complete Brackets", None)
        )
        self.label_5.setText(
            QCoreApplication.translate("MainWindow", "Syntax Highlighting", None)
        )
        self.label_15.setText(
            QCoreApplication.translate("MainWindow", "Confirm File/Folder Delete", None)
        )
        self.label_11.setText(
            QCoreApplication.translate("MainWindow", "Show Navigation Sidebar", None)
        )
        self.select_themeMode.setItemText(
            0, QCoreApplication.translate("MainWindow", "Light", None)
        )
        self.select_themeMode.setItemText(
            1, QCoreApplication.translate("MainWindow", "Dark", None)
        )

        self.enable_notifyOnMove.setText("")
        self.enable_navSidebar.setText("")
        self.adi_logo.setText(
            QCoreApplication.translate("MainWindow", "TextLabel", None)
        )
        self.reference_btn.setText(
            QCoreApplication.translate("MainWindow", "PushButton", None)
        )
        self.explorer_btn.setText(
            QCoreApplication.translate("MainWindow", "PushButton", None)
        )
        self.settings_btn.setText(
            QCoreApplication.translate("MainWindow", "PushButton", None)
        )
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", "File", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", "Edit", None))
        self.menuView.setTitle(QCoreApplication.translate("MainWindow", "View", None))
        self.menuColor_palatte.setTitle(
            QCoreApplication.translate("MainWindow", "Color palatte", None)
        )
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", "Help", None))

    # retranslateUi
