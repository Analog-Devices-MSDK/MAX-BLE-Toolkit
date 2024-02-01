# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QSplitter, QStackedWidget, QStatusBar, QTabWidget,
    QTextEdit, QTreeWidget, QTreeWidgetItem, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1528, 1039)
        self.actionNew_file = QAction(MainWindow)
        self.actionNew_file.setObjectName(u"actionNew_file")
        self.actionOpen_File = QAction(MainWindow)
        self.actionOpen_File.setObjectName(u"actionOpen_File")
        self.actionOpen_Folder = QAction(MainWindow)
        self.actionOpen_Folder.setObjectName(u"actionOpen_Folder")
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        self.actionSave_as = QAction(MainWindow)
        self.actionSave_as.setObjectName(u"actionSave_as")
        self.actionClose_folder = QAction(MainWindow)
        self.actionClose_folder.setObjectName(u"actionClose_folder")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionUndo = QAction(MainWindow)
        self.actionUndo.setObjectName(u"actionUndo")
        self.actionRedo = QAction(MainWindow)
        self.actionRedo.setObjectName(u"actionRedo")
        self.actionCut = QAction(MainWindow)
        self.actionCut.setObjectName(u"actionCut")
        self.actionCopy = QAction(MainWindow)
        self.actionCopy.setObjectName(u"actionCopy")
        self.actionPaste = QAction(MainWindow)
        self.actionPaste.setObjectName(u"actionPaste")
        self.actionLight = QAction(MainWindow)
        self.actionLight.setObjectName(u"actionLight")
        self.actionDark = QAction(MainWindow)
        self.actionDark.setObjectName(u"actionDark")
        self.actionShow_Reference_2 = QAction(MainWindow)
        self.actionShow_Reference_2.setObjectName(u"actionShow_Reference_2")
        self.actionShow_console = QAction(MainWindow)
        self.actionShow_console.setObjectName(u"actionShow_console")
        self.actionDefault = QAction(MainWindow)
        self.actionDefault.setObjectName(u"actionDefault")
        self.actionAdd_custom = QAction(MainWindow)
        self.actionAdd_custom.setObjectName(u"actionAdd_custom")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_4 = QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Vertical)
        self.editor_win = QTabWidget(self.splitter)
        self.editor_win.setObjectName(u"editor_win")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.editor_win.sizePolicy().hasHeightForWidth())
        self.editor_win.setSizePolicy(sizePolicy)
        self.editor_win.setTabsClosable(True)
        self.editor_win.setMovable(True)
        self.doc_tab = QWidget()
        self.doc_tab.setObjectName(u"doc_tab")
        self.gridLayout_15 = QGridLayout(self.doc_tab)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.gridLayout_16 = QGridLayout()
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.textEdit = QTextEdit(self.doc_tab)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setFrameShape(QFrame.NoFrame)

        self.gridLayout_16.addWidget(self.textEdit, 0, 0, 1, 1)


        self.gridLayout_15.addLayout(self.gridLayout_16, 0, 0, 1, 1)

        self.editor_win.addTab(self.doc_tab, "")
        self.quickadd_btn = QWidget()
        self.quickadd_btn.setObjectName(u"quickadd_btn")
        self.editor_win.addTab(self.quickadd_btn, "")
        self.splitter.addWidget(self.editor_win)
        self.console_win = QFrame(self.splitter)
        self.console_win.setObjectName(u"console_win")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.console_win.sizePolicy().hasHeightForWidth())
        self.console_win.setSizePolicy(sizePolicy1)
        self.console_win.setBaseSize(QSize(0, 0))
        self.console_win.setFrameShape(QFrame.NoFrame)
        self.console_win.setFrameShadow(QFrame.Raised)
        self.gridLayout_23 = QGridLayout(self.console_win)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.gridLayout_24 = QGridLayout()
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.logfile_btn_4 = QPushButton(self.console_win)
        self.logfile_btn_4.setObjectName(u"logfile_btn_4")

        self.gridLayout_24.addWidget(self.logfile_btn_4, 0, 3, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_24.addItem(self.horizontalSpacer_5, 0, 1, 1, 1)

        self.label_8 = QLabel(self.console_win)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_24.addWidget(self.label_8, 0, 0, 1, 1)

        self.logfile_label_4 = QLabel(self.console_win)
        self.logfile_label_4.setObjectName(u"logfile_label_4")

        self.gridLayout_24.addWidget(self.logfile_label_4, 0, 2, 1, 1)

        self.console_out_4 = QTextEdit(self.console_win)
        self.console_out_4.setObjectName(u"console_out_4")
        self.console_out_4.setFrameShape(QFrame.NoFrame)
        self.console_out_4.setReadOnly(True)

        self.gridLayout_24.addWidget(self.console_out_4, 1, 0, 1, 4)


        self.gridLayout_23.addLayout(self.gridLayout_24, 0, 0, 1, 1)

        self.splitter.addWidget(self.console_win)

        self.gridLayout_4.addWidget(self.splitter, 0, 2, 1, 1)

        self.context_menu = QFrame(self.centralwidget)
        self.context_menu.setObjectName(u"context_menu")
        sizePolicy2 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.context_menu.sizePolicy().hasHeightForWidth())
        self.context_menu.setSizePolicy(sizePolicy2)
        self.context_menu.setFrameShape(QFrame.NoFrame)
        self.context_menu.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.context_menu)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.nav_bar = QFrame(self.context_menu)
        self.nav_bar.setObjectName(u"nav_bar")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.nav_bar.sizePolicy().hasHeightForWidth())
        self.nav_bar.setSizePolicy(sizePolicy3)
        self.nav_bar.setMinimumSize(QSize(60, 0))
        self.nav_bar.setMaximumSize(QSize(60, 16777215))
        self.nav_bar.setFrameShape(QFrame.NoFrame)
        self.nav_bar.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.nav_bar)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.settings_btn = QPushButton(self.nav_bar)
        self.settings_btn.setObjectName(u"settings_btn")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.settings_btn.sizePolicy().hasHeightForWidth())
        self.settings_btn.setSizePolicy(sizePolicy4)
        self.settings_btn.setMinimumSize(QSize(40, 40))
        self.settings_btn.setMaximumSize(QSize(40, 40))

        self.gridLayout_2.addWidget(self.settings_btn, 4, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 3, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 5, 0, 1, 1)

        self.reference_btn = QPushButton(self.nav_bar)
        self.reference_btn.setObjectName(u"reference_btn")
        sizePolicy4.setHeightForWidth(self.reference_btn.sizePolicy().hasHeightForWidth())
        self.reference_btn.setSizePolicy(sizePolicy4)
        self.reference_btn.setMinimumSize(QSize(40, 40))
        self.reference_btn.setMaximumSize(QSize(40, 40))

        self.gridLayout_2.addWidget(self.reference_btn, 2, 0, 1, 1)

        self.explorer_btn = QPushButton(self.nav_bar)
        self.explorer_btn.setObjectName(u"explorer_btn")
        sizePolicy4.setHeightForWidth(self.explorer_btn.sizePolicy().hasHeightForWidth())
        self.explorer_btn.setSizePolicy(sizePolicy4)
        self.explorer_btn.setMinimumSize(QSize(40, 40))
        self.explorer_btn.setMaximumSize(QSize(40, 40))

        self.gridLayout_2.addWidget(self.explorer_btn, 0, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 5, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_2.addItem(self.verticalSpacer_3, 1, 0, 1, 1)


        self.gridLayout_3.addWidget(self.nav_bar, 0, 0, 1, 1)

        self.line = QFrame(self.context_menu)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout_3.addWidget(self.line, 0, 1, 1, 1)

        self.nav_window = QStackedWidget(self.context_menu)
        self.nav_window.setObjectName(u"nav_window")
        sizePolicy5 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.nav_window.sizePolicy().hasHeightForWidth())
        self.nav_window.setSizePolicy(sizePolicy5)
        self.explorer_win = QWidget()
        self.explorer_win.setObjectName(u"explorer_win")
        self.verticalLayout_2 = QVBoxLayout(self.explorer_win)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.explorer_win)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

        self.filetree = QTreeWidget(self.explorer_win)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.filetree.setHeaderItem(__qtreewidgetitem)
        self.filetree.setObjectName(u"filetree")
        self.filetree.setFrameShape(QFrame.NoFrame)
        self.filetree.header().setVisible(False)

        self.verticalLayout_2.addWidget(self.filetree)

        self.nav_window.addWidget(self.explorer_win)
        self.reference_win = QWidget()
        self.reference_win.setObjectName(u"reference_win")
        self.verticalLayout_3 = QVBoxLayout(self.reference_win)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_2 = QLabel(self.reference_win)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_3.addWidget(self.label_2)

        self.reftree = QTreeWidget(self.reference_win)
        __qtreewidgetitem1 = QTreeWidgetItem()
        __qtreewidgetitem1.setText(0, u"1");
        self.reftree.setHeaderItem(__qtreewidgetitem1)
        self.reftree.setObjectName(u"reftree")
        self.reftree.setFrameShape(QFrame.NoFrame)
        self.reftree.header().setVisible(False)

        self.verticalLayout_3.addWidget(self.reftree)

        self.nav_window.addWidget(self.reference_win)
        self.settings_win = QWidget()
        self.settings_win.setObjectName(u"settings_win")
        self.verticalLayout_4 = QVBoxLayout(self.settings_win)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_3 = QLabel(self.settings_win)
        self.label_3.setObjectName(u"label_3")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy6)

        self.verticalLayout_4.addWidget(self.label_3)

        self.settingstree = QFrame(self.settings_win)
        self.settingstree.setObjectName(u"settingstree")
        self.settingstree.setFrameShape(QFrame.NoFrame)
        self.settingstree.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.settingstree)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_7 = QLabel(self.settingstree)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 0, 0, 1, 1)

        self.lineEdit = QLineEdit(self.settingstree)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)


        self.verticalLayout_4.addWidget(self.settingstree)

        self.nav_window.addWidget(self.settings_win)

        self.gridLayout_3.addWidget(self.nav_window, 0, 2, 1, 1)


        self.gridLayout_4.addWidget(self.context_menu, 0, 0, 1, 1)

        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout_4.addWidget(self.line_2, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1528, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        self.menuView = QMenu(self.menubar)
        self.menuView.setObjectName(u"menuView")
        self.menuAppearance = QMenu(self.menuView)
        self.menuAppearance.setObjectName(u"menuAppearance")
        self.menuColor_palatte = QMenu(self.menuAppearance)
        self.menuColor_palatte.setObjectName(u"menuColor_palatte")
        self.menuLayout = QMenu(self.menuView)
        self.menuLayout.setObjectName(u"menuLayout")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
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
        self.menuView.addAction(self.menuAppearance.menuAction())
        self.menuView.addAction(self.menuLayout.menuAction())
        self.menuAppearance.addAction(self.menuColor_palatte.menuAction())
        self.menuAppearance.addAction(self.actionShow_Reference_2)
        self.menuAppearance.addAction(self.actionShow_console)
        self.menuColor_palatte.addAction(self.actionLight)
        self.menuColor_palatte.addAction(self.actionDark)
        self.menuLayout.addAction(self.actionDefault)
        self.menuLayout.addAction(self.actionAdd_custom)

        self.retranslateUi(MainWindow)

        self.editor_win.setCurrentIndex(0)
        self.nav_window.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionNew_file.setText(QCoreApplication.translate("MainWindow", u"New file", None))
        self.actionOpen_File.setText(QCoreApplication.translate("MainWindow", u"Open File", None))
        self.actionOpen_Folder.setText(QCoreApplication.translate("MainWindow", u"Open Folder", None))
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.actionSave_as.setText(QCoreApplication.translate("MainWindow", u"Save as", None))
        self.actionClose_folder.setText(QCoreApplication.translate("MainWindow", u"Close folder", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.actionUndo.setText(QCoreApplication.translate("MainWindow", u"Undo", None))
        self.actionRedo.setText(QCoreApplication.translate("MainWindow", u"Redo", None))
        self.actionCut.setText(QCoreApplication.translate("MainWindow", u"Cut", None))
        self.actionCopy.setText(QCoreApplication.translate("MainWindow", u"Copy", None))
        self.actionPaste.setText(QCoreApplication.translate("MainWindow", u"Paste", None))
        self.actionLight.setText(QCoreApplication.translate("MainWindow", u"Light", None))
        self.actionDark.setText(QCoreApplication.translate("MainWindow", u"Dark", None))
        self.actionShow_Reference_2.setText(QCoreApplication.translate("MainWindow", u"Show reference", None))
        self.actionShow_console.setText(QCoreApplication.translate("MainWindow", u"Show console", None))
        self.actionDefault.setText(QCoreApplication.translate("MainWindow", u"Default", None))
        self.actionAdd_custom.setText(QCoreApplication.translate("MainWindow", u"Add custom", None))
        self.editor_win.setTabText(self.editor_win.indexOf(self.doc_tab), QCoreApplication.translate("MainWindow", u"Untitled", None))
        self.editor_win.setTabText(self.editor_win.indexOf(self.quickadd_btn), "")
        self.logfile_btn_4.setText(QCoreApplication.translate("MainWindow", u"Add log file", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Console", None))
        self.logfile_label_4.setText("")
        self.settings_btn.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.reference_btn.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.explorer_btn.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Explorer", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"HCI Reference", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Placeholder", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.menuView.setTitle(QCoreApplication.translate("MainWindow", u"View", None))
        self.menuAppearance.setTitle(QCoreApplication.translate("MainWindow", u"Appearance", None))
        self.menuColor_palatte.setTitle(QCoreApplication.translate("MainWindow", u"Color palatte", None))
        self.menuLayout.setTitle(QCoreApplication.translate("MainWindow", u"Layout", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

