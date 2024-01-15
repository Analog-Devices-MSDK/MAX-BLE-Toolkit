# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dtm_tx.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QSlider, QSpinBox, QStatusBar,
    QTabWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1198, 720)
        MainWindow.setMaximumSize(QSize(16777215, 720))
        MainWindow.setLayoutDirection(Qt.LeftToRight)
        MainWindow.setAutoFillBackground(False)
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
        self.tx_frame = QFrame(self.tab_tx)
        self.tx_frame.setObjectName(u"tx_frame")
        self.tx_frame.setGeometry(QRect(0, 0, 1176, 531))
        self.tx_frame.setFrameShape(QFrame.StyledPanel)
        self.tx_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.tx_frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_9 = QLabel(self.tx_frame)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_4.addWidget(self.label_9)

        self.port_select_tx = QComboBox(self.tx_frame)
        self.port_select_tx.setObjectName(u"port_select_tx")

        self.verticalLayout_4.addWidget(self.port_select_tx)

        self.label_10 = QLabel(self.tx_frame)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_4.addWidget(self.label_10)

        self.baud_rate_select_tx = QSpinBox(self.tx_frame)
        self.baud_rate_select_tx.setObjectName(u"baud_rate_select_tx")
        self.baud_rate_select_tx.setMaximum(10000000)

        self.verticalLayout_4.addWidget(self.baud_rate_select_tx)

        self.label_11 = QLabel(self.tx_frame)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_4.addWidget(self.label_11)

        self.phy_select_tx = QComboBox(self.tx_frame)
        self.phy_select_tx.setObjectName(u"phy_select_tx")

        self.verticalLayout_4.addWidget(self.phy_select_tx)

        self.packet_type_label_3 = QLabel(self.tx_frame)
        self.packet_type_label_3.setObjectName(u"packet_type_label_3")
        self.packet_type_label_3.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_4.addWidget(self.packet_type_label_3)

        self.packet_type_select_tx = QComboBox(self.tx_frame)
        self.packet_type_select_tx.setObjectName(u"packet_type_select_tx")

        self.verticalLayout_4.addWidget(self.packet_type_select_tx)

        self.label_12 = QLabel(self.tx_frame)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_4.addWidget(self.label_12)

        self.power_select_tx = QComboBox(self.tx_frame)
        self.power_select_tx.setObjectName(u"power_select_tx")

        self.verticalLayout_4.addWidget(self.power_select_tx)

        self.channel_label_tx = QLabel(self.tx_frame)
        self.channel_label_tx.setObjectName(u"channel_label_tx")
        self.channel_label_tx.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_4.addWidget(self.channel_label_tx)

        self.channel_select_tx = QSlider(self.tx_frame)
        self.channel_select_tx.setObjectName(u"channel_select_tx")
        self.channel_select_tx.setMaximum(39)
        self.channel_select_tx.setOrientation(Qt.Horizontal)

        self.verticalLayout_4.addWidget(self.channel_select_tx)

        self.packet_len_label_tx = QLabel(self.tx_frame)
        self.packet_len_label_tx.setObjectName(u"packet_len_label_tx")
        self.packet_len_label_tx.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_4.addWidget(self.packet_len_label_tx)

        self.packet_len_select_tx = QSlider(self.tx_frame)
        self.packet_len_select_tx.setObjectName(u"packet_len_select_tx")
        self.packet_len_select_tx.setMaximum(255)
        self.packet_len_select_tx.setOrientation(Qt.Horizontal)

        self.verticalLayout_4.addWidget(self.packet_len_select_tx)

        self.start_stop_btn_tx = QPushButton(self.tab_tx)
        self.start_stop_btn_tx.setObjectName(u"start_stop_btn_tx")
        self.start_stop_btn_tx.setGeometry(QRect(510, 550, 100, 25))
        self.start_stop_btn_tx.setMaximumSize(QSize(100, 50))
        self.tab_mode.addTab(self.tab_tx, "")
        self.tab_rx = QWidget()
        self.tab_rx.setObjectName(u"tab_rx")
        self.rx_input_frame = QFrame(self.tab_rx)
        self.rx_input_frame.setObjectName(u"rx_input_frame")
        self.rx_input_frame.setGeometry(QRect(0, 0, 1176, 501))
        self.rx_input_frame.setFrameShape(QFrame.StyledPanel)
        self.rx_input_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.rx_input_frame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_13 = QLabel(self.rx_input_frame)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_5.addWidget(self.label_13)

        self.port_select_rx = QComboBox(self.rx_input_frame)
        self.port_select_rx.setObjectName(u"port_select_rx")

        self.verticalLayout_5.addWidget(self.port_select_rx)

        self.label_14 = QLabel(self.rx_input_frame)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_5.addWidget(self.label_14)

        self.baud_rate_select_rx = QSpinBox(self.rx_input_frame)
        self.baud_rate_select_rx.setObjectName(u"baud_rate_select_rx")
        self.baud_rate_select_rx.setMaximum(10000000)

        self.verticalLayout_5.addWidget(self.baud_rate_select_rx)

        self.label_15 = QLabel(self.rx_input_frame)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_5.addWidget(self.label_15)

        self.phy_select_rx = QComboBox(self.rx_input_frame)
        self.phy_select_rx.setObjectName(u"phy_select_rx")

        self.verticalLayout_5.addWidget(self.phy_select_rx)

        self.channel_label_rx = QLabel(self.rx_input_frame)
        self.channel_label_rx.setObjectName(u"channel_label_rx")
        self.channel_label_rx.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_5.addWidget(self.channel_label_rx)

        self.channel_select_rx = QSlider(self.rx_input_frame)
        self.channel_select_rx.setObjectName(u"channel_select_rx")
        self.channel_select_rx.setMaximum(39)
        self.channel_select_rx.setOrientation(Qt.Horizontal)

        self.verticalLayout_5.addWidget(self.channel_select_rx)

        self.start_stop_btn_rx = QPushButton(self.tab_rx)
        self.start_stop_btn_rx.setObjectName(u"start_stop_btn_rx")
        self.start_stop_btn_rx.setGeometry(QRect(0, 550, 1156, 25))
        self.rx_per_label = QLabel(self.tab_rx)
        self.rx_per_label.setObjectName(u"rx_per_label")
        self.rx_per_label.setGeometry(QRect(500, 510, 181, 31))
        self.tab_mode.addTab(self.tab_rx, "")

        self.verticalLayout_6.addWidget(self.tab_mode)


        self.horizontalLayout_5.addLayout(self.verticalLayout_6)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.reset_hci = QPushButton(self.centralwidget)
        self.reset_hci.setObjectName(u"reset_hci")
        self.reset_hci.setMaximumSize(QSize(100, 50))

        self.verticalLayout_3.addWidget(self.reset_hci)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1198, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tab_mode.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"DTM_TX", None))
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
        self.start_stop_btn_rx.setText(QCoreApplication.translate("MainWindow", u"START RX", None))
        self.rx_per_label.setText(QCoreApplication.translate("MainWindow", u"PER", None))
        self.tab_mode.setTabText(self.tab_mode.indexOf(self.tab_rx), QCoreApplication.translate("MainWindow", u"RX", None))
        self.reset_hci.setText(QCoreApplication.translate("MainWindow", u"RESET", None))
    # retranslateUi

