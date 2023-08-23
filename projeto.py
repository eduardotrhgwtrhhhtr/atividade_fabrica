# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'projeto.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSlider,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 696)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalSlider = QSlider(self.frame)
        self.verticalSlider.setObjectName(u"verticalSlider")
        self.verticalSlider.setOrientation(Qt.Vertical)

        self.verticalLayout_3.addWidget(self.verticalSlider)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.ok = QPushButton(self.frame_2)
        self.ok.setObjectName(u"ok")
        self.ok.setCursor(QCursor(Qt.CrossCursor))
        self.ok.setStyleSheet(u"background-color: rgb(0, 255, 127);")

        self.horizontalLayout.addWidget(self.ok)

        self.organizar = QPushButton(self.frame_2)
        self.organizar.setObjectName(u"organizar")
        self.organizar.setCursor(QCursor(Qt.CrossCursor))
        self.organizar.setStyleSheet(u"background-color: rgb(0, 255, 255);")
        self.organizar.setAutoDefault(True)

        self.horizontalLayout.addWidget(self.organizar)

        self.lineEdit = QLineEdit(self.frame_2)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout.addWidget(self.lineEdit)


        self.verticalLayout_3.addWidget(self.frame_2)


        self.verticalLayout_2.addWidget(self.frame)

        self.verticalSlider_2 = QSlider(self.centralwidget)
        self.verticalSlider_2.setObjectName(u"verticalSlider_2")
        self.verticalSlider_2.setOrientation(Qt.Vertical)

        self.verticalLayout_2.addWidget(self.verticalSlider_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.ok.setText(QCoreApplication.translate("MainWindow", u"ok", None))
        self.organizar.setText(QCoreApplication.translate("MainWindow", u"organizar", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"selecione uma pasta", None))
    # retranslateUi

