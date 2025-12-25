# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QLabel, QLineEdit,
    QProgressBar, QPushButton, QSizePolicy, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(636, 600)
        self.btn_download = QPushButton(Widget)
        self.btn_download.setObjectName(u"btn_download")
        self.btn_download.setGeometry(QRect(10, 150, 106, 36))
        font = QFont()
        font.setPointSize(12)
        self.btn_download.setFont(font)
        self.btn_download.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.link = QLineEdit(Widget)
        self.link.setObjectName(u"link")
        self.link.setGeometry(QRect(10, 100, 201, 28))
        self.link.setCursor(QCursor(Qt.CursorShape.IBeamCursor))
        self.checkBox = QCheckBox(Widget)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(230, 100, 92, 25))
        self.checkBox.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.progressBar = QProgressBar(Widget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(340, 100, 118, 23))
        self.progressBar.setValue(0)
        self.label = QLabel(Widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(470, 100, 101, 20))
        self.btn_cancel = QPushButton(Widget)
        self.btn_cancel.setObjectName(u"btn_cancel")
        self.btn_cancel.setGeometry(QRect(140, 150, 106, 36))
        self.btn_cancel.setFont(font)
        self.btn_cancel.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.btn_download.setText(QCoreApplication.translate("Widget", u"Download", None))
        self.link.setPlaceholderText(QCoreApplication.translate("Widget", u"Input URL:", None))
        self.checkBox.setText(QCoreApplication.translate("Widget", u"mp3", None))
        self.label.setText(QCoreApplication.translate("Widget", u"is downloaded", None))
        self.btn_cancel.setText(QCoreApplication.translate("Widget", u"Cancel", None))
    # retranslateUi

