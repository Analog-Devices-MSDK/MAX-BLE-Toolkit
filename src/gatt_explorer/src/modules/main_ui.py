# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCharts import QChartView
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QComboBox,
    QCommandLinkButton, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QMainWindow, QPlainTextEdit, QPushButton,
    QRadioButton, QScrollArea, QScrollBar, QSizePolicy,
    QSlider, QSpacerItem, QSplitter, QStackedWidget,
    QTableWidget, QTableWidgetItem, QTreeWidget, QTreeWidgetItem,
    QVBoxLayout, QWidget)

from custom_widgets.toggle import AnimatedToggle
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1195, 670)
        MainWindow.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_main_top_bar = QFrame(self.centralwidget)
        self.frame_main_top_bar.setObjectName(u"frame_main_top_bar")
        self.frame_main_top_bar.setMinimumSize(QSize(0, 53))
        self.frame_main_top_bar.setMaximumSize(QSize(16777215, 53))
        self.frame_main_top_bar.setStyleSheet(u"background-color: #0067B9\n"
"\n"
"")
        self.frame_main_top_bar.setFrameShape(QFrame.StyledPanel)
        self.frame_main_top_bar.setFrameShadow(QFrame.Raised)
        self.label_2 = QLabel(self.frame_main_top_bar)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(180, 0, 1064, 51))
        font = QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"")
        self.topLeftLogo = QFrame(self.frame_main_top_bar)
        self.topLeftLogo.setObjectName(u"topLeftLogo")
        self.topLeftLogo.setGeometry(QRect(30, 0, 101, 61))
        self.topLeftLogo.setMinimumSize(QSize(0, 0))
        self.topLeftLogo.setMaximumSize(QSize(9999999, 16777215))
        self.topLeftLogo.setFrameShape(QFrame.StyledPanel)
        self.topLeftLogo.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.topLeftLogo)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.topLeftLogoLabel = QLabel(self.topLeftLogo)
        self.topLeftLogoLabel.setObjectName(u"topLeftLogoLabel")

        self.verticalLayout_3.addWidget(self.topLeftLogoLabel)

        self.label = QLabel(self.frame_main_top_bar)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(160, -80, 16, 201))
        font1 = QFont()
        font1.setFamilies([u"Umpush"])
        font1.setPointSize(31)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.frame_main_top_bar)

        self.frame_main_middle = QFrame(self.centralwidget)
        self.frame_main_middle.setObjectName(u"frame_main_middle")
        self.frame_main_middle.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"QFrame {\n"
