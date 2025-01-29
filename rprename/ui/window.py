# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'window.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QProgressBar, QPushButton,
    QSizePolicy, QWidget)

class Ui_Window(object):
    def setupUi(self, Window):
        if not Window.objectName():
            Window.setObjectName(u"Window")
        Window.resize(692, 534)
        self.gridLayout_2 = QGridLayout(Window)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(Window)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setBold(True)
        self.label_2.setFont(font)

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.label_3 = QLabel(Window)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.gridLayout.addWidget(self.label_3, 0, 1, 1, 1)

        self.srcFileList = QListWidget(Window)
        self.srcFileList.setObjectName(u"srcFileList")

        self.gridLayout.addWidget(self.srcFileList, 1, 0, 1, 1)

        self.dstFileList = QListWidget(Window)
        self.dstFileList.setObjectName(u"dstFileList")

        self.gridLayout.addWidget(self.dstFileList, 1, 1, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 2, 0, 1, 3)

        self.prefixEdit = QLineEdit(Window)
        self.prefixEdit.setObjectName(u"prefixEdit")
        self.prefixEdit.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_2.addWidget(self.prefixEdit, 4, 0, 1, 1)

        self.extensionLabel = QLabel(Window)
        self.extensionLabel.setObjectName(u"extensionLabel")
        self.extensionLabel.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_2.addWidget(self.extensionLabel, 4, 1, 1, 1)

        self.progressBar = QProgressBar(Window)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)

        self.gridLayout_2.addWidget(self.progressBar, 5, 0, 1, 3)

        self.label = QLabel(Window)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 3)

        self.renameFilesButton = QPushButton(Window)
        self.renameFilesButton.setObjectName(u"renameFilesButton")
        self.renameFilesButton.setMinimumSize(QSize(0, 30))
        self.renameFilesButton.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_2.addWidget(self.renameFilesButton, 4, 2, 1, 1)

        self.label_4 = QLabel(Window)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.gridLayout_2.addWidget(self.label_4, 3, 0, 1, 3)

        self.dirEdit = QLineEdit(Window)
        self.dirEdit.setObjectName(u"dirEdit")
        self.dirEdit.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_2.addWidget(self.dirEdit, 1, 0, 1, 2)

        self.loadFilesButton = QPushButton(Window)
        self.loadFilesButton.setObjectName(u"loadFilesButton")
        self.loadFilesButton.setMinimumSize(QSize(0, 30))
        self.loadFilesButton.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_2.addWidget(self.loadFilesButton, 1, 2, 1, 1)


        self.retranslateUi(Window)

        QMetaObject.connectSlotsByName(Window)
    # setupUi

    def retranslateUi(self, Window):
        Window.setWindowTitle(QCoreApplication.translate("Window", u"RP Renamer", None))
        self.label_2.setText(QCoreApplication.translate("Window", u"Files to rename", None))
        self.label_3.setText(QCoreApplication.translate("Window", u"Renamed files", None))
        self.prefixEdit.setPlaceholderText(QCoreApplication.translate("Window", u"Rename yours files to...", None))
        self.extensionLabel.setText(QCoreApplication.translate("Window", u"*.jpg", None))
        self.label.setText(QCoreApplication.translate("Window", u"Last Source Directory:", None))
        self.renameFilesButton.setText(QCoreApplication.translate("Window", u"&Rename", None))
        self.label_4.setText(QCoreApplication.translate("Window", u"File Name Prefix", None))
        self.loadFilesButton.setText(QCoreApplication.translate("Window", u"&Load Files", None))
    # retranslateUi

