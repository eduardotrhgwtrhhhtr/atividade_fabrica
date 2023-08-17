# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'atv.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QMainWindow, QSizePolicy, QVBoxLayout, QWidget)
import login_senha_qrc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(378, 567)
        MainWindow.setStyleSheet(u"background-color: rgb(130, 130, 130);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.f_usuario = QFrame(self.frame)
        self.f_usuario.setObjectName(u"f_usuario")
        self.f_usuario.setFrameShape(QFrame.StyledPanel)
        self.f_usuario.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.f_usuario)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.f_senha = QFrame(self.f_usuario)
        self.f_senha.setObjectName(u"f_senha")
        self.f_senha.setFrameShape(QFrame.StyledPanel)
        self.f_senha.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.f_senha)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.f_usuario_2 = QLabel(self.f_senha)
        self.f_usuario_2.setObjectName(u"f_usuario_2")

        self.verticalLayout.addWidget(self.f_usuario_2)

        self.label_2 = QLabel(self.f_senha)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setPixmap(QPixmap(u":/stuart/ninja.jpg"))

        self.verticalLayout.addWidget(self.label_2)

        self.l_usuario = QLineEdit(self.f_senha)
        self.l_usuario.setObjectName(u"l_usuario")

        self.verticalLayout.addWidget(self.l_usuario)

        self.label = QLabel(self.f_senha)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.l_senha = QLabel(self.f_senha)
        self.l_senha.setObjectName(u"l_senha")

        self.verticalLayout.addWidget(self.l_senha)

        self.lineEdit_2 = QLineEdit(self.f_senha)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setEchoMode(QLineEdit.Password)

        self.verticalLayout.addWidget(self.lineEdit_2)


        self.verticalLayout_2.addWidget(self.f_senha)


        self.verticalLayout_4.addWidget(self.f_usuario)


        self.verticalLayout_3.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.f_usuario_2.setText(QCoreApplication.translate("MainWindow", u"USUARIO", None))
        self.label_2.setText("")
        self.label.setText("")
        self.l_senha.setText(QCoreApplication.translate("MainWindow", u"SENHA", None))
    # retranslateUi