"    border: 0px;\n"
"}")
        self.frame_main_middle.setFrameShape(QFrame.StyledPanel)
        self.frame_main_middle.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_main_middle)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_main_left = QFrame(self.frame_main_middle)
        self.frame_main_left.setObjectName(u"frame_main_left")
        self.frame_main_left.setMinimumSize(QSize(165, 0))
        self.frame_main_left.setMaximumSize(QSize(165, 16777215))
        self.frame_main_left.setStyleSheet(u"background-color: #EBEBEF;\n"
"")
        self.frame_main_left.setFrameShape(QFrame.StyledPanel)
        self.frame_main_left.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.frame_main_left)

        self.frame_main_middle_2 = QFrame(self.frame_main_middle)
        self.frame_main_middle_2.setObjectName(u"frame_main_middle_2")
        self.frame_main_middle_2.setFrameShape(QFrame.StyledPanel)
        self.frame_main_middle_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_main_middle_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.console_splitter = QSplitter(self.frame_main_middle_2)
        self.console_splitter.setObjectName(u"console_splitter")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.console_splitter.sizePolicy().hasHeightForWidth())
        self.console_splitter.setSizePolicy(sizePolicy)
        self.console_splitter.setBaseSize(QSize(0, 0))
        self.console_splitter.setOrientation(Qt.Vertical)
        self.console_splitter.setHandleWidth(6)
        self.frame_main_middle_content = QFrame(self.console_splitter)
        self.frame_main_middle_content.setObjectName(u"frame_main_middle_content")
        self.frame_main_middle_content.setMinimumSize(QSize(0, 300))
        self.frame_main_middle_content.setStyleSheet(u"border: 0px solid #E0E0F0;\n"
"border-radius: 0px;	\n"
"")
        self.frame_main_middle_content.setFrameShape(QFrame.StyledPanel)
        self.frame_main_middle_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_main_middle_content)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.stackedWidget = QStackedWidget(self.frame_main_middle_content)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.home.setStyleSheet(u"")
        self.verticalLayout_22 = QVBoxLayout(self.home)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.frame_explorer_top = QFrame(self.home)
        self.frame_explorer_top.setObjectName(u"frame_explorer_top")
        self.frame_explorer_top.setStyleSheet(u"")
        self.frame_explorer_top.setFrameShape(QFrame.StyledPanel)
        self.frame_explorer_top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_explorer_top)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, -1, -1, -1)
        self.frame_scan_results = QFrame(self.frame_explorer_top)
        self.frame_scan_results.setObjectName(u"frame_scan_results")
        self.frame_scan_results.setStyleSheet(u"")
        self.frame_scan_results.setFrameShape(QFrame.StyledPanel)
        self.frame_scan_results.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_scan_results)
        self.verticalLayout_24.setSpacing(6)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(-1, 0, -1, 0)
        self.frame_3 = QFrame(self.frame_scan_results)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 40))
        self.frame_3.setMaximumSize(QSize(16777215, 40))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, -1)
        self.txt_scan_filter_2 = QLineEdit(self.frame_3)
        self.txt_scan_filter_2.setObjectName(u"txt_scan_filter_2")
        self.txt_scan_filter_2.setMinimumSize(QSize(0, 30))
        self.txt_scan_filter_2.setMaximumSize(QSize(16777215, 35))
        self.txt_scan_filter_2.setStyleSheet(u"color: #464E69;\n"
"background-color: #EBEBEF;\n"
"")

        self.horizontalLayout_7.addWidget(self.txt_scan_filter_2)


        self.verticalLayout_24.addWidget(self.frame_3)

        self.list_widget_discovered = QListWidget(self.frame_scan_results)
        self.list_widget_discovered.setObjectName(u"list_widget_discovered")
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(10)
        font2.setBold(False)
        font2.setItalic(False)
        self.list_widget_discovered.setFont(font2)
        self.list_widget_discovered.setStyleSheet(u"border: 2px solid #EBEBEF;\n"
"border-radius: 5px;	\n"
"color: : #464E69;\n"
"")
        self.list_widget_discovered.setSelectionMode(QAbstractItemView.SingleSelection)

        self.verticalLayout_24.addWidget(self.list_widget_discovered)

        self.frame_12 = QFrame(self.frame_scan_results)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMinimumSize(QSize(0, 0))
        self.frame_12.setStyleSheet(u" border: 0px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 6, 0, -1)
        self.btn_scan_2 = QPushButton(self.frame_12)
        self.btn_scan_2.setObjectName(u"btn_scan_2")
        self.btn_scan_2.setMinimumSize(QSize(0, 30))
        self.btn_scan_2.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(153, 193, 241);\n"
" border: 0px solid rgb(52, 59, 72);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;	\n"
"text-align: center;\n"
"padding: 0px;\n"
"margin: 0px;\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(255, 255, 255);\n"
"background-color: #464E69;\n"
"}\n"
"QPushButton:pressed{\n"
"color: rgb(255, 255, 255);\n"
"background-color: #262E49;\n"
"}")

        self.horizontalLayout_19.addWidget(self.btn_scan_2)

        self.pushButton = QPushButton(self.frame_12)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_19.addWidget(self.pushButton)

        self.btn_connect = QPushButton(self.frame_12)
        self.btn_connect.setObjectName(u"btn_connect")
        self.btn_connect.setMinimumSize(QSize(0, 30))
        self.btn_connect.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(153, 193, 241);\n"
