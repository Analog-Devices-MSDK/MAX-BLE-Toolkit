# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dtm_tool.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QSlider, QSpinBox, QStatusBar,
    QTabWidget, QTextEdit, QToolBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1446, 720)
        MainWindow.setMaximumSize(QSize(16777215, 720))
        MainWindow.setLayoutDirection(Qt.LeftToRight)
        MainWindow.setAutoFillBackground(False)
        self.actionDocumentation = QAction(MainWindow)
        self.actionDocumentation.setObjectName(u"actionDocumentation")
        self.action_about = QAction(MainWindow)
        self.action_about.setObjectName(u"action_about")
        self.action_report_issue = QAction(MainWindow)
        self.action_report_issue.setObjectName(u"action_report_issue")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.tab_mode = QTabWidget(self.centralwidget)
        self.tab_mode.setObjectName(u"tab_mode")
        self.tab_tx = QWidget()
        self.tab_tx.setObjectName(u"tab_tx")
        self.verticalLayout_4 = QVBoxLayout(self.tab_tx)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_9 = QLabel(self.tab_tx)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_4.addWidget(self.label_9)

        self.port_select_tx = QComboBox(self.tab_tx)
        self.port_select_tx.setObjectName(u"port_select_tx")

        self.verticalLayout_4.addWidget(self.port_select_tx)

        self.label_10 = QLabel(self.tab_tx)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_4.addWidget(self.label_10)

        self.baud_rate_select_tx = QSpinBox(self.tab_tx)
        self.baud_rate_select_tx.setObjectName(u"baud_rate_select_tx")
        self.baud_rate_select_tx.setMaximum(10000000)

        self.verticalLayout_4.addWidget(self.baud_rate_select_tx)

        self.label_11 = QLabel(self.tab_tx)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_4.addWidget(self.label_11)

        self.phy_select_tx = QComboBox(self.tab_tx)
        self.phy_select_tx.setObjectName(u"phy_select_tx")

        self.verticalLayout_4.addWidget(self.phy_select_tx)

        self.packet_type_label_3 = QLabel(self.tab_tx)
        self.packet_type_label_3.setObjectName(u"packet_type_label_3")
        self.packet_type_label_3.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_4.addWidget(self.packet_type_label_3)

        self.packet_type_select_tx = QComboBox(self.tab_tx)
        self.packet_type_select_tx.setObjectName(u"packet_type_select_tx")

        self.verticalLayout_4.addWidget(self.packet_type_select_tx)

        self.label_12 = QLabel(self.tab_tx)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_4.addWidget(self.label_12)

        self.power_select_tx = QComboBox(self.tab_tx)
        self.power_select_tx.setObjectName(u"power_select_tx")

        self.verticalLayout_4.addWidget(self.power_select_tx)

        self.channel_label_tx = QLabel(self.tab_tx)
        self.channel_label_tx.setObjectName(u"channel_label_tx")
        self.channel_label_tx.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_4.addWidget(self.channel_label_tx)

        self.channel_select_tx = QSlider(self.tab_tx)
        self.channel_select_tx.setObjectName(u"channel_select_tx")
        self.channel_select_tx.setMaximum(39)
        self.channel_select_tx.setOrientation(Qt.Horizontal)

        self.verticalLayout_4.addWidget(self.channel_select_tx)

        self.packet_len_label_tx = QLabel(self.tab_tx)
        self.packet_len_label_tx.setObjectName(u"packet_len_label_tx")
        self.packet_len_label_tx.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_4.addWidget(self.packet_len_label_tx)

        self.packet_len_select_tx = QSlider(self.tab_tx)
        self.packet_len_select_tx.setObjectName(u"packet_len_select_tx")
        self.packet_len_select_tx.setMaximum(255)
        self.packet_len_select_tx.setOrientation(Qt.Horizontal)

        self.verticalLayout_4.addWidget(self.packet_len_select_tx)

        self.start_stop_btn_tx = QPushButton(self.tab_tx)
        self.start_stop_btn_tx.setObjectName(u"start_stop_btn_tx")
        self.start_stop_btn_tx.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_4.addWidget(self.start_stop_btn_tx)

        self.tab_mode.addTab(self.tab_tx, "")
        self.tab_rx = QWidget()
        self.tab_rx.setObjectName(u"tab_rx")
        self.verticalLayout_5 = QVBoxLayout(self.tab_rx)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_13 = QLabel(self.tab_rx)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_5.addWidget(self.label_13)

        self.port_select_rx = QComboBox(self.tab_rx)
        self.port_select_rx.setObjectName(u"port_select_rx")

        self.verticalLayout_5.addWidget(self.port_select_rx)

        self.label_14 = QLabel(self.tab_rx)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_5.addWidget(self.label_14)

        self.baud_rate_select_rx = QSpinBox(self.tab_rx)
        self.baud_rate_select_rx.setObjectName(u"baud_rate_select_rx")
        self.baud_rate_select_rx.setMaximum(10000000)

        self.verticalLayout_5.addWidget(self.baud_rate_select_rx)

        self.label_15 = QLabel(self.tab_rx)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_5.addWidget(self.label_15)

        self.phy_select_rx = QComboBox(self.tab_rx)
        self.phy_select_rx.setObjectName(u"phy_select_rx")

        self.verticalLayout_5.addWidget(self.phy_select_rx)

        self.channel_label_rx = QLabel(self.tab_rx)
        self.channel_label_rx.setObjectName(u"channel_label_rx")
        self.channel_label_rx.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_5.addWidget(self.channel_label_rx)

        self.channel_select_rx = QSlider(self.tab_rx)
        self.channel_select_rx.setObjectName(u"channel_select_rx")
        self.channel_select_rx.setMaximum(39)
        self.channel_select_rx.setOrientation(Qt.Horizontal)

        self.verticalLayout_5.addWidget(self.channel_select_rx)

        self.update_rate_label = QLabel(self.tab_rx)
        self.update_rate_label.setObjectName(u"update_rate_label")

        self.verticalLayout_5.addWidget(self.update_rate_label)

        self.update_rate_slider = QSlider(self.tab_rx)
        self.update_rate_slider.setObjectName(u"update_rate_slider")
        self.update_rate_slider.setMinimum(5)
        self.update_rate_slider.setMaximum(100)
        self.update_rate_slider.setSingleStep(5)
        self.update_rate_slider.setOrientation(Qt.Horizontal)

        self.verticalLayout_5.addWidget(self.update_rate_slider)

        self.rx_ok_label = QLabel(self.tab_rx)
        self.rx_ok_label.setObjectName(u"rx_ok_label")

        self.verticalLayout_5.addWidget(self.rx_ok_label)

        self.rx_crc_label = QLabel(self.tab_rx)
        self.rx_crc_label.setObjectName(u"rx_crc_label")

        self.verticalLayout_5.addWidget(self.rx_crc_label)

        self.rx_timeout_label = QLabel(self.tab_rx)
        self.rx_timeout_label.setObjectName(u"rx_timeout_label")

        self.verticalLayout_5.addWidget(self.rx_timeout_label)

        self.rx_per_label = QLabel(self.tab_rx)
        self.rx_per_label.setObjectName(u"rx_per_label")

        self.verticalLayout_5.addWidget(self.rx_per_label)

        self.start_stop_btn_rx = QPushButton(self.tab_rx)
        self.start_stop_btn_rx.setObjectName(u"start_stop_btn_rx")

        self.verticalLayout_5.addWidget(self.start_stop_btn_rx)

        self.tab_mode.addTab(self.tab_rx, "")

        self.verticalLayout_6.addWidget(self.tab_mode)


        self.horizontalLayout_5.addLayout(self.verticalLayout_6)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.reset_hci = QPushButton(self.centralwidget)
        self.reset_hci.setObjectName(u"reset_hci")
        self.reset_hci.setMaximumSize(QSize(100, 50))

        self.verticalLayout_3.addWidget(self.reset_hci, 0, Qt.AlignHCenter)

        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setReadOnly(True)

        self.verticalLayout_3.addWidget(self.textEdit)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1446, 22))
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuHelp.addAction(self.action_about)
        self.menuHelp.addAction(self.action_report_issue)

        self.retranslateUi(MainWindow)

        self.tab_mode.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"DTM TOOL", None))
        self.actionDocumentation.setText(QCoreApplication.translate("MainWindow", u"Documentation", None))
        self.action_about.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.action_report_issue.setText(QCoreApplication.translate("MainWindow", u"Report Issue", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Port", None))
        self.port_select_tx.setCurrentText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Baud", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"PHY", None))
        self.packet_type_label_3.setText(QCoreApplication.translate("MainWindow", u"Packet Type", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Power", None))
        self.channel_label_tx.setText(QCoreApplication.translate("MainWindow", u"Channel", None))
        self.packet_len_label_tx.setText(QCoreApplication.translate("MainWindow", u"Packet Length", None))
        self.start_stop_btn_tx.setText(QCoreApplication.translate("MainWindow", u"START TX", None))
        self.tab_mode.setTabText(self.tab_mode.indexOf(self.tab_tx), QCoreApplication.translate("MainWindow", u"TX", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Port", None))
        self.port_select_rx.setCurrentText("")
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Baud", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"PHY", None))
        self.channel_label_rx.setText(QCoreApplication.translate("MainWindow", u"Channel", None))
        self.update_rate_label.setText(QCoreApplication.translate("MainWindow", u"Update Rate (s)", None))
        self.rx_ok_label.setText(QCoreApplication.translate("MainWindow", u"RX OK - 0", None))
        self.rx_crc_label.setText(QCoreApplication.translate("MainWindow", u"RX CRC - 0", None))
        self.rx_timeout_label.setText(QCoreApplication.translate("MainWindow", u"RX Timeout - 0", None))
        self.rx_per_label.setText(QCoreApplication.translate("MainWindow", u"PER - 0", None))
        self.start_stop_btn_rx.setText(QCoreApplication.translate("MainWindow", u"START RX", None))
        self.tab_mode.setTabText(self.tab_mode.indexOf(self.tab_rx), QCoreApplication.translate("MainWindow", u"RX", None))
        self.reset_hci.setText(QCoreApplication.translate("MainWindow", u"RESET HCI", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

