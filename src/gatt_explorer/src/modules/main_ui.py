# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_ui_stripped.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QMainWindow, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QSplitter, QStackedWidget,
    QTableWidget, QTableWidgetItem, QTextEdit, QTreeWidget,
    QTreeWidgetItem, QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1274, 687)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_main_top_bar = QFrame(self.centralwidget)
        self.frame_main_top_bar.setObjectName(u"frame_main_top_bar")
        self.frame_main_top_bar.setMinimumSize(QSize(0, 53))
        self.frame_main_top_bar.setMaximumSize(QSize(16777215, 53))
        self.frame_main_top_bar.setFrameShape(QFrame.StyledPanel)
        self.frame_main_top_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_main_top_bar)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.topLeftLogo = QFrame(self.frame_main_top_bar)
        self.topLeftLogo.setObjectName(u"topLeftLogo")
        self.topLeftLogo.setMinimumSize(QSize(140, 60))
        self.topLeftLogo.setMaximumSize(QSize(140, 16777215))
        self.topLeftLogo.setFrameShape(QFrame.StyledPanel)
        self.topLeftLogo.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.topLeftLogo)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.topLeftLogoLabel = QLabel(self.topLeftLogo)
        self.topLeftLogoLabel.setObjectName(u"topLeftLogoLabel")
        self.topLeftLogoLabel.setMinimumSize(QSize(140, 60))
        self.topLeftLogoLabel.setMaximumSize(QSize(140, 16777215))

        self.verticalLayout_3.addWidget(self.topLeftLogoLabel)


        self.horizontalLayout_2.addWidget(self.topLeftLogo)

        self.logo_divider_line = QLabel(self.frame_main_top_bar)
        self.logo_divider_line.setObjectName(u"logo_divider_line")
        font = QFont()
        font.setFamilies([u"Umpush"])
        font.setPointSize(31)
        self.logo_divider_line.setFont(font)

        self.horizontalLayout_2.addWidget(self.logo_divider_line)

        self.label_gatt_explorer = QLabel(self.frame_main_top_bar)
        self.label_gatt_explorer.setObjectName(u"label_gatt_explorer")
        font1 = QFont()
        font1.setPointSize(12)
        self.label_gatt_explorer.setFont(font1)

        self.horizontalLayout_2.addWidget(self.label_gatt_explorer)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.btn_theme = QPushButton(self.frame_main_top_bar)
        self.btn_theme.setObjectName(u"btn_theme")
        self.btn_theme.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_2.addWidget(self.btn_theme)

        self.btn_menu = QPushButton(self.frame_main_top_bar)
        self.btn_menu.setObjectName(u"btn_menu")
        self.btn_menu.setMinimumSize(QSize(28, 28))
        self.btn_menu.setMaximumSize(QSize(28, 28))
        self.btn_menu.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/icon_settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_menu.setIcon(icon)
        self.btn_menu.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.btn_menu)


        self.verticalLayout.addWidget(self.frame_main_top_bar)

        self.frame_main_middle = QFrame(self.centralwidget)
        self.frame_main_middle.setObjectName(u"frame_main_middle")
        self.frame_main_middle.setFrameShape(QFrame.StyledPanel)
        self.frame_main_middle.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_main_middle)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 3, 0, 0)
        self.frame_main_left = QFrame(self.frame_main_middle)
        self.frame_main_left.setObjectName(u"frame_main_left")
        self.frame_main_left.setMinimumSize(QSize(165, 0))
        self.frame_main_left.setMaximumSize(QSize(165, 16777215))
        self.frame_main_left.setFrameShape(QFrame.StyledPanel)
        self.frame_main_left.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.frame_main_left)

        self.frame_main_middle_2 = QFrame(self.frame_main_middle)
        self.frame_main_middle_2.setObjectName(u"frame_main_middle_2")
        self.frame_main_middle_2.setFrameShape(QFrame.StyledPanel)
        self.frame_main_middle_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_main_middle_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 9)
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
        self.frame_main_middle_content.setFrameShape(QFrame.StyledPanel)
        self.frame_main_middle_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_main_middle_content)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.stackedWidget = QStackedWidget(self.frame_main_middle_content)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.verticalLayout_22 = QVBoxLayout(self.home)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.frame_explorer_top = QFrame(self.home)
        self.frame_explorer_top.setObjectName(u"frame_explorer_top")
        self.frame_explorer_top.setFrameShape(QFrame.StyledPanel)
        self.frame_explorer_top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_explorer_top)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, -1, -1, -1)
        self.frame_scan_results = QFrame(self.frame_explorer_top)
        self.frame_scan_results.setObjectName(u"frame_scan_results")
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

        self.horizontalLayout_7.addWidget(self.txt_scan_filter_2)


        self.verticalLayout_24.addWidget(self.frame_3)

        self.list_widget_discovered = QListWidget(self.frame_scan_results)
        QListWidgetItem(self.list_widget_discovered)
        QListWidgetItem(self.list_widget_discovered)
        QListWidgetItem(self.list_widget_discovered)
        QListWidgetItem(self.list_widget_discovered)
        self.list_widget_discovered.setObjectName(u"list_widget_discovered")
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(10)
        font2.setBold(False)
        font2.setItalic(False)
        self.list_widget_discovered.setFont(font2)
        self.list_widget_discovered.setSelectionMode(QAbstractItemView.SingleSelection)

        self.verticalLayout_24.addWidget(self.list_widget_discovered)

        self.frame_12 = QFrame(self.frame_scan_results)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMinimumSize(QSize(0, 0))
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 6, 0, -1)
        self.btn_scan = QPushButton(self.frame_12)
        self.btn_scan.setObjectName(u"btn_scan")
        self.btn_scan.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_19.addWidget(self.btn_scan)

        self.btn_connect = QPushButton(self.frame_12)
        self.btn_connect.setObjectName(u"btn_connect")
        self.btn_connect.setMinimumSize(QSize(0, 30))

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
        self.table_adv_data = QTableWidget(self.frame_adv_data)
        if (self.table_adv_data.columnCount() < 3):
            self.table_adv_data.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.table_adv_data.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_adv_data.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table_adv_data.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        if (self.table_adv_data.rowCount() < 3):
            self.table_adv_data.setRowCount(3)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table_adv_data.setVerticalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.table_adv_data.setVerticalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.table_adv_data.setVerticalHeaderItem(2, __qtablewidgetitem5)
        self.table_adv_data.setObjectName(u"table_adv_data")
        self.table_adv_data.horizontalHeader().setVisible(False)
        self.table_adv_data.verticalHeader().setVisible(False)

        self.verticalLayout_21.addWidget(self.table_adv_data)

        self.verticalLayout_21.setStretch(0, 7)

        self.verticalLayout_22.addWidget(self.frame_adv_data)

        self.verticalLayout_22.setStretch(0, 3)
        self.verticalLayout_22.setStretch(1, 3)
        self.stackedWidget.addWidget(self.home)
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
        self.gatt_tree_frame.setFrameShape(QFrame.StyledPanel)
        self.gatt_tree_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.gatt_tree_frame)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.gatt_treeView = QTreeWidget(self.gatt_tree_frame)
        self.gatt_treeView.setObjectName(u"gatt_treeView")
        self.gatt_treeView.setFont(font2)
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

        self.verticalLayout_34.addWidget(self.btn_disconnect)


        self.verticalLayout_35.addWidget(self.frame_11)


        self.horizontalLayout_18.addWidget(self.frame_10)

        self.scroll_Area_2_frame = QFrame(self.connections_main_frame)
        self.scroll_Area_2_frame.setObjectName(u"scroll_Area_2_frame")
        self.scroll_Area_2_frame.setFrameShape(QFrame.StyledPanel)
        self.scroll_Area_2_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.scroll_Area_2_frame)
        self.verticalLayout_28.setSpacing(15)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 9)
        self.scrollArea_2 = QScrollArea(self.scroll_Area_2_frame)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.scrollArea_2.sizePolicy().hasHeightForWidth())
        self.scrollArea_2.setSizePolicy(sizePolicy1)
        self.scrollArea_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 86, 30))
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
        self.frame_logging.setFrameShape(QFrame.StyledPanel)
        self.frame_logging.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_logging)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.console = QTextEdit(self.frame_logging)
        self.console.setObjectName(u"console")

        self.horizontalLayout_3.addWidget(self.console)

        self.console_splitter.addWidget(self.frame_logging)

        self.verticalLayout_2.addWidget(self.console_splitter)


        self.horizontalLayout.addWidget(self.frame_main_middle_2)

        self.frame_main_right = QFrame(self.frame_main_middle)
        self.frame_main_right.setObjectName(u"frame_main_right")
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
        self.rssi_gatt_expolrer.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"GATT Explorer", None))
        self.topLeftLogoLabel.setText("")
        self.logo_divider_line.setText(QCoreApplication.translate("MainWindow", u"|", None))
        self.label_gatt_explorer.setText(QCoreApplication.translate("MainWindow", u"gatt explorer", None))
        self.btn_theme.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