" border: 0px solid rgb(52, 59, 72);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;	\n"
"text-align: center;\n"
"padding: 0px;\n"
"margin: 0px;\n"
"}\n"
"QPushButton:hover{\n"
"color: rgb(255, 255, 255);\n"
"background-color: #464E69;\n"
"}\n"
"QPushButton:pressed{\n"
"color: rgb(255, 255, 255);\n"
"background-color: #262E49;\n"
"}")

        self.horizontalLayout_19.addWidget(self.btn_connect)


        self.verticalLayout_24.addWidget(self.frame_12)


        self.horizontalLayout_8.addWidget(self.frame_scan_results)

        self.rssi_gatt_expolrer = QStackedWidget(self.frame_explorer_top)
        self.rssi_gatt_expolrer.setObjectName(u"rssi_gatt_expolrer")
        self.rssi_graph = QWidget()
        self.rssi_graph.setObjectName(u"rssi_graph")
        self.verticalLayout_25 = QVBoxLayout(self.rssi_graph)
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(-1, 0, -1, 0)
        self.qtchart_widgetholder = QChartView(self.rssi_graph)
        self.qtchart_widgetholder.setObjectName(u"qtchart_widgetholder")

        self.verticalLayout_25.addWidget(self.qtchart_widgetholder)

        self.rssi_gatt_expolrer.addWidget(self.rssi_graph)
        self.gatt_view = QWidget()
        self.gatt_view.setObjectName(u"gatt_view")
        self.verticalLayout_26 = QVBoxLayout(self.gatt_view)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(-1, 0, -1, -1)
        self.label_3 = QLabel(self.gatt_view)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_26.addWidget(self.label_3)

        self.tree_gatt_view = QTreeWidget(self.gatt_view)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"1");
        self.tree_gatt_view.setHeaderItem(__qtreewidgetitem)
        self.tree_gatt_view.setObjectName(u"tree_gatt_view")

        self.verticalLayout_26.addWidget(self.tree_gatt_view)

        self.rssi_gatt_expolrer.addWidget(self.gatt_view)

        self.horizontalLayout_8.addWidget(self.rssi_gatt_expolrer)

        self.horizontalLayout_8.setStretch(0, 2)
        self.horizontalLayout_8.setStretch(1, 2)

        self.verticalLayout_22.addWidget(self.frame_explorer_top)

        self.frame_adv_data = QFrame(self.home)
        self.frame_adv_data.setObjectName(u"frame_adv_data")
        self.frame_adv_data.setMinimumSize(QSize(0, 60))
        self.frame_adv_data.setFrameShape(QFrame.StyledPanel)
        self.frame_adv_data.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_adv_data)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(-1, 0, -1, 0)
        self.tableWidget_2 = QTableWidget(self.frame_adv_data)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setStyleSheet(u"QTableWidget {	\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 58);\n"
"border: 2px solid  #EBEBEF;\n"
"}\n"
"QTableWidget::item{\n"
"	border-color:  #EBEBEF;\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(189, 147, 249);\n"
"}\n"
"QHeaderView::section{\n"
"	background-color: rgb(33, 37, 43);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(33, 37, 43);\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px "
                        "solid rgb(44, 49, 60);\n"
"}")
        self.tableWidget_2.horizontalHeader().setVisible(False)
        self.tableWidget_2.verticalHeader().setVisible(False)

        self.verticalLayout_21.addWidget(self.tableWidget_2)

        self.verticalLayout_21.setStretch(0, 7)

        self.verticalLayout_22.addWidget(self.frame_adv_data)

        self.verticalLayout_22.setStretch(0, 3)
        self.verticalLayout_22.setStretch(1, 3)
        self.stackedWidget.addWidget(self.home)
        self.widgets = QWidget()
        self.widgets.setObjectName(u"widgets")
        self.widgets.setStyleSheet(u"b")
        self.verticalLayout_4 = QVBoxLayout(self.widgets)
        self.verticalLayout_4.setSpacing(10)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(10, 10, 10, 10)
        self.row_1 = QFrame(self.widgets)
        self.row_1.setObjectName(u"row_1")
        self.row_1.setFrameShape(QFrame.StyledPanel)
        self.row_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.row_1)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.frame_div_content_1 = QFrame(self.row_1)
        self.frame_div_content_1.setObjectName(u"frame_div_content_1")
        self.frame_div_content_1.setMinimumSize(QSize(0, 110))
        self.frame_div_content_1.setMaximumSize(QSize(16777215, 110))
        self.frame_div_content_1.setFrameShape(QFrame.NoFrame)
        self.frame_div_content_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_div_content_1)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.frame_title_wid_1 = QFrame(self.frame_div_content_1)
        self.frame_title_wid_1.setObjectName(u"frame_title_wid_1")
        self.frame_title_wid_1.setMaximumSize(QSize(16777215, 35))
        self.frame_title_wid_1.setFrameShape(QFrame.StyledPanel)
        self.frame_title_wid_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_title_wid_1)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.labelBoxBlenderInstalation = QLabel(self.frame_title_wid_1)
        self.labelBoxBlenderInstalation.setObjectName(u"labelBoxBlenderInstalation")
        self.labelBoxBlenderInstalation.setFont(font2)
        self.labelBoxBlenderInstalation.setStyleSheet(u"")

        self.verticalLayout_18.addWidget(self.labelBoxBlenderInstalation)


        self.verticalLayout_17.addWidget(self.frame_title_wid_1)

        self.frame_content_wid_1 = QFrame(self.frame_div_content_1)
        self.frame_content_wid_1.setObjectName(u"frame_content_wid_1")
        self.frame_content_wid_1.setFrameShape(QFrame.NoFrame)
        self.frame_content_wid_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_content_wid_1)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, -1, -1, 0)
        self.lineEdit = QLineEdit(self.frame_content_wid_1)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 30))
        self.lineEdit.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 1)

        self.pushButton_2 = QPushButton(self.frame_content_wid_1)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(150, 30))
        self.pushButton_2.setFont(font2)
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/cil-folder-open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon)

        self.gridLayout.addWidget(self.pushButton_2, 0, 1, 1, 1)

        self.labelVersion_3 = QLabel(self.frame_content_wid_1)
        self.labelVersion_3.setObjectName(u"labelVersion_3")
        self.labelVersion_3.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_3.setLineWidth(1)
        self.labelVersion_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.labelVersion_3, 1, 0, 1, 2)


        self.horizontalLayout_9.addLayout(self.gridLayout)


        self.verticalLayout_17.addWidget(self.frame_content_wid_1)


        self.verticalLayout_16.addWidget(self.frame_div_content_1)


        self.verticalLayout_4.addWidget(self.row_1)

        self.row_2 = QFrame(self.widgets)
        self.row_2.setObjectName(u"row_2")
        self.row_2.setMinimumSize(QSize(0, 150))
        self.row_2.setFrameShape(QFrame.StyledPanel)
        self.row_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.row_2)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.checkBox = AnimatedToggle(self.row_2)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setAutoFillBackground(False)
        self.checkBox.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.checkBox, 0, 0, 1, 1)

        self.radioButton = QRadioButton(self.row_2)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.radioButton, 0, 1, 1, 1)

        self.verticalSlider = QSlider(self.row_2)
        self.verticalSlider.setObjectName(u"verticalSlider")
        self.verticalSlider.setStyleSheet(u"")
        self.verticalSlider.setOrientation(Qt.Vertical)

        self.gridLayout_2.addWidget(self.verticalSlider, 0, 2, 3, 1)

        self.verticalScrollBar = QScrollBar(self.row_2)
        self.verticalScrollBar.setObjectName(u"verticalScrollBar")
        self.verticalScrollBar.setStyleSheet(u" QScrollBar:vertical { background: rgb(52, 59, 72); }\n"
" QScrollBar:horizontal { background: rgb(52, 59, 72); }")
        self.verticalScrollBar.setOrientation(Qt.Vertical)

        self.gridLayout_2.addWidget(self.verticalScrollBar, 0, 4, 3, 1)

        self.scrollArea = QScrollArea(self.row_2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u" QScrollBar:vertical {\n"
"    background: rgb(52, 59, 72);\n"
" }\n"
" QScrollBar:horizontal {\n"
"    background: rgb(52, 59, 72);\n"
" }")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 218, 218))
        self.scrollAreaWidgetContents.setStyleSheet(u" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }")
        self.horizontalLayout_11 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.plainTextEdit = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setMinimumSize(QSize(200, 200))
        self.plainTextEdit.setStyleSheet(u"background-color: rgb(33, 37, 43);")

        self.horizontalLayout_11.addWidget(self.plainTextEdit)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_2.addWidget(self.scrollArea, 0, 5, 3, 1)

        self.comboBox = QComboBox(self.row_2)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setFont(font2)
        self.comboBox.setAutoFillBackground(False)
        self.comboBox.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.comboBox.setIconSize(QSize(16, 16))
        self.comboBox.setFrame(True)

        self.gridLayout_2.addWidget(self.comboBox, 1, 0, 1, 2)

        self.horizontalScrollBar = QScrollBar(self.row_2)
        self.horizontalScrollBar.setObjectName(u"horizontalScrollBar")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.horizontalScrollBar.sizePolicy().hasHeightForWidth())
        self.horizontalScrollBar.setSizePolicy(sizePolicy1)
        self.horizontalScrollBar.setStyleSheet(u" QScrollBar:vertical { background: rgb(52, 59, 72); }\n"
" QScrollBar:horizontal { background: rgb(52, 59, 72); }")
        self.horizontalScrollBar.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.horizontalScrollBar, 1, 3, 1, 1)

        self.commandLinkButton = QCommandLinkButton(self.row_2)
        self.commandLinkButton.setObjectName(u"commandLinkButton")
        self.commandLinkButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.commandLinkButton.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/cil-link.png", QSize(), QIcon.Normal, QIcon.Off)
        self.commandLinkButton.setIcon(icon1)

        self.gridLayout_2.addWidget(self.commandLinkButton, 1, 6, 1, 1)

        self.horizontalSlider = QSlider(self.row_2)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setStyleSheet(u"")
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.gridLayout_2.addWidget(self.horizontalSlider, 2, 0, 1, 2)


        self.verticalLayout_19.addLayout(self.gridLayout_2)


        self.verticalLayout_4.addWidget(self.row_2)

        self.tableWidget = QTableWidget(self.widgets)
        self.tableWidget.setObjectName(u"tableWidget")

        self.verticalLayout_4.addWidget(self.tableWidget)

        self.row_3 = QFrame(self.widgets)
        self.row_3.setObjectName(u"row_3")
        self.row_3.setMinimumSize(QSize(0, 150))
        self.row_3.setFrameShape(QFrame.StyledPanel)
        self.row_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.row_3)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_4.addWidget(self.row_3)

        self.stackedWidget.addWidget(self.widgets)
        self.insights = QWidget()
        self.insights.setObjectName(u"insights")
        self.horizontalLayout_17 = QHBoxLayout(self.insights)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.frame_8 = QFrame(self.insights)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, -1, 0)
        self.frame_7 = QFrame(self.frame_8)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setStyleSheet(u" border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.frame_7)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.tbl_core_regs = QTableWidget(self.frame_7)
        if (self.tbl_core_regs.columnCount() < 2):
            self.tbl_core_regs.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tbl_core_regs.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tbl_core_regs.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tbl_core_regs.setObjectName(u"tbl_core_regs")
        self.tbl_core_regs.setStyleSheet(u" border: 0px solid rgb(52, 59, 72);\n"
"	border-radius:0px;	\n"
"")
        self.tbl_core_regs.horizontalHeader().setVisible(False)
        self.tbl_core_regs.horizontalHeader().setCascadingSectionResizes(True)
        self.tbl_core_regs.horizontalHeader().setMinimumSectionSize(25)
        self.tbl_core_regs.horizontalHeader().setDefaultSectionSize(40)
        self.tbl_core_regs.horizontalHeader().setStretchLastSection(True)
        self.tbl_core_regs.verticalHeader().setVisible(False)

        self.verticalLayout_32.addWidget(self.tbl_core_regs)

        self.btn_refreshCoreRegs = QPushButton(self.frame_7)
        self.btn_refreshCoreRegs.setObjectName(u"btn_refreshCoreRegs")
        self.btn_refreshCoreRegs.setMinimumSize(QSize(0, 41))
        self.btn_refreshCoreRegs.setStyleSheet(u"QPushButton{\n"
"margin-left: 10px; \n"
"    margin-right: 10px;\n"
"	background-color: rgb(40, 44, 52);\n"
" border: 2px solid rgb(52, 59, 72);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;	\n"
"text-align: center;\n"
"padding: 0px;\n"
"margin: 0px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color: rgb(28, 28, 28);\n"
"background-color: rgb(153, 193, 241);\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	\n"
"		color: rgb(28, 28, 28);\n"
"	background-color: rgb(110,140,255);\n"
"}")

        self.verticalLayout_32.addWidget(self.btn_refreshCoreRegs)

        self.btn_hideCoreRegs = QPushButton(self.frame_7)
        self.btn_hideCoreRegs.setObjectName(u"btn_hideCoreRegs")
        self.btn_hideCoreRegs.setMinimumSize(QSize(0, 41))
        self.btn_hideCoreRegs.setStyleSheet(u"QPushButton{\n"
"margin-left: 10px; \n"
"    margin-right: 10px;\n"
"	background-color: rgb(40, 44, 52);\n"
" border: 2px solid rgb(52, 59, 72);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;	\n"
"text-align: center;\n"
"padding: 0px;\n"
"margin: 0px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color: rgb(28, 28, 28);\n"
"background-color: rgb(153, 193, 241);\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	\n"
"		color: rgb(28, 28, 28);\n"
"	background-color: rgb(110,140,255);\n"
"}")

        self.verticalLayout_32.addWidget(self.btn_hideCoreRegs)


        self.horizontalLayout_14.addWidget(self.frame_7)

        self.frame_9 = QFrame(self.frame_8)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.frame_9)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.symbols_frame = QFrame(self.frame_9)
        self.symbols_frame.setObjectName(u"symbols_frame")
        self.symbols_frame.setStyleSheet(u" border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"")
        self.symbols_frame.setFrameShape(QFrame.StyledPanel)
        self.symbols_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.symbols_frame)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.tbl_vars = QTableWidget(self.symbols_frame)
        if (self.tbl_vars.columnCount() < 3):
            self.tbl_vars.setColumnCount(3)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tbl_vars.setHorizontalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tbl_vars.setHorizontalHeaderItem(1, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tbl_vars.setHorizontalHeaderItem(2, __qtablewidgetitem4)
        self.tbl_vars.setObjectName(u"tbl_vars")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.tbl_vars.sizePolicy().hasHeightForWidth())
        self.tbl_vars.setSizePolicy(sizePolicy2)
        palette = QPalette()
        brush = QBrush(QColor(221, 221, 221, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 0))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        brush2 = QBrush(QColor(0, 0, 0, 255))
        brush2.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush2)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        brush3 = QBrush(QColor(0, 0, 0, 255))
        brush3.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        brush4 = QBrush(QColor(0, 0, 0, 255))
        brush4.setStyle(Qt.NoBrush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush)
