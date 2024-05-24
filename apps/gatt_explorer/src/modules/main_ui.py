# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_ui_stripped.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
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
    QAbstractItemView,
    QApplication,
    QCheckBox,
    QFrame,
    QHBoxLayout,
    QHeaderView,
    QLabel,
    QLineEdit,
    QListWidget,
    QListWidgetItem,
    QMainWindow,
    QPushButton,
    QRadioButton,
    QScrollArea,
    QSizePolicy,
    QSlider,
    QSpacerItem,
    QSplitter,
    QStackedWidget,
    QTableWidget,
    QTableWidgetItem,
    QTextEdit,
    QTreeWidget,
    QTreeWidgetItem,
    QVBoxLayout,
    QWidget,
)

from custom_widgets.toggle import AnimatedToggle
import resources_rc


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1302, 743)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_main_top_bar = QFrame(self.centralwidget)
        self.frame_main_top_bar.setObjectName("frame_main_top_bar")
        self.frame_main_top_bar.setMinimumSize(QSize(0, 53))
        self.frame_main_top_bar.setMaximumSize(QSize(16777215, 53))
        self.frame_main_top_bar.setFrameShape(QFrame.StyledPanel)
        self.frame_main_top_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_main_top_bar)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.topLeftLogo = QFrame(self.frame_main_top_bar)
        self.topLeftLogo.setObjectName("topLeftLogo")
        self.topLeftLogo.setMinimumSize(QSize(140, 60))
        self.topLeftLogo.setMaximumSize(QSize(140, 16777215))
        self.topLeftLogo.setFrameShape(QFrame.StyledPanel)
        self.topLeftLogo.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.topLeftLogo)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.topLeftLogoLabel = QLabel(self.topLeftLogo)
        self.topLeftLogoLabel.setObjectName("topLeftLogoLabel")
        self.topLeftLogoLabel.setMinimumSize(QSize(140, 60))
        self.topLeftLogoLabel.setMaximumSize(QSize(140, 16777215))

        self.verticalLayout_3.addWidget(self.topLeftLogoLabel)

        self.horizontalLayout_2.addWidget(self.topLeftLogo)

        self.logo_divider_line = QLabel(self.frame_main_top_bar)
        self.logo_divider_line.setObjectName("logo_divider_line")
        font = QFont()
        font.setFamilies(["Umpush"])
        font.setPointSize(31)
        self.logo_divider_line.setFont(font)

        self.horizontalLayout_2.addWidget(self.logo_divider_line)

        self.label_gatt_explorer = QLabel(self.frame_main_top_bar)
        self.label_gatt_explorer.setObjectName("label_gatt_explorer")
        font1 = QFont()
        font1.setPointSize(12)
        self.label_gatt_explorer.setFont(font1)

        self.horizontalLayout_2.addWidget(self.label_gatt_explorer)

        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.btn_theme = QPushButton(self.frame_main_top_bar)
        self.btn_theme.setObjectName("btn_theme")
        self.btn_theme.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_2.addWidget(self.btn_theme)

        self.btn_menu = QPushButton(self.frame_main_top_bar)
        self.btn_menu.setObjectName("btn_menu")
        self.btn_menu.setMinimumSize(QSize(28, 28))
        self.btn_menu.setMaximumSize(QSize(28, 28))
        self.btn_menu.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(
            ":/icons/images/icons/icon_settings.png", QSize(), QIcon.Normal, QIcon.Off
        )
        self.btn_menu.setIcon(icon)
        self.btn_menu.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.btn_menu)

        self.verticalLayout.addWidget(self.frame_main_top_bar)

        self.frame_main_middle = QFrame(self.centralwidget)
        self.frame_main_middle.setObjectName("frame_main_middle")
        self.frame_main_middle.setFrameShape(QFrame.StyledPanel)
        self.frame_main_middle.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_main_middle)
        self.horizontalLayout.setSpacing(9)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 3, 0, 0)
        self.frame_main_left = QFrame(self.frame_main_middle)
        self.frame_main_left.setObjectName("frame_main_left")
        self.frame_main_left.setMinimumSize(QSize(165, 0))
        self.frame_main_left.setMaximumSize(QSize(165, 16777215))
        self.frame_main_left.setFrameShape(QFrame.StyledPanel)
        self.frame_main_left.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.frame_main_left)

        self.frame_main_middle_2 = QFrame(self.frame_main_middle)
        self.frame_main_middle_2.setObjectName("frame_main_middle_2")
        self.frame_main_middle_2.setFrameShape(QFrame.StyledPanel)
        self.frame_main_middle_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_main_middle_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 9)
        self.console_splitter = QSplitter(self.frame_main_middle_2)
        self.console_splitter.setObjectName("console_splitter")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.console_splitter.sizePolicy().hasHeightForWidth()
        )
        self.console_splitter.setSizePolicy(sizePolicy)
        self.console_splitter.setBaseSize(QSize(0, 0))
        self.console_splitter.setFrameShape(QFrame.NoFrame)
        self.console_splitter.setLineWidth(1)
        self.console_splitter.setMidLineWidth(0)
        self.console_splitter.setOrientation(Qt.Vertical)
        self.console_splitter.setOpaqueResize(True)
        self.console_splitter.setHandleWidth(10)
        self.console_splitter.setChildrenCollapsible(True)
        self.frame_main_middle_content = QFrame(self.console_splitter)
        self.frame_main_middle_content.setObjectName("frame_main_middle_content")
        self.frame_main_middle_content.setMinimumSize(QSize(0, 300))
        self.frame_main_middle_content.setFrameShape(QFrame.StyledPanel)
        self.frame_main_middle_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_main_middle_content)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, -1)
        self.stackedWidget = QStackedWidget(self.frame_main_middle_content)
        self.stackedWidget.setObjectName("stackedWidget")
        self.home = QWidget()
        self.home.setObjectName("home")
        self.verticalLayout_22 = QVBoxLayout(self.home)
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.frame_explorer_top = QFrame(self.home)
        self.frame_explorer_top.setObjectName("frame_explorer_top")
        self.frame_explorer_top.setFrameShape(QFrame.StyledPanel)
        self.frame_explorer_top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_explorer_top)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, -1, -1, -1)
        self.frame_scan_results = QFrame(self.frame_explorer_top)
        self.frame_scan_results.setObjectName("frame_scan_results")
        self.frame_scan_results.setFrameShape(QFrame.StyledPanel)
        self.frame_scan_results.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_scan_results)
        self.verticalLayout_24.setSpacing(6)
        self.verticalLayout_24.setObjectName("verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, -1, 0)
        self.frame_3 = QFrame(self.frame_scan_results)
        self.frame_3.setObjectName("frame_3")
        self.frame_3.setMinimumSize(QSize(0, 40))
        self.frame_3.setMaximumSize(QSize(16777215, 40))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, -1)
        self.txt_scan_filter = QLineEdit(self.frame_3)
        self.txt_scan_filter.setObjectName("txt_scan_filter")
        self.txt_scan_filter.setMinimumSize(QSize(0, 30))
        self.txt_scan_filter.setMaximumSize(QSize(16777215, 35))

        self.horizontalLayout_7.addWidget(self.txt_scan_filter)

        self.verticalLayout_24.addWidget(self.frame_3)

        self.list_widget_discovered = QListWidget(self.frame_scan_results)
        self.list_widget_discovered.setObjectName("list_widget_discovered")
        font2 = QFont()
        font2.setFamilies(["Segoe UI"])
        font2.setPointSize(10)
        font2.setBold(False)
        font2.setItalic(False)
        self.list_widget_discovered.setFont(font2)
        self.list_widget_discovered.setSelectionMode(QAbstractItemView.SingleSelection)

        self.verticalLayout_24.addWidget(self.list_widget_discovered)

        self.frame_12 = QFrame(self.frame_scan_results)
        self.frame_12.setObjectName("frame_12")
        self.frame_12.setMinimumSize(QSize(0, 0))
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 6, 0, -1)
        self.btn_scan = QPushButton(self.frame_12)
        self.btn_scan.setObjectName("btn_scan")
        self.btn_scan.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_19.addWidget(self.btn_scan)

        self.btn_connect = QPushButton(self.frame_12)
        self.btn_connect.setObjectName("btn_connect")
        self.btn_connect.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_19.addWidget(self.btn_connect)

        self.verticalLayout_24.addWidget(self.frame_12)

        self.horizontalLayout_8.addWidget(self.frame_scan_results)

        self.frame_2 = QFrame(self.frame_explorer_top)
        self.frame_2.setObjectName("frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_8.addWidget(self.frame_2)

        self.horizontalLayout_8.setStretch(0, 2)
        self.horizontalLayout_8.setStretch(1, 2)

        self.verticalLayout_22.addWidget(self.frame_explorer_top)

        self.frame_adv_data = QFrame(self.home)
        self.frame_adv_data.setObjectName("frame_adv_data")
        self.frame_adv_data.setMinimumSize(QSize(0, 60))
        self.frame_adv_data.setFrameShape(QFrame.StyledPanel)
        self.frame_adv_data.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_adv_data)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.table_adv_data = QTableWidget(self.frame_adv_data)
        self.table_adv_data.setObjectName("table_adv_data")
        self.table_adv_data.setRowCount(0)
        self.table_adv_data.setColumnCount(0)
        self.table_adv_data.horizontalHeader().setVisible(False)
        self.table_adv_data.horizontalHeader().setStretchLastSection(True)
        self.table_adv_data.verticalHeader().setVisible(False)

        self.verticalLayout_21.addWidget(self.table_adv_data)

        self.verticalLayout_21.setStretch(0, 7)

        self.verticalLayout_22.addWidget(self.frame_adv_data)

        self.verticalLayout_22.setStretch(0, 3)
        self.verticalLayout_22.setStretch(1, 3)
        self.stackedWidget.addWidget(self.home)
        self.connections_page = QWidget()
        self.connections_page.setObjectName("connections_page")
        self.verticalLayout_20 = QVBoxLayout(self.connections_page)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.connections_main_frame = QFrame(self.connections_page)
        self.connections_main_frame.setObjectName("connections_main_frame")
        self.connections_main_frame.setFrameShape(QFrame.StyledPanel)
        self.connections_main_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.connections_main_frame)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(-1, 0, -1, 0)
        self.frame_10 = QFrame(self.connections_main_frame)
        self.frame_10.setObjectName("frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.verticalLayout_35 = QVBoxLayout(self.frame_10)
        self.verticalLayout_35.setObjectName("verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(-1, 0, 0, -1)
        self.gatt_tree_frame = QFrame(self.frame_10)
        self.gatt_tree_frame.setObjectName("gatt_tree_frame")
        self.gatt_tree_frame.setFrameShape(QFrame.StyledPanel)
        self.gatt_tree_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.gatt_tree_frame)
        self.verticalLayout_27.setObjectName("verticalLayout_27")
        self.gatt_treeView = QTreeWidget(self.gatt_tree_frame)
        self.gatt_treeView.setObjectName("gatt_treeView")
        self.gatt_treeView.setFont(font2)
        self.gatt_treeView.header().setVisible(False)

        self.verticalLayout_27.addWidget(self.gatt_treeView)

        self.verticalLayout_35.addWidget(self.gatt_tree_frame)

        self.frame_11 = QFrame(self.frame_10)
        self.frame_11.setObjectName("frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_34 = QVBoxLayout(self.frame_11)
        self.verticalLayout_34.setObjectName("verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(0, 9, 0, -1)
        self.btn_disconnect = QPushButton(self.frame_11)
        self.btn_disconnect.setObjectName("btn_disconnect")
        self.btn_disconnect.setMinimumSize(QSize(0, 50))

        self.verticalLayout_34.addWidget(self.btn_disconnect)

        self.verticalLayout_35.addWidget(self.frame_11)

        self.horizontalLayout_18.addWidget(self.frame_10)

        self.scroll_Area_2_frame = QFrame(self.connections_main_frame)
        self.scroll_Area_2_frame.setObjectName("scroll_Area_2_frame")
        self.scroll_Area_2_frame.setFrameShape(QFrame.StyledPanel)
        self.scroll_Area_2_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.scroll_Area_2_frame)
        self.verticalLayout_28.setSpacing(15)
        self.verticalLayout_28.setObjectName("verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 9)
        self.scrollArea_2 = QScrollArea(self.scroll_Area_2_frame)
        self.scrollArea_2.setObjectName("scrollArea_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(
            self.scrollArea_2.sizePolicy().hasHeightForWidth()
        )
        self.scrollArea_2.setSizePolicy(sizePolicy1)
        self.scrollArea_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
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
        self.frame_logging.setObjectName("frame_logging")
        self.frame_logging.setMinimumSize(QSize(0, 120))
        self.frame_logging.setFrameShape(QFrame.StyledPanel)
        self.frame_logging.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_logging)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.console = QTextEdit(self.frame_logging)
        self.console.setObjectName("console")

        self.horizontalLayout_3.addWidget(self.console)

        self.console_splitter.addWidget(self.frame_logging)

        self.verticalLayout_2.addWidget(self.console_splitter)

        self.horizontalLayout.addWidget(self.frame_main_middle_2)

        self.frame_main_right = QFrame(self.frame_main_middle)
        self.frame_main_right.setObjectName("frame_main_right")
        self.frame_main_right.setMinimumSize(QSize(0, 0))
        self.frame_main_right.setMaximumSize(QSize(0, 16777215))
        self.frame_main_right.setFrameShape(QFrame.StyledPanel)
        self.frame_main_right.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_main_right)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_scanner_settings = QFrame(self.frame_main_right)
        self.frame_scanner_settings.setObjectName("frame_scanner_settings")
        self.frame_scanner_settings.setMinimumSize(QSize(0, 0))
        self.frame_scanner_settings.setMaximumSize(QSize(16777215, 900))
        self.frame_scanner_settings.setFrameShape(QFrame.NoFrame)
        self.frame_scanner_settings.setFrameShadow(QFrame.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.frame_scanner_settings)
        self.verticalLayout_31.setSpacing(6)
        self.verticalLayout_31.setObjectName("verticalLayout_31")
        self.btn_save_logs = QPushButton(self.frame_scanner_settings)
        self.btn_save_logs.setObjectName("btn_save_logs")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(
            self.btn_save_logs.sizePolicy().hasHeightForWidth()
        )
        self.btn_save_logs.setSizePolicy(sizePolicy2)
        self.btn_save_logs.setMinimumSize(QSize(0, 45))
        self.btn_save_logs.setFont(font2)
        self.btn_save_logs.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_save_logs.setLayoutDirection(Qt.LeftToRight)

        self.verticalLayout_31.addWidget(self.btn_save_logs)

        self.btn_clear_logs = QPushButton(self.frame_scanner_settings)
        self.btn_clear_logs.setObjectName("btn_clear_logs")
        sizePolicy2.setHeightForWidth(
            self.btn_clear_logs.sizePolicy().hasHeightForWidth()
        )
        self.btn_clear_logs.setSizePolicy(sizePolicy2)
        self.btn_clear_logs.setMinimumSize(QSize(0, 45))
        self.btn_clear_logs.setFont(font2)
        self.btn_clear_logs.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_clear_logs.setLayoutDirection(Qt.LeftToRight)

        self.verticalLayout_31.addWidget(self.btn_clear_logs)

        self.frame_scan = QFrame(self.frame_scanner_settings)
        self.frame_scan.setObjectName("frame_scan")
        self.frame_scan.setEnabled(True)
        self.frame_scan.setFrameShape(QFrame.StyledPanel)
        self.frame_scan.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_scan)
        self.verticalLayout_23.setSpacing(10)
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(-1, 5, -1, 0)
        self.frame_scan_timeout = QFrame(self.frame_scan)
        self.frame_scan_timeout.setObjectName("frame_scan_timeout")
        self.frame_scan_timeout.setMinimumSize(QSize(0, 0))
        self.frame_scan_timeout.setMaximumSize(QSize(16777215, 20))
        self.frame_scan_timeout.setFrameShape(QFrame.StyledPanel)
        self.frame_scan_timeout.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_scan_timeout)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, -1, 0)
        self.label_scan_timeout = QLabel(self.frame_scan_timeout)
        self.label_scan_timeout.setObjectName("label_scan_timeout")
        self.label_scan_timeout.setMaximumSize(QSize(16777215, 20))

        self.horizontalLayout_6.addWidget(self.label_scan_timeout)

        self.label_scan_timeout_value = QLabel(self.frame_scan_timeout)
        self.label_scan_timeout_value.setObjectName("label_scan_timeout_value")
        self.label_scan_timeout_value.setMaximumSize(QSize(16777215, 20))
        self.label_scan_timeout_value.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_scan_timeout_value)

        self.verticalLayout_23.addWidget(self.frame_scan_timeout)

        self.scanSlider = QSlider(self.frame_scan)
        self.scanSlider.setObjectName("scanSlider")
        self.scanSlider.setMaximum(30)
        self.scanSlider.setPageStep(1)
        self.scanSlider.setValue(5)
        self.scanSlider.setOrientation(Qt.Horizontal)

        self.verticalLayout_23.addWidget(self.scanSlider)

        self.check_no_timeout = QCheckBox(self.frame_scan)
        self.check_no_timeout.setObjectName("check_no_timeout")
        self.check_no_timeout.setChecked(True)

        self.verticalLayout_23.addWidget(self.check_no_timeout)

        self.label_4 = QLabel(self.frame_scan)
        self.label_4.setObjectName("label_4")
        self.label_4.setMaximumSize(QSize(16777215, 20))
        font3 = QFont()
        font3.setFamilies(["Segoe UI"])
        font3.setPointSize(11)
        font3.setBold(False)
        font3.setItalic(False)
        self.label_4.setFont(font3)

        self.verticalLayout_23.addWidget(self.label_4)

        self.logSelection = QRadioButton(self.frame_scan)
        self.logSelection.setObjectName("logSelection")

        self.verticalLayout_23.addWidget(self.logSelection)

        self.logAll = QRadioButton(self.frame_scan)
        self.logAll.setObjectName("logAll")
        self.logAll.setChecked(True)

        self.verticalLayout_23.addWidget(self.logAll)

        self.logNone = QRadioButton(self.frame_scan)
        self.logNone.setObjectName("logNone")
        self.logNone.setChecked(False)

        self.verticalLayout_23.addWidget(self.logNone)

        self.frame = QFrame(self.frame_scan)
        self.frame.setObjectName("frame")
        self.frame.setMinimumSize(QSize(0, 50))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName("label_5")

        self.horizontalLayout_10.addWidget(self.label_5)

        self.graph_enabled = AnimatedToggle(self.frame)
        self.graph_enabled.setObjectName("graph_enabled")
        self.graph_enabled.setMinimumSize(QSize(84, 0))
        self.graph_enabled.setMaximumSize(QSize(84, 999999))
        self.graph_enabled.setChecked(True)

        self.horizontalLayout_10.addWidget(self.graph_enabled)

        self.horizontalLayout_10.setStretch(0, 5)
        self.horizontalLayout_10.setStretch(1, 2)

        self.verticalLayout_23.addWidget(self.frame)

        self.options_frame = QFrame(self.frame_scan)
        self.options_frame.setObjectName("options_frame")
        self.options_frame.setMinimumSize(QSize(0, 40))
        self.options_frame.setMaximumSize(QSize(16777215, 45))
        self.options_frame.setFrameShape(QFrame.StyledPanel)
        self.options_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.options_frame)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, -1, -1, -1)
        self.check_scroll_to_bottom = QCheckBox(self.options_frame)
        self.check_scroll_to_bottom.setObjectName("check_scroll_to_bottom")
        self.check_scroll_to_bottom.setChecked(True)

        self.verticalLayout_14.addWidget(self.check_scroll_to_bottom)

        self.verticalLayout_23.addWidget(self.options_frame)

        self.verticalSpacer_2 = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout_23.addItem(self.verticalSpacer_2)

        self.verticalLayout_31.addWidget(self.frame_scan)

        self.verticalSpacer_3 = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout_31.addItem(self.verticalSpacer_3)

        self.verticalLayout_31.setStretch(0, 1)

        self.verticalLayout_4.addWidget(self.frame_scanner_settings)

        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding
        )

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.horizontalLayout.addWidget(self.frame_main_right)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 5)

        self.verticalLayout.addWidget(self.frame_main_middle)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 10)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.scanSlider.valueChanged.connect(self.label_scan_timeout_value.setNum)

        self.stackedWidget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "GATT Explorer", None)
        )
        self.topLeftLogoLabel.setText("")
        self.logo_divider_line.setText(
            QCoreApplication.translate("MainWindow", "|", None)
        )
        self.label_gatt_explorer.setText(
            QCoreApplication.translate("MainWindow", "gatt explorer", None)
        )
        self.btn_theme.setText(
            QCoreApplication.translate("MainWindow", "PushButton", None)
        )
        # if QT_CONFIG(tooltip)
        self.btn_menu.setToolTip(
            QCoreApplication.translate("MainWindow", "Settings", None)
        )
        # endif // QT_CONFIG(tooltip)
        self.btn_menu.setText("")
        self.txt_scan_filter.setText("")
        self.txt_scan_filter.setPlaceholderText(
            QCoreApplication.translate("MainWindow", "filter scan results", None)
        )
        self.btn_scan.setText(QCoreApplication.translate("MainWindow", "Scan", None))
        self.btn_connect.setText(
            QCoreApplication.translate("MainWindow", "Connect", None)
        )
        ___qtreewidgetitem = self.gatt_treeView.headerItem()
        ___qtreewidgetitem.setText(
            0, QCoreApplication.translate("MainWindow", "Gatt Tree", None)
        )
        self.btn_disconnect.setText(
            QCoreApplication.translate("MainWindow", "Disconnect", None)
        )
        self.btn_save_logs.setText(
            QCoreApplication.translate("MainWindow", "Save  logs", None)
        )
        self.btn_clear_logs.setText(
            QCoreApplication.translate("MainWindow", "Clear logs & graph", None)
        )
        self.label_scan_timeout.setText(
            QCoreApplication.translate("MainWindow", "Scan timeout (s):", None)
        )
        self.label_scan_timeout_value.setText(
            QCoreApplication.translate("MainWindow", "5", None)
        )
        self.check_no_timeout.setText(
            QCoreApplication.translate("MainWindow", "No timeout", None)
        )
        self.label_4.setText(
            QCoreApplication.translate("MainWindow", "Adv data logging :", None)
        )
        self.logSelection.setText(
            QCoreApplication.translate("MainWindow", "Selection", None)
        )
        self.logAll.setText(
            QCoreApplication.translate("MainWindow", "Log all data", None)
        )
        self.logNone.setText(
            QCoreApplication.translate("MainWindow", "Do not log", None)
        )
        self.label_5.setText(
            QCoreApplication.translate("MainWindow", "RSSI graph :", None)
        )
        self.graph_enabled.setText(
            QCoreApplication.translate("MainWindow", "CheckBox", None)
        )
        self.check_scroll_to_bottom.setText(
            QCoreApplication.translate("MainWindow", "Auto scroll table", None)
        )

    # retranslateUi