#if QT_CONFIG(tooltip)
        self.btn_menu.setToolTip(QCoreApplication.translate("MainWindow", u"Settings", None))
#endif // QT_CONFIG(tooltip)
        self.btn_menu.setText("")
        self.txt_scan_filter_2.setText("")
        self.txt_scan_filter_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"filter scan results", None))

        __sortingEnabled = self.list_widget_discovered.isSortingEnabled()
        self.list_widget_discovered.setSortingEnabled(False)
        ___qlistwidgetitem = self.list_widget_discovered.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"New Item", None));
        ___qlistwidgetitem1 = self.list_widget_discovered.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"New Item", None));
        ___qlistwidgetitem2 = self.list_widget_discovered.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"New Item", None));
        ___qlistwidgetitem3 = self.list_widget_discovered.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("MainWindow", u"New Item", None));
        self.list_widget_discovered.setSortingEnabled(__sortingEnabled)

        self.btn_scan.setText(QCoreApplication.translate("MainWindow", u"Scan", None))
        self.btn_connect.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        ___qtablewidgetitem = self.table_adv_data.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem1 = self.table_adv_data.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem2 = self.table_adv_data.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem3 = self.table_adv_data.verticalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem4 = self.table_adv_data.verticalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem5 = self.table_adv_data.verticalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtreewidgetitem = self.gatt_treeView.headerItem()
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"Gatt Tree", None));
        self.btn_disconnect.setText(QCoreApplication.translate("MainWindow", u"Disconnect", None))
    # retranslateUi