#endif
        self.tbl_vars.setPalette(palette)
        self.tbl_vars.setStyleSheet(u" border: 0px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"")
        self.tbl_vars.setFrameShape(QFrame.NoFrame)
        self.tbl_vars.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.tbl_vars.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tbl_vars.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tbl_vars.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tbl_vars.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tbl_vars.setShowGrid(True)
        self.tbl_vars.setGridStyle(Qt.SolidLine)
        self.tbl_vars.setSortingEnabled(True)
        self.tbl_vars.horizontalHeader().setVisible(False)
        self.tbl_vars.horizontalHeader().setCascadingSectionResizes(False)
        self.tbl_vars.horizontalHeader().setDefaultSectionSize(120)
        self.tbl_vars.horizontalHeader().setHighlightSections(True)
        self.tbl_vars.horizontalHeader().setProperty("showSortIndicator", True)
        self.tbl_vars.horizontalHeader().setStretchLastSection(False)
        self.tbl_vars.verticalHeader().setVisible(False)
        self.tbl_vars.verticalHeader().setCascadingSectionResizes(False)
        self.tbl_vars.verticalHeader().setHighlightSections(False)
        self.tbl_vars.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_30.addWidget(self.tbl_vars)


        self.verticalLayout_33.addWidget(self.symbols_frame)

        self.watched_frame = QFrame(self.frame_9)
        self.watched_frame.setObjectName(u"watched_frame")
        self.watched_frame.setStyleSheet(u" border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"")
        self.watched_frame.setFrameShape(QFrame.StyledPanel)
        self.watched_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.watched_frame)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.tbl_vars_watched = QTableWidget(self.watched_frame)
        if (self.tbl_vars_watched.columnCount() < 5):
            self.tbl_vars_watched.setColumnCount(5)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tbl_vars_watched.setHorizontalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tbl_vars_watched.setHorizontalHeaderItem(1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tbl_vars_watched.setHorizontalHeaderItem(2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tbl_vars_watched.setHorizontalHeaderItem(3, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tbl_vars_watched.setHorizontalHeaderItem(4, __qtablewidgetitem9)
        self.tbl_vars_watched.setObjectName(u"tbl_vars_watched")
        self.tbl_vars_watched.setStyleSheet(u" border: 0px solid rgb(52, 59, 72);\n"
"	border-radius:0px;	\n"
"\n"
"")
        self.tbl_vars_watched.setSortingEnabled(False)
        self.tbl_vars_watched.horizontalHeader().setVisible(False)
        self.tbl_vars_watched.horizontalHeader().setCascadingSectionResizes(True)
        self.tbl_vars_watched.horizontalHeader().setDefaultSectionSize(120)
        self.tbl_vars_watched.verticalHeader().setVisible(False)

        self.horizontalLayout_13.addWidget(self.tbl_vars_watched)


        self.verticalLayout_33.addWidget(self.watched_frame)

        self.verticalLayout_33.setStretch(0, 1)
        self.verticalLayout_33.setStretch(1, 1)

        self.horizontalLayout_14.addWidget(self.frame_9)

        self.insights_graphing_frame = QFrame(self.frame_8)
        self.insights_graphing_frame.setObjectName(u"insights_graphing_frame")
        self.insights_graphing_frame.setMinimumSize(QSize(300, 0))
        self.insights_graphing_frame.setFrameShape(QFrame.StyledPanel)
        self.insights_graphing_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_37 = QVBoxLayout(self.insights_graphing_frame)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_37.setContentsMargins(-1, 0, -1, -1)
        self.stats_frame = QFrame(self.insights_graphing_frame)
        self.stats_frame.setObjectName(u"stats_frame")
        self.stats_frame.setMinimumSize(QSize(0, 250))
        self.stats_frame.setStyleSheet(u"border: 2px solid rgb(52, 59, 72);\n"
"border-radius: 5px;	\n"
"")
        self.stats_frame.setFrameShape(QFrame.StyledPanel)
        self.stats_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_39 = QVBoxLayout(self.stats_frame)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.verticalLayout_39.setContentsMargins(9, 0, -1, -1)
        self.frame_4 = QFrame(self.stats_frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u" border: 0px solid rgb(52, 59, 72);")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.titleLeftApp_2 = QLabel(self.frame_4)
        self.titleLeftApp_2.setObjectName(u"titleLeftApp_2")
        self.titleLeftApp_2.setGeometry(QRect(10, 10, 160, 20))
        self.titleLeftApp_2.setFont(font2)
        self.titleLeftApp_2.setStyleSheet(u" border: 0px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"")
        self.titleLeftApp_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_39.addWidget(self.frame_4)

        self.frame_15 = QFrame(self.stats_frame)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setStyleSheet(u" border: 0px solid rgb(52, 59, 72);")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_40 = QVBoxLayout(self.frame_15)
        self.verticalLayout_40.setSpacing(10)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.lbl_rx_data_count = QLabel(self.frame_15)
        self.lbl_rx_data_count.setObjectName(u"lbl_rx_data_count")

        self.verticalLayout_40.addWidget(self.lbl_rx_data_count)

        self.lbl_rx_data_crc_err = QLabel(self.frame_15)
        self.lbl_rx_data_crc_err.setObjectName(u"lbl_rx_data_crc_err")

        self.verticalLayout_40.addWidget(self.lbl_rx_data_crc_err)

        self.lbl_rx_data_timeout = QLabel(self.frame_15)
        self.lbl_rx_data_timeout.setObjectName(u"lbl_rx_data_timeout")

        self.verticalLayout_40.addWidget(self.lbl_rx_data_timeout)

        self.lbl_tx_data_count = QLabel(self.frame_15)
        self.lbl_tx_data_count.setObjectName(u"lbl_tx_data_count")

        self.verticalLayout_40.addWidget(self.lbl_tx_data_count)

        self.lbl_tx_data_err = QLabel(self.frame_15)
        self.lbl_tx_data_err.setObjectName(u"lbl_tx_data_err")

        self.verticalLayout_40.addWidget(self.lbl_tx_data_err)

        self.lbl_PER = QLabel(self.frame_15)
        self.lbl_PER.setObjectName(u"lbl_PER")
        self.lbl_PER.setStyleSheet(u"")

        self.verticalLayout_40.addWidget(self.lbl_PER)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_40.addItem(self.verticalSpacer_5)


        self.verticalLayout_39.addWidget(self.frame_15)

        self.verticalLayout_39.setStretch(0, 1)
        self.verticalLayout_39.setStretch(1, 8)

        self.verticalLayout_37.addWidget(self.stats_frame)

        self.insights_scroll_area = QScrollArea(self.insights_graphing_frame)
        self.insights_scroll_area.setObjectName(u"insights_scroll_area")
        self.insights_scroll_area.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 268, 16))
        self.insights_scroll_area.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_37.addWidget(self.insights_scroll_area)


        self.horizontalLayout_14.addWidget(self.insights_graphing_frame)

        self.horizontalLayout_14.setStretch(0, 2)
        self.horizontalLayout_14.setStretch(1, 4)
        self.horizontalLayout_14.setStretch(2, 5)

        self.horizontalLayout_17.addWidget(self.frame_8)

        self.stackedWidget.addWidget(self.insights)
        self.connections_page = QWidget()
        self.connections_page.setObjectName(u"connections_page")
        self.verticalLayout_20 = QVBoxLayout(self.connections_page)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.connections_main_frame = QFrame(self.connections_page)
        self.connections_main_frame.setObjectName(u"connections_main_frame")
        self.connections_main_frame.setFrameShape(QFrame.StyledPanel)
        self.connections_main_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.connections_main_frame)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(-1, 0, -1, 0)
        self.frame_10 = QFrame(self.connections_main_frame)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_35 = QVBoxLayout(self.frame_10)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(-1, 0, 0, -1)
        self.gatt_tree_frame = QFrame(self.frame_10)
        self.gatt_tree_frame.setObjectName(u"gatt_tree_frame")
        self.gatt_tree_frame.setStyleSheet(u" border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"")
        self.gatt_tree_frame.setFrameShape(QFrame.StyledPanel)
        self.gatt_tree_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.gatt_tree_frame)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.gatt_treeView = QTreeWidget(self.gatt_tree_frame)
        self.gatt_treeView.setObjectName(u"gatt_treeView")
        self.gatt_treeView.setFont(font2)
        self.gatt_treeView.setStyleSheet(u" border: 0px solid rgb(52, 59, 72);\n"
"	border-radius: 0px;	\n"
"")
        self.gatt_treeView.header().setVisible(False)

        self.verticalLayout_27.addWidget(self.gatt_treeView)


        self.verticalLayout_35.addWidget(self.gatt_tree_frame)

        self.frame_11 = QFrame(self.frame_10)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_34 = QVBoxLayout(self.frame_11)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(0, 9, 0, -1)
        self.btn_disconnect = QPushButton(self.frame_11)
        self.btn_disconnect.setObjectName(u"btn_disconnect")
        self.btn_disconnect.setMinimumSize(QSize(0, 50))
        self.btn_disconnect.setStyleSheet(u"QPushButton{\n"
"margin-left: 10px; \n"
"    margin-right: 10px;\n"
"	background-color: rgb(40, 44, 52);\n"
" border: 2px solid rgb(52, 59, 72);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 5px;	\n"
"text-align: center;\n"
"padding: 0px;\n"
"margin: 0px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color: rgb(28, 28, 28);\n"
"background-color: rgb(153, 193, 241);\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	\n"
"		color: rgb(28, 28, 28);\n"
"	background-color: rgb(110,140,255);\n"
"}")

        self.verticalLayout_34.addWidget(self.btn_disconnect)


        self.verticalLayout_35.addWidget(self.frame_11)


        self.horizontalLayout_18.addWidget(self.frame_10)

        self.scroll_Area_2_frame = QFrame(self.connections_main_frame)
        self.scroll_Area_2_frame.setObjectName(u"scroll_Area_2_frame")
        self.scroll_Area_2_frame.setStyleSheet(u" border: 0px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"")
        self.scroll_Area_2_frame.setFrameShape(QFrame.StyledPanel)
        self.scroll_Area_2_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.scroll_Area_2_frame)
        self.verticalLayout_28.setSpacing(15)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 9)
        self.scrollArea_2 = QScrollArea(self.scroll_Area_2_frame)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.scrollArea_2.sizePolicy().hasHeightForWidth())
        self.scrollArea_2.setSizePolicy(sizePolicy3)
        self.scrollArea_2.setStyleSheet(u"\n"
" border: 0px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"")
        self.scrollArea_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 18, 16))
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_28.addWidget(self.scrollArea_2)

        self.verticalLayout_28.setStretch(0, 2)

        self.horizontalLayout_18.addWidget(self.scroll_Area_2_frame)

        self.horizontalLayout_18.setStretch(0, 3)
        self.horizontalLayout_18.setStretch(1, 5)

        self.verticalLayout_20.addWidget(self.connections_main_frame)

        self.stackedWidget.addWidget(self.connections_page)

        self.verticalLayout_5.addWidget(self.stackedWidget)

        self.console_splitter.addWidget(self.frame_main_middle_content)
        self.frame_logging = QFrame(self.console_splitter)
        self.frame_logging.setObjectName(u"frame_logging")
        self.frame_logging.setMinimumSize(QSize(0, 120))
        self.frame_logging.setStyleSheet(u"background-color: #464E69;\n"
"")
        self.frame_logging.setFrameShape(QFrame.StyledPanel)
        self.frame_logging.setFrameShadow(QFrame.Raised)
        self.console_splitter.addWidget(self.frame_logging)

        self.verticalLayout_2.addWidget(self.console_splitter)


        self.horizontalLayout.addWidget(self.frame_main_middle_2)

        self.frame_main_right = QFrame(self.frame_main_middle)
        self.frame_main_right.setObjectName(u"frame_main_right")
        self.frame_main_right.setStyleSheet(u"background-color: #EBEBEF;")
        self.frame_main_right.setFrameShape(QFrame.StyledPanel)
        self.frame_main_right.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.frame_main_right)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 5)
        self.horizontalLayout.setStretch(2, 1)

        self.verticalLayout.addWidget(self.frame_main_middle)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 10)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)
        self.rssi_gatt_expolrer.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"GATT Explorer", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"gatt explorer", None))
        self.topLeftLogoLabel.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"|", None))
        self.txt_scan_filter_2.setText("")
        self.txt_scan_filter_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"filter scan results", None))
        self.btn_scan_2.setText(QCoreApplication.translate("MainWindow", u"Scan", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.btn_connect.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"GATT view:", None))
        self.labelBoxBlenderInstalation.setText(QCoreApplication.translate("MainWindow", u"FILE BOX", None))
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type here", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.labelVersion_3.setText(QCoreApplication.translate("MainWindow", u"Label description", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Test 1", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Test 2", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Test 3", None))

        self.commandLinkButton.setText(QCoreApplication.translate("MainWindow", u"Link Button", None))
        self.commandLinkButton.setDescription(QCoreApplication.translate("MainWindow", u"Link description", None))
        ___qtablewidgetitem = self.tbl_core_regs.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Reg", None));
        ___qtablewidgetitem1 = self.tbl_core_regs.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Value", None));
        self.btn_refreshCoreRegs.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.btn_hideCoreRegs.setText(QCoreApplication.translate("MainWindow", u"Hide", None))
        ___qtablewidgetitem2 = self.tbl_vars.horizontalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Variable", None));
        ___qtablewidgetitem3 = self.tbl_vars.horizontalHeaderItem(1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Address", None));
        ___qtablewidgetitem4 = self.tbl_vars.horizontalHeaderItem(2)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Watch", None));
        ___qtablewidgetitem5 = self.tbl_vars_watched.horizontalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem6 = self.tbl_vars_watched.horizontalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Value", None));
        self.titleLeftApp_2.setText(QCoreApplication.translate("MainWindow", u"Connection stats", None))
        self.lbl_rx_data_count.setText(QCoreApplication.translate("MainWindow", u"RX Data Count:", None))
        self.lbl_rx_data_crc_err.setText(QCoreApplication.translate("MainWindow", u"RX Data CRC ERR:", None))
        self.lbl_rx_data_timeout.setText(QCoreApplication.translate("MainWindow", u"RX Data Timeout:", None))
        self.lbl_tx_data_count.setText(QCoreApplication.translate("MainWindow", u"TX Data Count:", None))
        self.lbl_tx_data_err.setText(QCoreApplication.translate("MainWindow", u"TX Data ERR:", None))
        self.lbl_PER.setText(QCoreApplication.translate("MainWindow", u"PER : ", None))
        ___qtreewidgetitem = self.gatt_treeView.headerItem()
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"Gatt Tree", None));
        self.btn_disconnect.setText(QCoreApplication.translate("MainWindow", u"Disconnect", None))
    # retranslateUi

