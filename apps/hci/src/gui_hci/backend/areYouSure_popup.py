# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'areYouSure_popup_v3.ui'
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
    QFrame,
    QGridLayout,
    QLabel,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QStackedWidget,
    QWidget,
)


class Ui_areYouSure_popup(object):
    def setupUi(self, areYouSure_popupV3):
        if not areYouSure_popupV3.objectName():
            areYouSure_popupV3.setObjectName("areYouSure_popupV3")
        areYouSure_popupV3.setWindowModality(Qt.ApplicationModal)
        areYouSure_popupV3.resize(485, 120)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            areYouSure_popupV3.sizePolicy().hasHeightForWidth()
        )
        areYouSure_popupV3.setSizePolicy(sizePolicy)
        areYouSure_popupV3.setMinimumSize(QSize(485, 120))
        areYouSure_popupV3.setMaximumSize(QSize(485, 120))
        areYouSure_popupV3.setContextMenuPolicy(Qt.NoContextMenu)
        self.gridLayout = QGridLayout(areYouSure_popupV3)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.popupView = QStackedWidget(areYouSure_popupV3)
        self.popupView.setObjectName("popupView")
        self.saveNeededPage = QWidget()
        self.saveNeededPage.setObjectName("saveNeededPage")
        self.gridLayout_2 = QGridLayout(self.saveNeededPage)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame1 = QFrame(self.saveNeededPage)
        self.frame1.setObjectName("frame1")
        self.frame1.setContextMenuPolicy(Qt.NoContextMenu)
        self.frame1.setFrameShape(QFrame.StyledPanel)
        self.frame1.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame1)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_3.setContentsMargins(2, 2, 2, 2)
        self.saveNeeded_noSave = QPushButton(self.frame1)
        self.saveNeeded_noSave.setObjectName("saveNeeded_noSave")

        self.gridLayout_3.addWidget(self.saveNeeded_noSave, 2, 1, 1, 1)

        self.saveNeeded_cancel = QPushButton(self.frame1)
        self.saveNeeded_cancel.setObjectName("saveNeeded_cancel")

        self.gridLayout_3.addWidget(self.saveNeeded_cancel, 2, 2, 1, 1)

        self.saveNeeded_warningIcon = QLabel(self.frame1)
        self.saveNeeded_warningIcon.setObjectName("saveNeeded_warningIcon")
        sizePolicy.setHeightForWidth(
            self.saveNeeded_warningIcon.sizePolicy().hasHeightForWidth()
        )
        self.saveNeeded_warningIcon.setSizePolicy(sizePolicy)
        self.saveNeeded_warningIcon.setMinimumSize(QSize(110, 110))

        self.gridLayout_3.addWidget(self.saveNeeded_warningIcon, 0, 0, 3, 1)

        self.saveNeeded_save = QPushButton(self.frame1)
        self.saveNeeded_save.setObjectName("saveNeeded_save")

        self.gridLayout_3.addWidget(self.saveNeeded_save, 2, 3, 1, 1)

        self.saveNeeded_msg1 = QLabel(self.frame1)
        self.saveNeeded_msg1.setObjectName("saveNeeded_msg1")

        self.gridLayout_3.addWidget(self.saveNeeded_msg1, 0, 1, 1, 3)

        self.saveNeeded_msg2 = QLabel(self.frame1)
        self.saveNeeded_msg2.setObjectName("saveNeeded_msg2")

        self.gridLayout_3.addWidget(self.saveNeeded_msg2, 1, 1, 1, 3)

        self.gridLayout_2.addWidget(self.frame1, 3, 4, 1, 1)

        self.popupView.addWidget(self.saveNeededPage)
        self.confirmMovePage = QWidget()
        self.confirmMovePage.setObjectName("confirmMovePage")
        self.gridLayout_5 = QGridLayout(self.confirmMovePage)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame2 = QFrame(self.confirmMovePage)
        self.frame2.setObjectName("frame2")
        self.frame2.setContextMenuPolicy(Qt.NoContextMenu)
        self.frame2.setFrameShape(QFrame.StyledPanel)
        self.frame2.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_4.setContentsMargins(2, 2, 2, 2)
        self.confirmMove_cancel = QPushButton(self.frame2)
        self.confirmMove_cancel.setObjectName("confirmMove_cancel")

        self.gridLayout_4.addWidget(self.confirmMove_cancel, 1, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(
            117, 20, QSizePolicy.Fixed, QSizePolicy.Minimum
        )

        self.gridLayout_4.addItem(self.horizontalSpacer, 1, 1, 1, 1)

        self.confirmMove_move = QPushButton(self.frame2)
        self.confirmMove_move.setObjectName("confirmMove_move")

        self.gridLayout_4.addWidget(self.confirmMove_move, 1, 3, 1, 1)

        self.confirmMove_warningIcon = QLabel(self.frame2)
        self.confirmMove_warningIcon.setObjectName("confirmMove_warningIcon")
        sizePolicy.setHeightForWidth(
            self.confirmMove_warningIcon.sizePolicy().hasHeightForWidth()
        )
        self.confirmMove_warningIcon.setSizePolicy(sizePolicy)
        self.confirmMove_warningIcon.setMinimumSize(QSize(110, 110))

        self.gridLayout_4.addWidget(self.confirmMove_warningIcon, 0, 0, 2, 1)

        self.confirmMove_msg1 = QLabel(self.frame2)
        self.confirmMove_msg1.setObjectName("confirmMove_msg1")

        self.gridLayout_4.addWidget(self.confirmMove_msg1, 0, 1, 1, 3)

        self.gridLayout_5.addWidget(self.frame2, 0, 0, 1, 1)

        self.popupView.addWidget(self.confirmMovePage)
        self.confirmDeletePage = QWidget()
        self.confirmDeletePage.setObjectName("confirmDeletePage")
        self.gridLayout_7 = QGridLayout(self.confirmDeletePage)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame3 = QFrame(self.confirmDeletePage)
        self.frame3.setObjectName("frame3")
        self.frame3.setContextMenuPolicy(Qt.NoContextMenu)
        self.frame3.setFrameShape(QFrame.StyledPanel)
        self.frame3.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame3)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.gridLayout_6.setContentsMargins(2, 2, 2, 2)
        self.confirmDelete_cancel = QPushButton(self.frame3)
        self.confirmDelete_cancel.setObjectName("confirmDelete_cancel")

        self.gridLayout_6.addWidget(self.confirmDelete_cancel, 2, 2, 1, 1)

        self.confirmDelete_warningIcon = QLabel(self.frame3)
        self.confirmDelete_warningIcon.setObjectName("confirmDelete_warningIcon")
        sizePolicy.setHeightForWidth(
            self.confirmDelete_warningIcon.sizePolicy().hasHeightForWidth()
        )
        self.confirmDelete_warningIcon.setSizePolicy(sizePolicy)
        self.confirmDelete_warningIcon.setMinimumSize(QSize(110, 110))

        self.gridLayout_6.addWidget(self.confirmDelete_warningIcon, 0, 0, 3, 1)

        self.confirmDelete_delete = QPushButton(self.frame3)
        self.confirmDelete_delete.setObjectName("confirmDelete_delete")

        self.gridLayout_6.addWidget(self.confirmDelete_delete, 2, 3, 1, 1)

        self.confirmDelete_msg1 = QLabel(self.frame3)
        self.confirmDelete_msg1.setObjectName("confirmDelete_msg1")

        self.gridLayout_6.addWidget(self.confirmDelete_msg1, 0, 1, 1, 3)

        self.confirmDelete_msg2 = QLabel(self.frame3)
        self.confirmDelete_msg2.setObjectName("confirmDelete_msg2")

        self.gridLayout_6.addWidget(self.confirmDelete_msg2, 1, 1, 1, 3)

        self.horizontalSpacer_2 = QSpacerItem(
            117, 20, QSizePolicy.Fixed, QSizePolicy.Minimum
        )

        self.gridLayout_6.addItem(self.horizontalSpacer_2, 2, 1, 1, 1)

        self.gridLayout_7.addWidget(self.frame3, 0, 0, 1, 1)

        self.popupView.addWidget(self.confirmDeletePage)

        self.gridLayout.addWidget(self.popupView, 0, 0, 1, 1)

        self.retranslateUi(areYouSure_popupV3)

        self.popupView.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(areYouSure_popupV3)

    # setupUi

    def retranslateUi(self, areYouSure_popupV3):
        areYouSure_popupV3.setWindowTitle(
            QCoreApplication.translate("areYouSure_popupV3", "Form", None)
        )
        self.saveNeeded_noSave.setText(
            QCoreApplication.translate("areYouSure_popupV3", "Don't Save", None)
        )
        self.saveNeeded_cancel.setText(
            QCoreApplication.translate("areYouSure_popupV3", "Cancel", None)
        )
        self.saveNeeded_warningIcon.setText("")
        self.saveNeeded_save.setText(
            QCoreApplication.translate("areYouSure_popupV3", "Save", None)
        )
        self.saveNeeded_msg1.setText("")
        self.saveNeeded_msg2.setText(
            QCoreApplication.translate(
                "areYouSure_popupV3",
                "Changes that have not been saved will be lost.",
                None,
            )
        )
        self.confirmMove_cancel.setText(
            QCoreApplication.translate("areYouSure_popupV3", "Cancel", None)
        )
        self.confirmMove_move.setText(
            QCoreApplication.translate("areYouSure_popupV3", "Move", None)
        )
        self.confirmMove_warningIcon.setText("")
        self.confirmMove_msg1.setText("")
        self.confirmDelete_cancel.setText(
            QCoreApplication.translate("areYouSure_popupV3", "Cancel", None)
        )
        self.confirmDelete_warningIcon.setText("")
        self.confirmDelete_delete.setText(
            QCoreApplication.translate("areYouSure_popupV3", "Delete", None)
        )
        self.confirmDelete_msg1.setText("")
        self.confirmDelete_msg2.setText(
            QCoreApplication.translate(
                "areYouSure_popupV3",
                "This file can be restored from the system trash.",
                None,
            )
        )

    # retranslateUi
