# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login_agendamentos.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form: object) -> object:
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(859, 579)
        icon = QIcon()
        icon.addFile(u"logo.png", QSize(), QIcon.Normal, QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(9, 9, 9, 9)
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setPixmap(QPixmap(u"pms_fundo_HOME.jpg"))
        self.label.setScaledContents(False)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.le_usuario = QLineEdit(self.frame)
        self.le_usuario.setObjectName(u"le_usuario")
        self.le_usuario.setMinimumSize(QSize(141, 20))
        self.le_usuario.setMaximumSize(QSize(141, 20))
        font = QFont()
        font.setFamily(u"Courier")
        font.setPointSize(12)
        self.le_usuario.setFont(font)
        self.le_usuario.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.le_usuario, 0, Qt.AlignHCenter)

        self.le_senha = QLineEdit(self.frame)
        self.le_senha.setObjectName(u"le_senha")
        self.le_senha.setMinimumSize(QSize(141, 20))
        self.le_senha.setMaximumSize(QSize(141, 20))
        self.le_senha.setFont(font)
        self.le_senha.setEchoMode(QLineEdit.Password)
        self.le_senha.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.le_senha, 0, Qt.AlignHCenter)

        self.btn_login = QPushButton(self.frame)
        self.btn_login.setObjectName(u"btn_login")
        font1 = QFont()
        font1.setFamily(u"Courier New")
        font1.setBold(True)
        font1.setItalic(False)
        font1.setUnderline(False)
        font1.setWeight(75)
        font1.setStrikeOut(False)
        self.btn_login.setFont(font1)
        self.btn_login.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_login.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"    \n"
"	background-color: rgb(144, 0, 0);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: black;\n"
"    font: bold 14px;\n"
"    min-width: 10em;\n"
"    padding: 6px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(238, 238, 0);\n"
"    border-style: inset;\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: red;\n"
"    border-style: inset;\n"
"}")

        self.horizontalLayout.addWidget(self.btn_login, 0, Qt.AlignHCenter)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Sistema de Agendamento DGS", None))
        self.label.setText("")
        self.le_usuario.setPlaceholderText(QCoreApplication.translate("Form", u"USUARIO", None))
        self.le_senha.setPlaceholderText(QCoreApplication.translate("Form", u"SENHA", None))
        self.btn_login.setText(QCoreApplication.translate("Form", u"LOGIN", None))
    # retranslateUi

