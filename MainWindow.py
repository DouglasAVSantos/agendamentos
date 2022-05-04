# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1082, 859)
        icon = QIcon()
        icon.addFile(u"logo.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_13 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_home = QPushButton(self.centralwidget)
        self.btn_home.setObjectName(u"btn_home")
        self.btn_home.setMinimumSize(QSize(186, 0))
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_home.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout.addWidget(self.btn_home)

        self.btn_cadastrar = QPushButton(self.centralwidget)
        self.btn_cadastrar.setObjectName(u"btn_cadastrar")
        self.btn_cadastrar.setMinimumSize(QSize(186, 0))
        self.btn_cadastrar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cadastrar.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout.addWidget(self.btn_cadastrar)

        self.btn_cadastrados = QPushButton(self.centralwidget)
        self.btn_cadastrados.setObjectName(u"btn_cadastrados")
        self.btn_cadastrados.setMinimumSize(QSize(186, 0))
        self.btn_cadastrados.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_cadastrados.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout.addWidget(self.btn_cadastrados)

        self.btn_agendamento = QPushButton(self.centralwidget)
        self.btn_agendamento.setObjectName(u"btn_agendamento")
        self.btn_agendamento.setMinimumSize(QSize(186, 0))
        self.btn_agendamento.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_agendamento.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout.addWidget(self.btn_agendamento)

        self.btn_sobre = QPushButton(self.centralwidget)
        self.btn_sobre.setObjectName(u"btn_sobre")
        self.btn_sobre.setMinimumSize(QSize(186, 0))
        self.btn_sobre.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_sobre.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout.addWidget(self.btn_sobre)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.verticalLayout_10 = QVBoxLayout(self.page_home)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.frame = QFrame(self.page_home)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.frame)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.label_22 = QLabel(self.frame)
        self.label_22.setObjectName(u"label_22")

        self.horizontalLayout_26.addWidget(self.label_22)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_20 = QLabel(self.frame)
        self.label_20.setObjectName(u"label_20")

        self.horizontalLayout_17.addWidget(self.label_20)

        self.btn_new_user = QPushButton(self.frame)
        self.btn_new_user.setObjectName(u"btn_new_user")
        self.btn_new_user.setMinimumSize(QSize(186, 33))
        self.btn_new_user.setMaximumSize(QSize(208, 33))
        self.btn_new_user.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_new_user.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_17.addWidget(self.btn_new_user)

        self.label_21 = QLabel(self.frame)
        self.label_21.setObjectName(u"label_21")

        self.horizontalLayout_17.addWidget(self.label_21)


        self.verticalLayout_2.addLayout(self.horizontalLayout_17)

        self.label_18 = QLabel(self.frame)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setPixmap(QPixmap(u"pms_fundo_HOME.jpg"))
        self.label_18.setScaledContents(True)

        self.verticalLayout_2.addWidget(self.label_18)

        self.label_74 = QLabel(self.frame)
        self.label_74.setObjectName(u"label_74")

        self.verticalLayout_2.addWidget(self.label_74)


        self.horizontalLayout_26.addLayout(self.verticalLayout_2)

        self.label_23 = QLabel(self.frame)
        self.label_23.setObjectName(u"label_23")

        self.horizontalLayout_26.addWidget(self.label_23)


        self.horizontalLayout_30.addLayout(self.horizontalLayout_26)


        self.verticalLayout_10.addWidget(self.frame)

        self.stackedWidget.addWidget(self.page_home)
        self.page_new_user = QWidget()
        self.page_new_user.setObjectName(u"page_new_user")
        self.verticalLayout_17 = QVBoxLayout(self.page_new_user)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.frame_2 = QFrame(self.page_new_user)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_2)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.label_49 = QLabel(self.frame_2)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setMinimumSize(QSize(311, 61))
        self.label_49.setMaximumSize(QSize(311, 61))
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_49.setFont(font)
        self.label_49.setStyleSheet(u"QLabel {\n"
"	color: rgb(255, 255, 255);\n"
"    \n"
"	background-color: rgb(144, 0, 0);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: black;\n"
"}")
        self.label_49.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_28.addWidget(self.label_49)


        self.verticalLayout_11.addLayout(self.horizontalLayout_28)


        self.verticalLayout_17.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.page_new_user)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.label_47 = QLabel(self.frame_3)
        self.label_47.setObjectName(u"label_47")

        self.horizontalLayout_29.addWidget(self.label_47)

        self.frame_13 = QFrame(self.frame_3)
        self.frame_13.setObjectName(u"frame_13")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_13.sizePolicy().hasHeightForWidth())
        self.frame_13.setSizePolicy(sizePolicy)
        self.frame_13.setStyleSheet(u"border-width: 2px;\n"
"border-color: black;\n"
"border-style: solid;\n"
"display: inline-block;\n"
"border-radius: 8px")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.frame_13)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.le_novo_login = QLineEdit(self.frame_13)
        self.le_novo_login.setObjectName(u"le_novo_login")
        self.le_novo_login.setMinimumSize(QSize(151, 20))
        self.le_novo_login.setMaximumSize(QSize(151, 20))
        self.le_novo_login.setAlignment(Qt.AlignCenter)

        self.verticalLayout_33.addWidget(self.le_novo_login)

        self.le_novo_usuario = QLineEdit(self.frame_13)
        self.le_novo_usuario.setObjectName(u"le_novo_usuario")
        self.le_novo_usuario.setMinimumSize(QSize(151, 20))
        self.le_novo_usuario.setMaximumSize(QSize(151, 20))
        self.le_novo_usuario.setAlignment(Qt.AlignCenter)

        self.verticalLayout_33.addWidget(self.le_novo_usuario)

        self.le_senha1 = QLineEdit(self.frame_13)
        self.le_senha1.setObjectName(u"le_senha1")
        self.le_senha1.setMinimumSize(QSize(151, 20))
        self.le_senha1.setMaximumSize(QSize(151, 20))
        self.le_senha1.setEchoMode(QLineEdit.Password)
        self.le_senha1.setAlignment(Qt.AlignCenter)

        self.verticalLayout_33.addWidget(self.le_senha1)

        self.le_senha2 = QLineEdit(self.frame_13)
        self.le_senha2.setObjectName(u"le_senha2")
        self.le_senha2.setMinimumSize(QSize(151, 21))
        self.le_senha2.setMaximumSize(QSize(151, 21))
        self.le_senha2.setEchoMode(QLineEdit.Password)
        self.le_senha2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_33.addWidget(self.le_senha2)

        self.cb_users = QComboBox(self.frame_13)
        self.cb_users.addItem("")
        self.cb_users.addItem("")
        self.cb_users.setObjectName(u"cb_users")
        self.cb_users.setMinimumSize(QSize(151, 20))
        self.cb_users.setMaximumSize(QSize(151, 20))
        font1 = QFont()
        font1.setPointSize(12)
        self.cb_users.setFont(font1)
        self.cb_users.setLayoutDirection(Qt.LeftToRight)
        self.cb_users.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.verticalLayout_33.addWidget(self.cb_users)

        self.bt_cadastrar_usuario = QPushButton(self.frame_13)
        self.bt_cadastrar_usuario.setObjectName(u"bt_cadastrar_usuario")
        self.bt_cadastrar_usuario.setMinimumSize(QSize(151, 31))
        self.bt_cadastrar_usuario.setMaximumSize(QSize(151, 31))
        font2 = QFont()
        font2.setFamily(u"Courier")
        font2.setPointSize(12)
        font2.setBold(True)
        font2.setWeight(75)
        self.bt_cadastrar_usuario.setFont(font2)
        self.bt_cadastrar_usuario.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_cadastrar_usuario.setStyleSheet(u"QPushButton{\n"
"\n"
"background-color: rgb(219, 57, 62);\n"
"border-radius: 8px;\n"
"color: rgb(255, 255, 255);\n"
"border-width: 2px;\n"
"border-color: black;\n"
"border-style: solid;\n"
"display: inline-block;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"	\n"
"	background-color: rgb(77, 11, 17);\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"}")

        self.verticalLayout_33.addWidget(self.bt_cadastrar_usuario)


        self.horizontalLayout_29.addWidget(self.frame_13)

        self.label_46 = QLabel(self.frame_3)
        self.label_46.setObjectName(u"label_46")

        self.horizontalLayout_29.addWidget(self.label_46)

        self.frame_14 = QFrame(self.frame_3)
        self.frame_14.setObjectName(u"frame_14")
        sizePolicy.setHeightForWidth(self.frame_14.sizePolicy().hasHeightForWidth())
        self.frame_14.setSizePolicy(sizePolicy)
        self.frame_14.setStyleSheet(u"border-width: 2px;\n"
"border-color: black;\n"
"border-style: solid;\n"
"display: inline-block;\n"
"border-radius: 8px")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.frame_14)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.le_usuario_deletar = QLineEdit(self.frame_14)
        self.le_usuario_deletar.setObjectName(u"le_usuario_deletar")
        self.le_usuario_deletar.setMinimumSize(QSize(151, 20))
        self.le_usuario_deletar.setMaximumSize(QSize(151, 20))
        self.le_usuario_deletar.setAlignment(Qt.AlignCenter)

        self.verticalLayout_29.addWidget(self.le_usuario_deletar)

        self.le_senha_deletar = QLineEdit(self.frame_14)
        self.le_senha_deletar.setObjectName(u"le_senha_deletar")
        self.le_senha_deletar.setMinimumSize(QSize(151, 20))
        self.le_senha_deletar.setMaximumSize(QSize(151, 20))
        self.le_senha_deletar.setEchoMode(QLineEdit.Password)
        self.le_senha_deletar.setAlignment(Qt.AlignCenter)

        self.verticalLayout_29.addWidget(self.le_senha_deletar)

        self.bt_deletar_usuario = QPushButton(self.frame_14)
        self.bt_deletar_usuario.setObjectName(u"bt_deletar_usuario")
        self.bt_deletar_usuario.setMinimumSize(QSize(151, 31))
        self.bt_deletar_usuario.setMaximumSize(QSize(151, 31))
        self.bt_deletar_usuario.setFont(font2)
        self.bt_deletar_usuario.setCursor(QCursor(Qt.PointingHandCursor))
        self.bt_deletar_usuario.setStyleSheet(u"QPushButton{\n"
"\n"
"background-color: rgb(219, 57, 62);\n"
"border-radius: 8px;\n"
"color: rgb(255, 255, 255);\n"
"border-width: 2px;\n"
"border-color: black;\n"
"border-style: solid;\n"
"display: inline-block;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"	\n"
"	background-color: rgb(77, 11, 17);\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"\n"
"}")

        self.verticalLayout_29.addWidget(self.bt_deletar_usuario)


        self.horizontalLayout_29.addWidget(self.frame_14)

        self.label_48 = QLabel(self.frame_3)
        self.label_48.setObjectName(u"label_48")

        self.horizontalLayout_29.addWidget(self.label_48)


        self.verticalLayout_17.addWidget(self.frame_3)

        self.stackedWidget.addWidget(self.page_new_user)
        self.page_cadastrados = QWidget()
        self.page_cadastrados.setObjectName(u"page_cadastrados")
        self.verticalLayout_19 = QVBoxLayout(self.page_cadastrados)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_39 = QLabel(self.page_cadastrados)
        self.label_39.setObjectName(u"label_39")

        self.verticalLayout_14.addWidget(self.label_39)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_17 = QLabel(self.page_cadastrados)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_18.addWidget(self.label_17)

        self.label_27 = QLabel(self.page_cadastrados)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setMinimumSize(QSize(311, 61))
        self.label_27.setMaximumSize(QSize(311, 61))
        self.label_27.setFont(font)
        self.label_27.setStyleSheet(u"QLabel {\n"
"	color: rgb(255, 255, 255);\n"
"    \n"
"	background-color: rgb(144, 0, 0);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: black;\n"
"}")
        self.label_27.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_18.addWidget(self.label_27)

        self.label_26 = QLabel(self.page_cadastrados)
        self.label_26.setObjectName(u"label_26")

        self.horizontalLayout_18.addWidget(self.label_26)


        self.verticalLayout_14.addLayout(self.horizontalLayout_18)

        self.label_38 = QLabel(self.page_cadastrados)
        self.label_38.setObjectName(u"label_38")

        self.verticalLayout_14.addWidget(self.label_38)


        self.verticalLayout_19.addLayout(self.verticalLayout_14)

        self.label_41 = QLabel(self.page_cadastrados)
        self.label_41.setObjectName(u"label_41")

        self.verticalLayout_19.addWidget(self.label_41)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_5)

        self.le_update_municipe = QLineEdit(self.page_cadastrados)
        self.le_update_municipe.setObjectName(u"le_update_municipe")
        self.le_update_municipe.setMinimumSize(QSize(134, 0))
        self.le_update_municipe.setStyleSheet(u"QLineEdit{	\n"
"	color: rgb(0, 0, 0);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: black;\n"
"    min-width: 10em;\n"
"}\n"
"")
        self.le_update_municipe.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_23.addWidget(self.le_update_municipe)

        self.btn_update_municipe_id = QPushButton(self.page_cadastrados)
        self.btn_update_municipe_id.setObjectName(u"btn_update_municipe_id")
        self.btn_update_municipe_id.setMinimumSize(QSize(186, 0))
        self.btn_update_municipe_id.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_update_municipe_id.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_23.addWidget(self.btn_update_municipe_id)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_2)


        self.verticalLayout_19.addLayout(self.horizontalLayout_23)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_6)

        self.le_delete_municipe = QLineEdit(self.page_cadastrados)
        self.le_delete_municipe.setObjectName(u"le_delete_municipe")
        self.le_delete_municipe.setMinimumSize(QSize(134, 0))
        self.le_delete_municipe.setStyleSheet(u"QLineEdit{	\n"
"	color: rgb(0, 0, 0);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: black;\n"
"    min-width: 10em;\n"
"}\n"
"")
        self.le_delete_municipe.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_22.addWidget(self.le_delete_municipe)

        self.btn_delete_municipe = QPushButton(self.page_cadastrados)
        self.btn_delete_municipe.setObjectName(u"btn_delete_municipe")
        self.btn_delete_municipe.setMinimumSize(QSize(186, 0))
        self.btn_delete_municipe.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_delete_municipe.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_22.addWidget(self.btn_delete_municipe)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_3)


        self.verticalLayout_19.addLayout(self.horizontalLayout_22)

        self.label_40 = QLabel(self.page_cadastrados)
        self.label_40.setObjectName(u"label_40")

        self.verticalLayout_19.addWidget(self.label_40)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.label_53 = QLabel(self.page_cadastrados)
        self.label_53.setObjectName(u"label_53")

        self.horizontalLayout_25.addWidget(self.label_53)

        self.label_52 = QLabel(self.page_cadastrados)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setMinimumSize(QSize(131, 20))
        self.label_52.setMaximumSize(QSize(131, 20))
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(True)
        font3.setItalic(False)
        font3.setWeight(75)
        self.label_52.setFont(font3)
        self.label_52.setStyleSheet(u"QLabel {\n"
"	color: rgb(255, 255, 255);\n"
"    \n"
"	background-color: rgb(144, 0, 0);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: black;\n"
"}")
        self.label_52.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_25.addWidget(self.label_52)

        self.label_54 = QLabel(self.page_cadastrados)
        self.label_54.setObjectName(u"label_54")

        self.horizontalLayout_25.addWidget(self.label_54)

        self.le_pesquisa_municipe = QLineEdit(self.page_cadastrados)
        self.le_pesquisa_municipe.setObjectName(u"le_pesquisa_municipe")
        self.le_pesquisa_municipe.setMinimumSize(QSize(132, 0))
        self.le_pesquisa_municipe.setLayoutDirection(Qt.LeftToRight)
        self.le_pesquisa_municipe.setStyleSheet(u"QLineEdit{	\n"
"	color: rgb(0, 0, 0);\n"
"    border-style: outset;\n"
"    border-width: 0.5px;\n"
"    border-radius: 10px;\n"
"    border-color: black;\n"
"    min-width: 10em;\n"
"}\n"
"")
        self.le_pesquisa_municipe.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_25.addWidget(self.le_pesquisa_municipe)

        self.label_55 = QLabel(self.page_cadastrados)
        self.label_55.setObjectName(u"label_55")

        self.horizontalLayout_25.addWidget(self.label_55)


        self.verticalLayout_19.addLayout(self.horizontalLayout_25)

        self.tb_municipes_cadastrados = QTableView(self.page_cadastrados)
        self.tb_municipes_cadastrados.setObjectName(u"tb_municipes_cadastrados")
        font4 = QFont()
        font4.setPointSize(10)
        font4.setBold(True)
        font4.setWeight(75)
        self.tb_municipes_cadastrados.setFont(font4)
        self.tb_municipes_cadastrados.setLineWidth(2)
        self.tb_municipes_cadastrados.setMidLineWidth(1)
        self.tb_municipes_cadastrados.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tb_municipes_cadastrados.setEditTriggers(QAbstractItemView.DoubleClicked)
        self.tb_municipes_cadastrados.horizontalHeader().setCascadingSectionResizes(True)
        self.tb_municipes_cadastrados.horizontalHeader().setProperty("showSortIndicator", True)
        self.tb_municipes_cadastrados.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_19.addWidget(self.tb_municipes_cadastrados)

        self.stackedWidget.addWidget(self.page_cadastrados)
        self.page_agendamento = QWidget()
        self.page_agendamento.setObjectName(u"page_agendamento")
        self.verticalLayout_6 = QVBoxLayout(self.page_agendamento)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_44 = QLabel(self.page_agendamento)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setMinimumSize(QSize(311, 61))
        self.label_44.setMaximumSize(QSize(311, 61))
        self.label_44.setFont(font)
        self.label_44.setStyleSheet(u"QLabel {\n"
"	color: rgb(255, 255, 255);\n"
"    \n"
"	background-color: rgb(144, 0, 0);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: black;\n"
"}")
        self.label_44.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_19.addWidget(self.label_44)

        self.calendarWidget_2 = QCalendarWidget(self.page_agendamento)
        self.calendarWidget_2.setObjectName(u"calendarWidget_2")
        self.calendarWidget_2.setMinimumSize(QSize(491, 281))
        self.calendarWidget_2.setMaximumSize(QSize(491, 281))
        font5 = QFont()
        font5.setPointSize(15)
        font5.setBold(True)
        font5.setWeight(75)
        self.calendarWidget_2.setFont(font5)
        self.calendarWidget_2.setGridVisible(True)
        self.calendarWidget_2.setVerticalHeaderFormat(QCalendarWidget.NoVerticalHeader)
        self.calendarWidget_2.setNavigationBarVisible(True)
        self.calendarWidget_2.setDateEditEnabled(True)

        self.horizontalLayout_19.addWidget(self.calendarWidget_2)


        self.verticalLayout_6.addLayout(self.horizontalLayout_19)

        self.label_45 = QLabel(self.page_agendamento)
        self.label_45.setObjectName(u"label_45")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_45.sizePolicy().hasHeightForWidth())
        self.label_45.setSizePolicy(sizePolicy1)

        self.verticalLayout_6.addWidget(self.label_45)

        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_25 = QLabel(self.page_agendamento)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMinimumSize(QSize(174, 31))
        self.label_25.setMaximumSize(QSize(16777215, 31))
        self.label_25.setStyleSheet(u"QLabel {\n"
"	color: rgb(255, 255, 255);\n"
"    \n"
"	background-color: rgb(144, 0, 0);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: black;\n"
"    font: bold 14px;\n"
"    min-width: 10em;}")
        self.label_25.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_25)

        self.comboBox_municipe = QComboBox(self.page_agendamento)
        self.comboBox_municipe.setObjectName(u"comboBox_municipe")
        self.comboBox_municipe.setMinimumSize(QSize(174, 31))
        self.comboBox_municipe.setMaximumSize(QSize(16777215, 31))
        self.comboBox_municipe.setCursor(QCursor(Qt.PointingHandCursor))
        self.comboBox_municipe.setStyleSheet(u"QComboBox {\n"
"	color: rgb(0, 0, 0);\n"
"    \n"
";\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: black;\n"
"    font: bold 14px;\n"
"    min-width: 10em;}")
        self.comboBox_municipe.setMaxVisibleItems(10)

        self.verticalLayout_8.addWidget(self.comboBox_municipe)


        self.horizontalLayout_27.addLayout(self.verticalLayout_8)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_24 = QLabel(self.page_agendamento)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMinimumSize(QSize(174, 31))
        self.label_24.setMaximumSize(QSize(174, 31))
        self.label_24.setStyleSheet(u"QLabel {\n"
"	color: rgb(255, 255, 255);\n"
"    \n"
"	background-color: rgb(144, 0, 0);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: black;\n"
"    font: bold 14px;\n"
"    min-width: 10em;}")
        self.label_24.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_24)

        self.de_data_do_agendamento = QDateEdit(self.page_agendamento)
        self.de_data_do_agendamento.setObjectName(u"de_data_do_agendamento")
        self.de_data_do_agendamento.setMinimumSize(QSize(174, 31))
        self.de_data_do_agendamento.setMaximumSize(QSize(174, 31))
        self.de_data_do_agendamento.setCursor(QCursor(Qt.PointingHandCursor))
        self.de_data_do_agendamento.setStyleSheet(u"QDateEdit {\n"
"	color: rgb(0, 0, 0);\n"
"    \n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: black;\n"
"    font: bold 14px;\n"
"    min-width: 10em;}")
        self.de_data_do_agendamento.setAlignment(Qt.AlignCenter)
        self.de_data_do_agendamento.setDateTime(QDateTime(QDate(2022, 1, 1), QTime(0, 0, 0)))
        self.de_data_do_agendamento.setCalendarPopup(True)

        self.verticalLayout_9.addWidget(self.de_data_do_agendamento)


        self.horizontalLayout_27.addLayout(self.verticalLayout_9)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_43 = QLabel(self.page_agendamento)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setMinimumSize(QSize(174, 31))
        self.label_43.setMaximumSize(QSize(211, 31))
        self.label_43.setStyleSheet(u"QLabel {\n"
"	color: rgb(255, 255, 255);\n"
"    \n"
"	background-color: rgb(144, 0, 0);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: black;\n"
"    font: bold 14px;\n"
"    min-width: 10em;}")
        self.label_43.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_43)

        self.te_horario_agendamento = QTimeEdit(self.page_agendamento)
        self.te_horario_agendamento.setObjectName(u"te_horario_agendamento")
        self.te_horario_agendamento.setMinimumSize(QSize(174, 31))
        self.te_horario_agendamento.setMaximumSize(QSize(211, 31))
        self.te_horario_agendamento.setStyleSheet(u"QTimeEdit {\n"
"	color: rgb(0, 0, 0);\n"
"    \n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: black;\n"
"    font: bold 14px;\n"
"    min-width: 10em;}")
        self.te_horario_agendamento.setAlignment(Qt.AlignCenter)
        self.te_horario_agendamento.setMaximumTime(QTime(17, 30, 0))
        self.te_horario_agendamento.setMinimumTime(QTime(8, 30, 0))

        self.verticalLayout_12.addWidget(self.te_horario_agendamento)


        self.horizontalLayout_27.addLayout(self.verticalLayout_12)

        self.btn_agendar = QPushButton(self.page_agendamento)
        self.btn_agendar.setObjectName(u"btn_agendar")
        self.btn_agendar.setMinimumSize(QSize(186, 31))
        self.btn_agendar.setMaximumSize(QSize(151, 31))
        self.btn_agendar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_agendar.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_27.addWidget(self.btn_agendar)


        self.verticalLayout_6.addLayout(self.horizontalLayout_27)

        self.label_50 = QLabel(self.page_agendamento)
        self.label_50.setObjectName(u"label_50")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_50.sizePolicy().hasHeightForWidth())
        self.label_50.setSizePolicy(sizePolicy2)

        self.verticalLayout_6.addWidget(self.label_50)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_72 = QLabel(self.page_agendamento)
        self.label_72.setObjectName(u"label_72")
        self.label_72.setMinimumSize(QSize(131, 20))
        self.label_72.setMaximumSize(QSize(131, 20))
        self.label_72.setFont(font3)
        self.label_72.setStyleSheet(u"QLabel {\n"
"	color: rgb(255, 255, 255);\n"
"    \n"
"	background-color: rgb(144, 0, 0);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: black;\n"
"}")
        self.label_72.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_14.addWidget(self.label_72)

        self.le_filtro_data = QLineEdit(self.page_agendamento)
        self.le_filtro_data.setObjectName(u"le_filtro_data")
        self.le_filtro_data.setMinimumSize(QSize(132, 0))
        self.le_filtro_data.setLayoutDirection(Qt.LeftToRight)
        self.le_filtro_data.setStyleSheet(u"QLineEdit{	\n"
"	color: rgb(0, 0, 0);\n"
"    border-style: outset;\n"
"    border-width: 0.5px;\n"
"    border-radius: 10px;\n"
"    border-color: black;\n"
"    min-width: 10em;\n"
"}\n"
"")
        self.le_filtro_data.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_14.addWidget(self.le_filtro_data)


        self.verticalLayout_6.addLayout(self.horizontalLayout_14)

        self.tableView_agendamento = QTableView(self.page_agendamento)
        self.tableView_agendamento.setObjectName(u"tableView_agendamento")
        font6 = QFont()
        font6.setPointSize(12)
        font6.setBold(True)
        font6.setWeight(75)
        self.tableView_agendamento.setFont(font6)
        self.tableView_agendamento.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableView_agendamento.setSortingEnabled(True)

        self.verticalLayout_6.addWidget(self.tableView_agendamento)

        self.stackedWidget.addWidget(self.page_agendamento)
        self.page_cadastrar = QWidget()
        self.page_cadastrar.setObjectName(u"page_cadastrar")
        self.verticalLayout_16 = QVBoxLayout(self.page_cadastrar)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_68 = QLabel(self.page_cadastrar)
        self.label_68.setObjectName(u"label_68")

        self.horizontalLayout_20.addWidget(self.label_68)

        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_69 = QLabel(self.page_cadastrar)
        self.label_69.setObjectName(u"label_69")

        self.verticalLayout_15.addWidget(self.label_69)

        self.label_12 = QLabel(self.page_cadastrar)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setPixmap(QPixmap(u"logo.png"))
        self.label_12.setScaledContents(True)

        self.verticalLayout_15.addWidget(self.label_12)

        self.label_67 = QLabel(self.page_cadastrar)
        self.label_67.setObjectName(u"label_67")

        self.verticalLayout_15.addWidget(self.label_67)


        self.horizontalLayout_20.addLayout(self.verticalLayout_15)

        self.label_11 = QLabel(self.page_cadastrar)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_20.addWidget(self.label_11)


        self.horizontalLayout_24.addLayout(self.horizontalLayout_20)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_71 = QLabel(self.page_cadastrar)
        self.label_71.setObjectName(u"label_71")

        self.verticalLayout_7.addWidget(self.label_71)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_28 = QLabel(self.page_cadastrar)
        self.label_28.setObjectName(u"label_28")
        font7 = QFont()
        font7.setFamily(u"Courier New")
        font7.setPointSize(32)
        font7.setBold(True)
        font7.setWeight(75)
        self.label_28.setFont(font7)

        self.horizontalLayout_15.addWidget(self.label_28)

        self.label_73 = QLabel(self.page_cadastrar)
        self.label_73.setObjectName(u"label_73")

        self.horizontalLayout_15.addWidget(self.label_73)


        self.verticalLayout_7.addLayout(self.horizontalLayout_15)

        self.label_70 = QLabel(self.page_cadastrar)
        self.label_70.setObjectName(u"label_70")

        self.verticalLayout_7.addWidget(self.label_70)


        self.horizontalLayout_24.addLayout(self.verticalLayout_7)


        self.verticalLayout_16.addLayout(self.horizontalLayout_24)

        self.label_16 = QLabel(self.page_cadastrar)
        self.label_16.setObjectName(u"label_16")

        self.verticalLayout_16.addWidget(self.label_16)

        self.label_15 = QLabel(self.page_cadastrar)
        self.label_15.setObjectName(u"label_15")

        self.verticalLayout_16.addWidget(self.label_15)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_19 = QLabel(self.page_cadastrar)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMinimumSize(QSize(61, 31))
        self.label_19.setMaximumSize(QSize(61, 31))
        self.label_19.setPixmap(QPixmap(u"icone agendamento.png"))
        self.label_19.setScaledContents(True)
        self.label_19.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_19)

        self.label_66 = QLabel(self.page_cadastrar)
        self.label_66.setObjectName(u"label_66")
        self.label_66.setMinimumSize(QSize(131, 20))
        self.label_66.setMaximumSize(QSize(131, 20))
        self.label_66.setFont(font3)
        self.label_66.setStyleSheet(u"QLabel {\n"
"	color: rgb(255, 255, 255);\n"
"    \n"
"	background-color: rgb(144, 0, 0);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: black;\n"
"}")
        self.label_66.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_66)

        self.le_nome = QLineEdit(self.page_cadastrar)
        self.le_nome.setObjectName(u"le_nome")
        font8 = QFont()
        font8.setFamily(u"Courier New")
        font8.setPointSize(12)
        font8.setBold(True)
        font8.setWeight(75)
        self.le_nome.setFont(font8)
        self.le_nome.setStyleSheet(u"QLineEdit{	\n"
"	color: rgb(0, 0, 0);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: black;\n"
"    min-width: 10em;\n"
"}\n"
"")

        self.horizontalLayout_4.addWidget(self.le_nome)


        self.verticalLayout_16.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_29 = QLabel(self.page_cadastrar)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setMinimumSize(QSize(61, 31))
        self.label_29.setMaximumSize(QSize(61, 31))
        self.label_29.setPixmap(QPixmap(u"icone agendamento.png"))
        self.label_29.setScaledContents(True)
        self.label_29.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_29)

        self.label_65 = QLabel(self.page_cadastrar)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setMinimumSize(QSize(131, 20))
        self.label_65.setMaximumSize(QSize(131, 20))
        self.label_65.setFont(font3)
        self.label_65.setStyleSheet(u"QLabel {\n"
"	color: rgb(255, 255, 255);\n"
"    \n"
"	background-color: rgb(144, 0, 0);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: black;\n"
"}")
        self.label_65.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_65)

        self.lv_rg = QLineEdit(self.page_cadastrar)
        self.lv_rg.setObjectName(u"lv_rg")
        self.lv_rg.setFont(font8)
        self.lv_rg.setStyleSheet(u"QLineEdit{	\n"
"	color: rgb(0, 0, 0);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: black;\n"
"    min-width: 10em;\n"
"}\n"
"")

        self.horizontalLayout_5.addWidget(self.lv_rg)


        self.verticalLayout_16.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_30 = QLabel(self.page_cadastrar)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setMinimumSize(QSize(61, 31))
        self.label_30.setMaximumSize(QSize(61, 31))
        self.label_30.setPixmap(QPixmap(u"icone agendamento.png"))
        self.label_30.setScaledContents(True)
        self.label_30.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_30)

        self.label_64 = QLabel(self.page_cadastrar)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setMinimumSize(QSize(131, 20))
        self.label_64.setMaximumSize(QSize(131, 20))
        self.label_64.setFont(font3)
        self.label_64.setStyleSheet(u"QLabel {\n"
"	color: rgb(255, 255, 255);\n"
"    \n"
"	background-color: rgb(144, 0, 0);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: black;\n"
"}")
        self.label_64.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_64)

        self.le_cpf = QLineEdit(self.page_cadastrar)
        self.le_cpf.setObjectName(u"le_cpf")
        self.le_cpf.setFont(font8)
        self.le_cpf.setStyleSheet(u"QLineEdit{	\n"
"	color: rgb(0, 0, 0);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: black;\n"
"    min-width: 10em;\n"
"}\n"
"")

        self.horizontalLayout_6.addWidget(self.le_cpf)


        self.verticalLayout_16.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_37 = QLabel(self.page_cadastrar)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setMinimumSize(QSize(61, 31))
        self.label_37.setMaximumSize(QSize(61, 31))
        self.label_37.setPixmap(QPixmap(u"icone agendamento.png"))
        self.label_37.setScaledContents(True)
        self.label_37.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.label_37)

        self.label_63 = QLabel(self.page_cadastrar)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setMinimumSize(QSize(161, 20))
        self.label_63.setMaximumSize(QSize(161, 20))
        self.label_63.setFont(font3)
        self.label_63.setStyleSheet(u"QLabel {\n"
"	color: rgb(255, 255, 255);\n"
"    \n"
"	background-color: rgb(144, 0, 0);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: black;\n"
"}")
        self.label_63.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.label_63)

        self.de_data_nascimento = QDateEdit(self.page_cadastrar)
        self.de_data_nascimento.setObjectName(u"de_data_nascimento")
        self.de_data_nascimento.setFont(font8)
        self.de_data_nascimento.setStyleSheet(u"QLineEdit{	\n"
"	color: rgb(0, 0, 0);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: black;\n"
"    min-width: 10em;\n"
"}")
        self.de_data_nascimento.setCalendarPopup(True)

        self.horizontalLayout_13.addWidget(self.de_data_nascimento)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer)


        self.verticalLayout_16.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_42 = QLabel(self.page_cadastrar)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setMinimumSize(QSize(61, 31))
        self.label_42.setMaximumSize(QSize(61, 31))
        self.label_42.setPixmap(QPixmap(u"icone agendamento.png"))
        self.label_42.setScaledContents(True)
        self.label_42.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_21.addWidget(self.label_42)

        self.label_62 = QLabel(self.page_cadastrar)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setMinimumSize(QSize(131, 20))
        self.label_62.setMaximumSize(QSize(131, 20))
        self.label_62.setFont(font3)
        self.label_62.setStyleSheet(u"QLabel {\n"
"	color: rgb(255, 255, 255);\n"
"    \n"
"	background-color: rgb(144, 0, 0);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: black;\n"
"}")
        self.label_62.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_21.addWidget(self.label_62)

        self.le_telefone = QLineEdit(self.page_cadastrar)
        self.le_telefone.setObjectName(u"le_telefone")
        self.le_telefone.setFont(font8)
        self.le_telefone.setStyleSheet(u"QLineEdit{	\n"
"	color: rgb(0, 0, 0);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: black;\n"
"    min-width: 10em;\n"
"}\n"
"")

        self.horizontalLayout_21.addWidget(self.le_telefone)


        self.verticalLayout_16.addLayout(self.horizontalLayout_21)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_36 = QLabel(self.page_cadastrar)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setMinimumSize(QSize(61, 31))
        self.label_36.setMaximumSize(QSize(61, 31))
        self.label_36.setPixmap(QPixmap(u"icone agendamento.png"))
        self.label_36.setScaledContents(True)
        self.label_36.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_11.addWidget(self.label_36)

        self.label_61 = QLabel(self.page_cadastrar)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setMinimumSize(QSize(131, 20))
        self.label_61.setMaximumSize(QSize(131, 20))
        self.label_61.setFont(font3)
        self.label_61.setStyleSheet(u"QLabel {\n"
"	color: rgb(255, 255, 255);\n"
"    \n"
"	background-color: rgb(144, 0, 0);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: black;\n"
"}")
        self.label_61.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_11.addWidget(self.label_61)

        self.le_instituicao = QLineEdit(self.page_cadastrar)
        self.le_instituicao.setObjectName(u"le_instituicao")
        self.le_instituicao.setFont(font8)
        self.le_instituicao.setStyleSheet(u"QLineEdit{	\n"
"	color: rgb(0, 0, 0);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: black;\n"
"    min-width: 10em;\n"
"}\n"
"")

        self.horizontalLayout_11.addWidget(self.le_instituicao)


        self.verticalLayout_16.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_31 = QLabel(self.page_cadastrar)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setMinimumSize(QSize(61, 31))
        self.label_31.setMaximumSize(QSize(61, 31))
        self.label_31.setPixmap(QPixmap(u"icone agendamento.png"))
        self.label_31.setScaledContents(True)
        self.label_31.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.label_31)

        self.label_60 = QLabel(self.page_cadastrar)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setMinimumSize(QSize(131, 20))
        self.label_60.setMaximumSize(QSize(131, 20))
        self.label_60.setFont(font3)
        self.label_60.setStyleSheet(u"QLabel {\n"
"	color: rgb(255, 255, 255);\n"
"    \n"
"	background-color: rgb(144, 0, 0);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: black;\n"
"}")
        self.label_60.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.label_60)

        self.le_cep = QLineEdit(self.page_cadastrar)
        self.le_cep.setObjectName(u"le_cep")
        self.le_cep.setFont(font8)
        self.le_cep.setStyleSheet(u"QLineEdit{	\n"
"	color: rgb(0, 0, 0);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: black;\n"
"    min-width: 10em;\n"
"}")

        self.horizontalLayout_7.addWidget(self.le_cep)


        self.verticalLayout_16.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_32 = QLabel(self.page_cadastrar)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setMinimumSize(QSize(61, 31))
        self.label_32.setMaximumSize(QSize(61, 31))
        self.label_32.setPixmap(QPixmap(u"icone agendamento.png"))
        self.label_32.setScaledContents(True)
        self.label_32.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.label_32)

        self.label_59 = QLabel(self.page_cadastrar)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setMinimumSize(QSize(131, 20))
        self.label_59.setMaximumSize(QSize(131, 20))
        self.label_59.setFont(font3)
        self.label_59.setStyleSheet(u"QLabel {\n"
"	color: rgb(255, 255, 255);\n"
"    \n"
"	background-color: rgb(144, 0, 0);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: black;\n"
"}")
        self.label_59.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.label_59)

        self.le_endereco = QLineEdit(self.page_cadastrar)
        self.le_endereco.setObjectName(u"le_endereco")
        self.le_endereco.setFont(font8)
        self.le_endereco.setStyleSheet(u"QLineEdit{	\n"
"	color: rgb(0, 0, 0);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: black;\n"
"    min-width: 10em;\n"
"}\n"
"")

        self.horizontalLayout_8.addWidget(self.le_endereco)


        self.verticalLayout_16.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_33 = QLabel(self.page_cadastrar)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setMinimumSize(QSize(61, 31))
        self.label_33.setMaximumSize(QSize(61, 31))
        self.label_33.setPixmap(QPixmap(u"icone agendamento.png"))
        self.label_33.setScaledContents(True)
        self.label_33.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.label_33)

        self.label_58 = QLabel(self.page_cadastrar)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setMinimumSize(QSize(131, 20))
        self.label_58.setMaximumSize(QSize(131, 20))
        self.label_58.setFont(font3)
        self.label_58.setStyleSheet(u"QLabel {\n"
"	color: rgb(255, 255, 255);\n"
"    \n"
"	background-color: rgb(144, 0, 0);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: black;\n"
"}")
        self.label_58.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.label_58)

        self.le_numero = QLineEdit(self.page_cadastrar)
        self.le_numero.setObjectName(u"le_numero")
        self.le_numero.setFont(font8)
        self.le_numero.setStyleSheet(u"QLineEdit{	\n"
"	color: rgb(0, 0, 0);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: black;\n"
"    min-width: 10em;\n"
"}")

        self.horizontalLayout_9.addWidget(self.le_numero)


        self.verticalLayout_16.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_34 = QLabel(self.page_cadastrar)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setMinimumSize(QSize(61, 31))
        self.label_34.setMaximumSize(QSize(61, 31))
        self.label_34.setPixmap(QPixmap(u"icone agendamento.png"))
        self.label_34.setScaledContents(True)
        self.label_34.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.label_34)

        self.label_57 = QLabel(self.page_cadastrar)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setMinimumSize(QSize(131, 20))
        self.label_57.setMaximumSize(QSize(131, 20))
        self.label_57.setFont(font3)
        self.label_57.setStyleSheet(u"QLabel {\n"
"	color: rgb(255, 255, 255);\n"
"    \n"
"	background-color: rgb(144, 0, 0);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: black;\n"
"}")
        self.label_57.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.label_57)

        self.le_bairro = QLineEdit(self.page_cadastrar)
        self.le_bairro.setObjectName(u"le_bairro")
        self.le_bairro.setFont(font8)
        self.le_bairro.setStyleSheet(u"QLineEdit{	\n"
"	color: rgb(0, 0, 0);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: black;\n"
"    min-width: 10em;\n"
"}")

        self.horizontalLayout_10.addWidget(self.le_bairro)


        self.verticalLayout_16.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_35 = QLabel(self.page_cadastrar)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setMinimumSize(QSize(61, 31))
        self.label_35.setMaximumSize(QSize(61, 31))
        self.label_35.setPixmap(QPixmap(u"icone agendamento.png"))
        self.label_35.setScaledContents(True)
        self.label_35.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_12.addWidget(self.label_35)

        self.label_56 = QLabel(self.page_cadastrar)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setMinimumSize(QSize(131, 20))
        self.label_56.setMaximumSize(QSize(131, 20))
        self.label_56.setFont(font3)
        self.label_56.setStyleSheet(u"QLabel {\n"
"	color: rgb(255, 255, 255);\n"
"    \n"
"	background-color: rgb(144, 0, 0);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: black;\n"
"}")
        self.label_56.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_12.addWidget(self.label_56)

        self.le_cidade = QLineEdit(self.page_cadastrar)
        self.le_cidade.setObjectName(u"le_cidade")
        font9 = QFont()
        font9.setFamily(u"Courier New")
        font9.setPointSize(12)
        font9.setBold(True)
        font9.setUnderline(False)
        font9.setWeight(75)
        font9.setStrikeOut(False)
        font9.setKerning(True)
        self.le_cidade.setFont(font9)
        self.le_cidade.setStyleSheet(u"QLineEdit{	\n"
"	color: rgb(0, 0, 0);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: black;\n"
"    min-width: 10em;\n"
"}\n"
"")

        self.horizontalLayout_12.addWidget(self.le_cidade)


        self.verticalLayout_16.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_13 = QLabel(self.page_cadastrar)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_16.addWidget(self.label_13)

        self.btn_update_municipe = QPushButton(self.page_cadastrar)
        self.btn_update_municipe.setObjectName(u"btn_update_municipe")
        self.btn_update_municipe.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_update_municipe.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_16.addWidget(self.btn_update_municipe)

        self.label_51 = QLabel(self.page_cadastrar)
        self.label_51.setObjectName(u"label_51")

        self.horizontalLayout_16.addWidget(self.label_51)

        self.btn_novo_cadastro = QPushButton(self.page_cadastrar)
        self.btn_novo_cadastro.setObjectName(u"btn_novo_cadastro")
        self.btn_novo_cadastro.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_novo_cadastro.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_16.addWidget(self.btn_novo_cadastro)

        self.label_14 = QLabel(self.page_cadastrar)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_16.addWidget(self.label_14)


        self.verticalLayout_16.addLayout(self.horizontalLayout_16)

        self.stackedWidget.addWidget(self.page_cadastrar)
        self.page_sobre = QWidget()
        self.page_sobre.setObjectName(u"page_sobre")
        self.verticalLayout_5 = QVBoxLayout(self.page_sobre)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_7 = QLabel(self.page_sobre)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_2.addWidget(self.label_7)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_10 = QLabel(self.page_sobre)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_3.addWidget(self.label_10)

        self.label_2 = QLabel(self.page_sobre)
        self.label_2.setObjectName(u"label_2")
        font10 = QFont()
        font10.setFamily(u"Courier New")
        font10.setPointSize(60)
        font10.setBold(True)
        font10.setWeight(75)
        self.label_2.setFont(font10)
        self.label_2.setTextFormat(Qt.MarkdownText)
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_2)

        self.label_8 = QLabel(self.page_sobre)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_3.addWidget(self.label_8)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        self.label_9 = QLabel(self.page_sobre)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_2.addWidget(self.label_9)


        self.verticalLayout_5.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.page_sobre)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_4 = QLabel(self.page_sobre)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_4.addWidget(self.label_4)

        self.label = QLabel(self.page_sobre)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(411, 141))
        self.label.setMaximumSize(QSize(411, 141))
        self.label.setPixmap(QPixmap(u"SEQUAV.jpg"))
        self.label.setScaledContents(True)

        self.verticalLayout_4.addWidget(self.label)

        self.label_6 = QLabel(self.page_sobre)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_4.addWidget(self.label_6)


        self.horizontalLayout_3.addLayout(self.verticalLayout_4)

        self.label_5 = QLabel(self.page_sobre)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_3.addWidget(self.label_5)


        self.verticalLayout_5.addLayout(self.horizontalLayout_3)

        self.stackedWidget.addWidget(self.page_sobre)

        self.verticalLayout.addWidget(self.stackedWidget)


        self.verticalLayout_13.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Sistema de Agendamentos DGS", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"HOME", None))
        self.btn_cadastrar.setText(QCoreApplication.translate("MainWindow", u"CADASTRAR", None))
        self.btn_cadastrados.setText(QCoreApplication.translate("MainWindow", u"MUNICIPES", None))
        self.btn_agendamento.setText(QCoreApplication.translate("MainWindow", u"AGENDAMENTO", None))
        self.btn_sobre.setText(QCoreApplication.translate("MainWindow", u"SOBRE", None))
        self.label_22.setText("")
        self.label_20.setText("")
        self.btn_new_user.setText(QCoreApplication.translate("MainWindow", u"NOVO USUARIO", None))
        self.label_21.setText("")
        self.label_18.setText("")
        self.label_74.setText("")
        self.label_23.setText("")
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"NOVO USUARIO", None))
        self.label_47.setText("")
        self.le_novo_login.setPlaceholderText(QCoreApplication.translate("MainWindow", u"LOGIN", None))
        self.le_novo_usuario.setPlaceholderText(QCoreApplication.translate("MainWindow", u"NOME DE USUARIO", None))
        self.le_senha1.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Senha", None))
        self.le_senha2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Repetir Senha", None))
        self.cb_users.setItemText(0, QCoreApplication.translate("MainWindow", u"user", None))
        self.cb_users.setItemText(1, QCoreApplication.translate("MainWindow", u"admin", None))

        self.bt_cadastrar_usuario.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.label_46.setText("")
        self.le_usuario_deletar.setText("")
        self.le_usuario_deletar.setPlaceholderText(QCoreApplication.translate("MainWindow", u"NOME DE USUARIO", None))
        self.le_senha_deletar.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Senha admin", None))
        self.bt_deletar_usuario.setText(QCoreApplication.translate("MainWindow", u"DELETAR", None))
        self.label_48.setText("")
        self.label_39.setText("")
        self.label_17.setText("")
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"MUNICIPES CADASTRADOS", None))
        self.label_26.setText("")
        self.label_38.setText("")
        self.label_41.setText("")
        self.le_update_municipe.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.btn_update_municipe_id.setText(QCoreApplication.translate("MainWindow", u"ATUALIZAR DADOS", None))
        self.le_delete_municipe.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ID", None))
        self.btn_delete_municipe.setText(QCoreApplication.translate("MainWindow", u"DELETAR", None))
        self.label_40.setText("")
        self.label_53.setText("")
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"NOME", None))
        self.label_54.setText("")
        self.le_pesquisa_municipe.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Filtro", None))
        self.label_55.setText("")
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"AGENDAMENTO", None))
        self.label_45.setText("")
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Selecione um Municipe Cadastrado", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Data do Agendamento", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"Hor\u00e1rio do Agendamento", None))
        self.btn_agendar.setText(QCoreApplication.translate("MainWindow", u"AGENDAR", None))
        self.label_50.setText("")
        self.label_72.setText(QCoreApplication.translate("MainWindow", u"DATA", None))
        self.le_filtro_data.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Filtro", None))
        self.label_68.setText("")
        self.label_69.setText("")
        self.label_12.setText("")
        self.label_67.setText("")
        self.label_11.setText("")
        self.label_71.setText("")
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"CADASTRO DE MUNICIPE", None))
        self.label_73.setText("")
        self.label_70.setText("")
        self.label_16.setText("")
        self.label_15.setText("")
        self.label_19.setText("")
        self.label_66.setText(QCoreApplication.translate("MainWindow", u"NOME", None))
        self.le_nome.setPlaceholderText(QCoreApplication.translate("MainWindow", u"NOME", None))
        self.label_29.setText("")
        self.label_65.setText(QCoreApplication.translate("MainWindow", u"RG", None))
        self.lv_rg.setText("")
        self.lv_rg.setPlaceholderText(QCoreApplication.translate("MainWindow", u"RG", None))
        self.label_30.setText("")
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"CPF", None))
        self.le_cpf.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CPF", None))
        self.label_37.setText("")
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"DATA DE NASCIMENTO", None))
        self.label_42.setText("")
        self.label_62.setText(QCoreApplication.translate("MainWindow", u"TELEFONE", None))
        self.le_telefone.setPlaceholderText(QCoreApplication.translate("MainWindow", u"TELEFONE", None))
        self.label_36.setText("")
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"INSTITUI\u00c7\u00c3O", None))
        self.le_instituicao.setText("")
        self.le_instituicao.setPlaceholderText(QCoreApplication.translate("MainWindow", u"INSTITUI\u00c7\u00c3O", None))
        self.label_31.setText("")
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"CEP", None))
        self.le_cep.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CEP", None))
        self.label_32.setText("")
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"ENDERE\u00c7O", None))
        self.le_endereco.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ENDERE\u00c7O", None))
        self.label_33.setText("")
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"NUMERO", None))
        self.le_numero.setPlaceholderText(QCoreApplication.translate("MainWindow", u"NUMERO", None))
        self.label_34.setText("")
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"BAIRRO", None))
        self.le_bairro.setText("")
        self.le_bairro.setPlaceholderText(QCoreApplication.translate("MainWindow", u"BAIRRO", None))
        self.label_35.setText("")
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"CIDADE", None))
        self.le_cidade.setText("")
        self.le_cidade.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CIDADE", None))
        self.label_13.setText("")
        self.btn_update_municipe.setText(QCoreApplication.translate("MainWindow", u"ATUALIZAR", None))
        self.label_51.setText("")
        self.btn_novo_cadastro.setText(QCoreApplication.translate("MainWindow", u"CADASTRAR", None))
        self.label_14.setText("")
        self.label_7.setText("")
        self.label_10.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"DESENVOLVEDOR", None))
        self.label_8.setText("")
        self.label_9.setText("")
        self.label_3.setText("")
        self.label_4.setText("")
        self.label.setText("")
        self.label_6.setText("")
        self.label_5.setText("")
    # retranslateUi

