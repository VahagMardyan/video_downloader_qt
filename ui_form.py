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
from PySide6.QtWidgets import (QApplication, QCheckBox, QLineEdit, QProgressBar,
    QPushButton, QSizePolicy, QSplitter, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(762, 503)
        Widget.setMinimumSize(QSize(750, 500))
        self.splitter = QSplitter(Widget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setGeometry(QRect(260, 150, 251, 171))
        self.splitter.setOrientation(Qt.Orientation.Vertical)
        self.link = QLineEdit(self.splitter)
        self.link.setObjectName(u"link")
        self.link.setCursor(QCursor(Qt.CursorShape.IBeamCursor))
        self.splitter.addWidget(self.link)
        self.checkBox = QCheckBox(self.splitter)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.splitter.addWidget(self.checkBox)
        self.progressBar = QProgressBar(self.splitter)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)
        self.splitter.addWidget(self.progressBar)
        self.btn_download = QPushButton(self.splitter)
        self.btn_download.setObjectName(u"btn_download")
        font = QFont()
        font.setPointSize(12)
        self.btn_download.setFont(font)
        self.btn_download.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.splitter.addWidget(self.btn_download)
        self.btn_cancel = QPushButton(self.splitter)
        self.btn_cancel.setObjectName(u"btn_cancel")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.btn_cancel.setFont(font1)
        self.btn_cancel.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_cancel.setStyleSheet(u"	background-color: rgb(199, 15, 39);\n"
"    border: none;\n"
"    border-radius: 6px;\n"
"    padding: 8px;\n"
"    font-weight: bold;")
        self.splitter.addWidget(self.btn_cancel)

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.link.setPlaceholderText(QCoreApplication.translate("Widget", u"Input URL:", None))
        self.checkBox.setText(QCoreApplication.translate("Widget", u"mp3", None))
#if QT_CONFIG(tooltip)
        self.btn_download.setToolTip(QCoreApplication.translate("Widget", u"<html><head/><body><p>Enter</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_download.setText(QCoreApplication.translate("Widget", u"Download", None))
#if QT_CONFIG(tooltip)
        self.btn_cancel.setToolTip(QCoreApplication.translate("Widget", u"<html><head/><body><p>Cancel downloading</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_cancel.setText(QCoreApplication.translate("Widget", u"Cancel", None))
    # retranslateUi

