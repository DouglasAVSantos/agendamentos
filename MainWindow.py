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

import icon

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1205, 859)
        icon = QIcon()
        icon.addFile(u"logo.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAnimated(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_21 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_menu_home = QPushButton(self.centralwidget)
        self.btn_menu_home.setObjectName(u"btn_menu_home")
        self.btn_menu_home.setMinimumSize(QSize(186, 0))
        self.btn_menu_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_menu_home.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout.addWidget(self.btn_menu_home, 0, Qt.AlignTop)

        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.btn_menu_cadastrar = QPushButton(self.centralwidget)
        self.btn_menu_cadastrar.setObjectName(u"btn_menu_cadastrar")
        self.btn_menu_cadastrar.setMinimumSize(QSize(186, 0))
        self.btn_menu_cadastrar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_menu_cadastrar.setStyleSheet(u"QPushButton {\n"
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
        self.btn_menu_cadastrar.setCheckable(False)
        self.btn_menu_cadastrar.setAutoExclusive(True)
        self.btn_menu_cadastrar.setAutoRepeatDelay(300)
        self.btn_menu_cadastrar.setAutoRepeatInterval(3000)

        self.verticalLayout_20.addWidget(self.btn_menu_cadastrar, 0, Qt.AlignTop)

        self.frame_cadastrar = QFrame(self.centralwidget)
        self.frame_cadastrar.setObjectName(u"frame_cadastrar")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_cadastrar.sizePolicy().hasHeightForWidth())
        self.frame_cadastrar.setSizePolicy(sizePolicy)
        self.frame_cadastrar.setMaximumSize(QSize(16777215, 0))
        self.frame_cadastrar.setStyleSheet(u"background-color: rgb(240, 240, 240);\n"
"")
        self.frame_cadastrar.setFrameShape(QFrame.StyledPanel)
        self.frame_cadastrar.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_cadastrar)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.btn_new_user = QPushButton(self.frame_cadastrar)
        self.btn_new_user.setObjectName(u"btn_new_user")
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
"\n"
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

        self.verticalLayout.addWidget(self.btn_new_user)

        self.btn_new_municipe = QPushButton(self.frame_cadastrar)
        self.btn_new_municipe.setObjectName(u"btn_new_municipe")
        self.btn_new_municipe.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_new_municipe.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"    \n"
"	background-color: rgb(144, 0, 0);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: black;\n"
"    font: bold 14px;\n"
"\n"
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

        self.verticalLayout.addWidget(self.btn_new_municipe)

        self.btn_new_agendamento = QPushButton(self.frame_cadastrar)
        self.btn_new_agendamento.setObjectName(u"btn_new_agendamento")
        self.btn_new_agendamento.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_new_agendamento.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"    \n"
"	background-color: rgb(144, 0, 0);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: black;\n"
"    font: bold 14px;\n"
"\n"
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

        self.verticalLayout.addWidget(self.btn_new_agendamento)


        self.verticalLayout_20.addWidget(self.frame_cadastrar)


        self.horizontalLayout.addLayout(self.verticalLayout_20)

        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.btn_menu_municipes = QPushButton(self.centralwidget)
        self.btn_menu_municipes.setObjectName(u"btn_menu_municipes")
        self.btn_menu_municipes.setMinimumSize(QSize(186, 0))
        self.btn_menu_municipes.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_menu_municipes.setStyleSheet(u"QPushButton {\n"
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
        self.btn_menu_municipes.setAutoRepeat(False)
        self.btn_menu_municipes.setAutoExclusive(False)
        self.btn_menu_municipes.setAutoRepeatDelay(300)
        self.btn_menu_municipes.setAutoRepeatInterval(3000)

        self.verticalLayout_18.addWidget(self.btn_menu_municipes, 0, Qt.AlignTop)

        self.frame_municipes = QFrame(self.centralwidget)
        self.frame_municipes.setObjectName(u"frame_municipes")
        sizePolicy.setHeightForWidth(self.frame_municipes.sizePolicy().hasHeightForWidth())
        self.frame_municipes.setSizePolicy(sizePolicy)
        self.frame_municipes.setMaximumSize(QSize(16777215, 0))
        self.frame_municipes.setStyleSheet(u"background-color: rgb(240, 240, 240);")
        self.frame_municipes.setFrameShape(QFrame.StyledPanel)
        self.frame_municipes.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_municipes)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.btn_municipes_cadastrados = QPushButton(self.frame_municipes)
        self.btn_municipes_cadastrados.setObjectName(u"btn_municipes_cadastrados")
        self.btn_municipes_cadastrados.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_municipes_cadastrados.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"    \n"
"	background-color: rgb(144, 0, 0);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: black;\n"
"    font: bold 14px;\n"
"\n"
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

        self.verticalLayout_13.addWidget(self.btn_municipes_cadastrados)

        self.btn_alterar_municipes_cadastros = QPushButton(self.frame_municipes)
        self.btn_alterar_municipes_cadastros.setObjectName(u"btn_alterar_municipes_cadastros")
        self.btn_alterar_municipes_cadastros.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_alterar_municipes_cadastros.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"    \n"
"	background-color: rgb(144, 0, 0);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: black;\n"
"    font: bold 14px;\n"
"\n"
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

        self.verticalLayout_13.addWidget(self.btn_alterar_municipes_cadastros)


        self.verticalLayout_18.addWidget(self.frame_municipes)


        self.horizontalLayout.addLayout(self.verticalLayout_18)

        self.btn_menu_agendamento = QPushButton(self.centralwidget)
        self.btn_menu_agendamento.setObjectName(u"btn_menu_agendamento")
        self.btn_menu_agendamento.setMinimumSize(QSize(186, 0))
        self.btn_menu_agendamento.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_menu_agendamento.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout.addWidget(self.btn_menu_agendamento, 0, Qt.AlignTop)

        self.btn_menu_sobre = QPushButton(self.centralwidget)
        self.btn_menu_sobre.setObjectName(u"btn_menu_sobre")
        self.btn_menu_sobre.setMinimumSize(QSize(186, 0))
        self.btn_menu_sobre.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_menu_sobre.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout.addWidget(self.btn_menu_sobre, 0, Qt.AlignTop)


        self.verticalLayout_21.addLayout(self.horizontalLayout)

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
        self.label_49 = QLabel(self.frame_2)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setPixmap(QPixmap(u"novo_usuario.png"))
        self.label_49.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_49)


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
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_13.sizePolicy().hasHeightForWidth())
        self.frame_13.setSizePolicy(sizePolicy1)
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
        font = QFont()
        font.setPointSize(12)
        self.cb_users.setFont(font)
        self.cb_users.setLayoutDirection(Qt.LeftToRight)
        self.cb_users.setSizeAdjustPolicy(QComboBox.AdjustToContents)

        self.verticalLayout_33.addWidget(self.cb_users)

        self.bt_cadastrar_usuario = QPushButton(self.frame_13)
        self.bt_cadastrar_usuario.setObjectName(u"bt_cadastrar_usuario")
        self.bt_cadastrar_usuario.setMinimumSize(QSize(151, 31))
        self.bt_cadastrar_usuario.setMaximumSize(QSize(151, 31))
        font1 = QFont()
        font1.setFamily(u"Courier")
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setWeight(75)
        self.bt_cadastrar_usuario.setFont(font1)
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
        sizePolicy1.setHeightForWidth(self.frame_14.sizePolicy().hasHeightForWidth())
        self.frame_14.setSizePolicy(sizePolicy1)
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
        self.bt_deletar_usuario.setFont(font1)
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


        self.verticalLayout_17.addWidget(self.frame_3, 0, Qt.AlignTop)

        self.stackedWidget.addWidget(self.page_new_user)
        self.page_cadastrados = QWidget()
        self.page_cadastrados.setObjectName(u"page_cadastrados")
        self.verticalLayout_14 = QVBoxLayout(self.page_cadastrados)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_17 = QLabel(self.page_cadastrados)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setPixmap(QPixmap(u"municipes_cadastrados.png"))
        self.label_17.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_17)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_26 = QLabel(self.page_cadastrados)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setMinimumSize(QSize(91, 81))
        self.label_26.setMaximumSize(QSize(91, 81))
        self.label_26.setPixmap(QPixmap(u"LUPA.png"))
        self.label_26.setScaledContents(True)

        self.horizontalLayout_18.addWidget(self.label_26)

        self.frame_20 = QFrame(self.page_cadastrados)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.frame_20)
        self.formLayout.setObjectName(u"formLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.rb_instituicao = QRadioButton(self.frame_20)
        self.rb_instituicao.setObjectName(u"rb_instituicao")
        self.rb_instituicao.setCheckable(True)
        self.rb_instituicao.setChecked(False)
        self.rb_instituicao.setAutoExclusive(True)

        self.gridLayout.addWidget(self.rb_instituicao, 0, 1, 2, 1)

        self.rb_nome = QRadioButton(self.frame_20)
        self.rb_nome.setObjectName(u"rb_nome")
        self.rb_nome.setChecked(True)

        self.gridLayout.addWidget(self.rb_nome, 0, 0, 1, 1)

        self.rb_cep = QRadioButton(self.frame_20)
        self.rb_cep.setObjectName(u"rb_cep")

        self.gridLayout.addWidget(self.rb_cep, 2, 1, 1, 1)

        self.rb_rg = QRadioButton(self.frame_20)
        self.rb_rg.setObjectName(u"rb_rg")

        self.gridLayout.addWidget(self.rb_rg, 1, 0, 2, 1)

        self.rb_telefone = QRadioButton(self.frame_20)
        self.rb_telefone.setObjectName(u"rb_telefone")

        self.gridLayout.addWidget(self.rb_telefone, 5, 0, 1, 1)

        self.rb_endereco = QRadioButton(self.frame_20)
        self.rb_endereco.setObjectName(u"rb_endereco")

        self.gridLayout.addWidget(self.rb_endereco, 3, 1, 1, 1)

        self.rb_bairro = QRadioButton(self.frame_20)
        self.rb_bairro.setObjectName(u"rb_bairro")

        self.gridLayout.addWidget(self.rb_bairro, 5, 1, 1, 1)

        self.rb_cidade = QRadioButton(self.frame_20)
        self.rb_cidade.setObjectName(u"rb_cidade")

        self.gridLayout.addWidget(self.rb_cidade, 6, 1, 1, 1)

        self.rb_cpf = QRadioButton(self.frame_20)
        self.rb_cpf.setObjectName(u"rb_cpf")

        self.gridLayout.addWidget(self.rb_cpf, 3, 0, 1, 1)


        self.formLayout.setLayout(0, QFormLayout.LabelRole, self.gridLayout)


        self.horizontalLayout_18.addWidget(self.frame_20)

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

        self.horizontalLayout_18.addWidget(self.le_pesquisa_municipe)


        self.verticalLayout_14.addLayout(self.horizontalLayout_18)

        self.tb_municipes_cadastrados = QTableWidget(self.page_cadastrados)
        if (self.tb_municipes_cadastrados.columnCount() < 11):
            self.tb_municipes_cadastrados.setColumnCount(11)
        __qtablewidgetitem = QTableWidgetItem()
        self.tb_municipes_cadastrados.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tb_municipes_cadastrados.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tb_municipes_cadastrados.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tb_municipes_cadastrados.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tb_municipes_cadastrados.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tb_municipes_cadastrados.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tb_municipes_cadastrados.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tb_municipes_cadastrados.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tb_municipes_cadastrados.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tb_municipes_cadastrados.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tb_municipes_cadastrados.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        self.tb_municipes_cadastrados.setObjectName(u"tb_municipes_cadastrados")
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(False)
        font2.setWeight(50)
        self.tb_municipes_cadastrados.setFont(font2)
        self.tb_municipes_cadastrados.setLineWidth(2)
        self.tb_municipes_cadastrados.setMidLineWidth(1)
        self.tb_municipes_cadastrados.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tb_municipes_cadastrados.setEditTriggers(QAbstractItemView.DoubleClicked)

        self.verticalLayout_14.addWidget(self.tb_municipes_cadastrados)

        self.stackedWidget.addWidget(self.page_cadastrados)
        self.page_novo_agendamento = QWidget()
        self.page_novo_agendamento.setObjectName(u"page_novo_agendamento")
        self.verticalLayout_12 = QVBoxLayout(self.page_novo_agendamento)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_14 = QLabel(self.page_novo_agendamento)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setPixmap(QPixmap(u"NOVO_AGENDAMENTO.png"))
        self.label_14.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_14)

        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setSpacing(0)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_15 = QLabel(self.page_novo_agendamento)
        self.label_15.setObjectName(u"label_15")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy2)
        self.label_15.setPixmap(QPixmap(u"SELE_MUNICIPE.png"))
        self.label_15.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_15)

        self.comboBox_municipe = QComboBox(self.page_novo_agendamento)
        self.comboBox_municipe.setObjectName(u"comboBox_municipe")
        sizePolicy2.setHeightForWidth(self.comboBox_municipe.sizePolicy().hasHeightForWidth())
        self.comboBox_municipe.setSizePolicy(sizePolicy2)
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

        self.verticalLayout_9.addWidget(self.comboBox_municipe)


        self.horizontalLayout_27.addLayout(self.verticalLayout_9)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setSpacing(0)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_44 = QLabel(self.page_novo_agendamento)
        self.label_44.setObjectName(u"label_44")

        self.horizontalLayout_24.addWidget(self.label_44)

        self.label_24 = QLabel(self.page_novo_agendamento)
        self.label_24.setObjectName(u"label_24")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_24.sizePolicy().hasHeightForWidth())
        self.label_24.setSizePolicy(sizePolicy3)
        self.label_24.setMaximumSize(QSize(309, 34))
        self.label_24.setStyleSheet(u"")
        self.label_24.setPixmap(QPixmap(u"DATA_AGENDAMENTO.png"))
        self.label_24.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_24.addWidget(self.label_24)

        self.label_45 = QLabel(self.page_novo_agendamento)
        self.label_45.setObjectName(u"label_45")

        self.horizontalLayout_24.addWidget(self.label_45)


        self.verticalLayout_8.addLayout(self.horizontalLayout_24)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setSpacing(0)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.label_16 = QLabel(self.page_novo_agendamento)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_25.addWidget(self.label_16)

        self.de_data_do_agendamento = QDateEdit(self.page_novo_agendamento)
        self.de_data_do_agendamento.setObjectName(u"de_data_do_agendamento")
        sizePolicy3.setHeightForWidth(self.de_data_do_agendamento.sizePolicy().hasHeightForWidth())
        self.de_data_do_agendamento.setSizePolicy(sizePolicy3)
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

        self.horizontalLayout_25.addWidget(self.de_data_do_agendamento)

        self.label_25 = QLabel(self.page_novo_agendamento)
        self.label_25.setObjectName(u"label_25")

        self.horizontalLayout_25.addWidget(self.label_25)


        self.verticalLayout_8.addLayout(self.horizontalLayout_25)


        self.horizontalLayout_27.addLayout(self.verticalLayout_8)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_50 = QLabel(self.page_novo_agendamento)
        self.label_50.setObjectName(u"label_50")

        self.horizontalLayout_14.addWidget(self.label_50)

        self.label_43 = QLabel(self.page_novo_agendamento)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setMaximumSize(QSize(308, 34))
        self.label_43.setStyleSheet(u"")
        self.label_43.setPixmap(QPixmap(u"horario_agendamento.png"))
        self.label_43.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_14.addWidget(self.label_43)

        self.label_51 = QLabel(self.page_novo_agendamento)
        self.label_51.setObjectName(u"label_51")

        self.horizontalLayout_14.addWidget(self.label_51)


        self.verticalLayout_6.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_28 = QLabel(self.page_novo_agendamento)
        self.label_28.setObjectName(u"label_28")

        self.horizontalLayout_19.addWidget(self.label_28)

        self.te_horario_agendamento = QTimeEdit(self.page_novo_agendamento)
        self.te_horario_agendamento.setObjectName(u"te_horario_agendamento")
        sizePolicy3.setHeightForWidth(self.te_horario_agendamento.sizePolicy().hasHeightForWidth())
        self.te_horario_agendamento.setSizePolicy(sizePolicy3)
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
        self.te_horario_agendamento.setReadOnly(False)
        self.te_horario_agendamento.setMaximumTime(QTime(17, 30, 0))
        self.te_horario_agendamento.setMinimumTime(QTime(8, 30, 0))

        self.horizontalLayout_19.addWidget(self.te_horario_agendamento)

        self.label_41 = QLabel(self.page_novo_agendamento)
        self.label_41.setObjectName(u"label_41")

        self.horizontalLayout_19.addWidget(self.label_41)


        self.verticalLayout_6.addLayout(self.horizontalLayout_19)


        self.horizontalLayout_27.addLayout(self.verticalLayout_6)

        self.btn_agendar = QPushButton(self.page_novo_agendamento)
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


        self.verticalLayout_12.addLayout(self.horizontalLayout_27)

        self.tb_agendamento = QTableWidget(self.page_novo_agendamento)
        if (self.tb_agendamento.columnCount() < 10):
            self.tb_agendamento.setColumnCount(10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tb_agendamento.setHorizontalHeaderItem(0, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tb_agendamento.setHorizontalHeaderItem(1, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tb_agendamento.setHorizontalHeaderItem(2, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tb_agendamento.setHorizontalHeaderItem(3, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tb_agendamento.setHorizontalHeaderItem(4, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tb_agendamento.setHorizontalHeaderItem(5, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tb_agendamento.setHorizontalHeaderItem(6, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tb_agendamento.setHorizontalHeaderItem(7, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tb_agendamento.setHorizontalHeaderItem(8, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tb_agendamento.setHorizontalHeaderItem(9, __qtablewidgetitem20)
        self.tb_agendamento.setObjectName(u"tb_agendamento")
        font3 = QFont()
        font3.setPointSize(12)
        font3.setBold(True)
        font3.setWeight(75)
        self.tb_agendamento.setFont(font3)
        self.tb_agendamento.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tb_agendamento.setSortingEnabled(True)

        self.verticalLayout_12.addWidget(self.tb_agendamento)

        self.stackedWidget.addWidget(self.page_novo_agendamento)
        self.page_agendados = QWidget()
        self.page_agendados.setObjectName(u"page_agendados")
        self.verticalLayout_16 = QVBoxLayout(self.page_agendados)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_4 = QLabel(self.page_agendados)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setPixmap(QPixmap(u"AGENDAMENTOS_CADASTRADOS.png"))
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.label_4)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.calendarWidget = QCalendarWidget(self.page_agendados)
        self.calendarWidget.setObjectName(u"calendarWidget")
        font4 = QFont()
        font4.setPointSize(15)
        self.calendarWidget.setFont(font4)
        self.calendarWidget.setCursor(QCursor(Qt.PointingHandCursor))
        self.calendarWidget.setLayoutDirection(Qt.LeftToRight)
        self.calendarWidget.setAutoFillBackground(True)
        self.calendarWidget.setGridVisible(True)
        self.calendarWidget.setVerticalHeaderFormat(QCalendarWidget.NoVerticalHeader)
        self.calendarWidget.setNavigationBarVisible(True)
        self.calendarWidget.setDateEditEnabled(True)

        self.horizontalLayout_20.addWidget(self.calendarWidget)


        self.verticalLayout_16.addLayout(self.horizontalLayout_20)

        self.lv_agendamentos_cadastrados = QListView(self.page_agendados)
        self.lv_agendamentos_cadastrados.setObjectName(u"lv_agendamentos_cadastrados")

        self.verticalLayout_16.addWidget(self.lv_agendamentos_cadastrados)

        self.stackedWidget.addWidget(self.page_agendados)
        self.page_novo_municipe = QWidget()
        self.page_novo_municipe.setObjectName(u"page_novo_municipe")
        self.verticalLayout_15 = QVBoxLayout(self.page_novo_municipe)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_12 = QLabel(self.page_novo_municipe)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setPixmap(QPixmap(u"NOVO_MUNICIPE.png"))
        self.label_12.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.label_12)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.frame_5 = QFrame(self.page_novo_municipe)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy3.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy3)
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_15.addWidget(self.frame_5)

        self.frame_4 = QFrame(self.page_novo_municipe)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy3.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy3)
        self.frame_4.setMinimumSize(QSize(681, 445))
        self.frame_4.setMaximumSize(QSize(681, 445))
        self.frame_4.setStyleSheet(u"border-width: 2px;\n"
"border-color: black;\n"
"border-style: solid;\n"
"display: inline-block;\n"
"border-radius: 8px")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_4)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_19 = QLabel(self.frame_4)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMinimumSize(QSize(61, 31))
        self.label_19.setMaximumSize(QSize(61, 31))
        self.label_19.setPixmap(QPixmap(u"icone agendamento.png"))
        self.label_19.setScaledContents(True)
        self.label_19.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_19)

        self.label_66 = QLabel(self.frame_4)
        self.label_66.setObjectName(u"label_66")
        self.label_66.setMinimumSize(QSize(131, 20))
        self.label_66.setMaximumSize(QSize(131, 20))
        font5 = QFont()
        font5.setPointSize(10)
        font5.setBold(True)
        font5.setItalic(False)
        font5.setWeight(75)
        self.label_66.setFont(font5)
        self.label_66.setStyleSheet(u"QLabel {\n"
"	color: rgb(255, 255, 255);\n"
"    \n"
"	background-color: rgb(144, 0, 0);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 0px;\n"
"    border-color: black;\n"
"}")
        self.label_66.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label_66)

        self.le_nome = QLineEdit(self.frame_4)
        self.le_nome.setObjectName(u"le_nome")
        font6 = QFont()
        font6.setFamily(u"Courier New")
        font6.setPointSize(12)
        font6.setBold(True)
        font6.setWeight(75)
        self.le_nome.setFont(font6)
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


        self.verticalLayout_7.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_29 = QLabel(self.frame_4)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setMinimumSize(QSize(61, 31))
        self.label_29.setMaximumSize(QSize(61, 31))
        self.label_29.setPixmap(QPixmap(u"icone agendamento.png"))
        self.label_29.setScaledContents(True)
        self.label_29.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_29)

        self.label_65 = QLabel(self.frame_4)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setMinimumSize(QSize(131, 20))
        self.label_65.setMaximumSize(QSize(131, 20))
        self.label_65.setFont(font5)
        self.label_65.setStyleSheet(u"QLabel {\n"
"	color: rgb(255, 255, 255);\n"
"    \n"
"	background-color: rgb(144, 0, 0);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 0px;\n"
"    border-color: black;\n"
"}")
        self.label_65.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_65)

        self.lv_rg = QLineEdit(self.frame_4)
        self.lv_rg.setObjectName(u"lv_rg")
        self.lv_rg.setFont(font6)
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


        self.verticalLayout_7.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_30 = QLabel(self.frame_4)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setMinimumSize(QSize(61, 31))
        self.label_30.setMaximumSize(QSize(61, 31))
        self.label_30.setPixmap(QPixmap(u"icone agendamento.png"))
        self.label_30.setScaledContents(True)
        self.label_30.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_30)

        self.label_64 = QLabel(self.frame_4)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setMinimumSize(QSize(131, 20))
        self.label_64.setMaximumSize(QSize(131, 20))
        self.label_64.setFont(font5)
        self.label_64.setStyleSheet(u"QLabel {\n"
"	color: rgb(255, 255, 255);\n"
"    \n"
"	background-color: rgb(144, 0, 0);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 0px;\n"
"    border-color: black;\n"
"}")
        self.label_64.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_64)

        self.le_cpf = QLineEdit(self.frame_4)
        self.le_cpf.setObjectName(u"le_cpf")
        self.le_cpf.setFont(font6)
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


        self.verticalLayout_7.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_37 = QLabel(self.frame_4)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setMinimumSize(QSize(61, 31))
        self.label_37.setMaximumSize(QSize(61, 31))
        self.label_37.setPixmap(QPixmap(u"icone agendamento.png"))
        self.label_37.setScaledContents(True)
        self.label_37.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.label_37)

        self.label_63 = QLabel(self.frame_4)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setMinimumSize(QSize(161, 20))
        self.label_63.setMaximumSize(QSize(161, 20))
        self.label_63.setFont(font5)
        self.label_63.setStyleSheet(u"QLabel {\n"
"	color: rgb(255, 255, 255);\n"
"    \n"
"	background-color: rgb(144, 0, 0);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 0px;\n"
"    border-color: black;\n"
"}")
        self.label_63.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.label_63)

        self.de_data_nascimento = QDateEdit(self.frame_4)
        self.de_data_nascimento.setObjectName(u"de_data_nascimento")
        self.de_data_nascimento.setFont(font6)
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


        self.verticalLayout_7.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_42 = QLabel(self.frame_4)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setMinimumSize(QSize(61, 31))
        self.label_42.setMaximumSize(QSize(61, 31))
        self.label_42.setPixmap(QPixmap(u"icone agendamento.png"))
        self.label_42.setScaledContents(True)
        self.label_42.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_21.addWidget(self.label_42)

        self.label_62 = QLabel(self.frame_4)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setMinimumSize(QSize(131, 20))
        self.label_62.setMaximumSize(QSize(131, 20))
        self.label_62.setFont(font5)
        self.label_62.setStyleSheet(u"QLabel {\n"
"	color: rgb(255, 255, 255);\n"
"    \n"
"	background-color: rgb(144, 0, 0);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 0px;\n"
"    border-color: black;\n"
"}")
        self.label_62.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_21.addWidget(self.label_62)

        self.le_telefone = QLineEdit(self.frame_4)
        self.le_telefone.setObjectName(u"le_telefone")
        self.le_telefone.setFont(font6)
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


        self.verticalLayout_7.addLayout(self.horizontalLayout_21)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_36 = QLabel(self.frame_4)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setMinimumSize(QSize(61, 31))
        self.label_36.setMaximumSize(QSize(61, 31))
        self.label_36.setPixmap(QPixmap(u"icone agendamento.png"))
        self.label_36.setScaledContents(True)
        self.label_36.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_11.addWidget(self.label_36)

        self.label_61 = QLabel(self.frame_4)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setMinimumSize(QSize(131, 20))
        self.label_61.setMaximumSize(QSize(131, 20))
        self.label_61.setFont(font5)
        self.label_61.setStyleSheet(u"QLabel {\n"
"	color: rgb(255, 255, 255);\n"
"    \n"
"	background-color: rgb(144, 0, 0);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 0px;\n"
"    border-color: black;\n"
"}")
        self.label_61.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_11.addWidget(self.label_61)

        self.le_instituicao = QLineEdit(self.frame_4)
        self.le_instituicao.setObjectName(u"le_instituicao")
        self.le_instituicao.setFont(font6)
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


        self.verticalLayout_7.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_31 = QLabel(self.frame_4)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setMinimumSize(QSize(61, 31))
        self.label_31.setMaximumSize(QSize(61, 31))
        self.label_31.setPixmap(QPixmap(u"icone agendamento.png"))
        self.label_31.setScaledContents(True)
        self.label_31.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.label_31)

        self.label_60 = QLabel(self.frame_4)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setMinimumSize(QSize(131, 20))
        self.label_60.setMaximumSize(QSize(131, 20))
        self.label_60.setFont(font5)
        self.label_60.setStyleSheet(u"QLabel {\n"
"	color: rgb(255, 255, 255);\n"
"    \n"
"	background-color: rgb(144, 0, 0);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 0px;\n"
"    border-color: black;\n"
"}")
        self.label_60.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.label_60)

        self.le_cep = QLineEdit(self.frame_4)
        self.le_cep.setObjectName(u"le_cep")
        self.le_cep.setFont(font6)
        self.le_cep.setStyleSheet(u"QLineEdit{	\n"
"	color: rgb(0, 0, 0);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: black;\n"
"    min-width: 10em;\n"
"}")

        self.horizontalLayout_7.addWidget(self.le_cep)


        self.verticalLayout_7.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_32 = QLabel(self.frame_4)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setMinimumSize(QSize(61, 31))
        self.label_32.setMaximumSize(QSize(61, 31))
        self.label_32.setPixmap(QPixmap(u"icone agendamento.png"))
        self.label_32.setScaledContents(True)
        self.label_32.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.label_32)

        self.label_59 = QLabel(self.frame_4)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setMinimumSize(QSize(131, 20))
        self.label_59.setMaximumSize(QSize(131, 20))
        self.label_59.setFont(font5)
        self.label_59.setStyleSheet(u"QLabel {\n"
"	color: rgb(255, 255, 255);\n"
"    \n"
"	background-color: rgb(144, 0, 0);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 0px;\n"
"    border-color: black;\n"
"}")
        self.label_59.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.label_59)

        self.le_endereco = QLineEdit(self.frame_4)
        self.le_endereco.setObjectName(u"le_endereco")
        self.le_endereco.setFont(font6)
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


        self.verticalLayout_7.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_33 = QLabel(self.frame_4)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setMinimumSize(QSize(61, 31))
        self.label_33.setMaximumSize(QSize(61, 31))
        self.label_33.setPixmap(QPixmap(u"icone agendamento.png"))
        self.label_33.setScaledContents(True)
        self.label_33.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.label_33)

        self.label_58 = QLabel(self.frame_4)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setMinimumSize(QSize(131, 20))
        self.label_58.setMaximumSize(QSize(131, 20))
        self.label_58.setFont(font5)
        self.label_58.setStyleSheet(u"QLabel {\n"
"	color: rgb(255, 255, 255);\n"
"    \n"
"	background-color: rgb(144, 0, 0);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 0px;\n"
"    border-color: black;\n"
"}")
        self.label_58.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.label_58)

        self.le_numero = QLineEdit(self.frame_4)
        self.le_numero.setObjectName(u"le_numero")
        self.le_numero.setFont(font6)
        self.le_numero.setStyleSheet(u"QLineEdit{	\n"
"	color: rgb(0, 0, 0);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: black;\n"
"    min-width: 10em;\n"
"}")

        self.horizontalLayout_9.addWidget(self.le_numero)


        self.verticalLayout_7.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_34 = QLabel(self.frame_4)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setMinimumSize(QSize(61, 31))
        self.label_34.setMaximumSize(QSize(61, 31))
        self.label_34.setPixmap(QPixmap(u"icone agendamento.png"))
        self.label_34.setScaledContents(True)
        self.label_34.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.label_34)

        self.label_57 = QLabel(self.frame_4)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setMinimumSize(QSize(131, 20))
        self.label_57.setMaximumSize(QSize(131, 20))
        self.label_57.setFont(font5)
        self.label_57.setStyleSheet(u"QLabel {\n"
"	color: rgb(255, 255, 255);\n"
"    \n"
"	background-color: rgb(144, 0, 0);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 0px;\n"
"    border-color: black;\n"
"}")
        self.label_57.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.label_57)

        self.le_bairro = QLineEdit(self.frame_4)
        self.le_bairro.setObjectName(u"le_bairro")
        self.le_bairro.setFont(font6)
        self.le_bairro.setStyleSheet(u"QLineEdit{	\n"
"	color: rgb(0, 0, 0);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: black;\n"
"    min-width: 10em;\n"
"}")

        self.horizontalLayout_10.addWidget(self.le_bairro)


        self.verticalLayout_7.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_35 = QLabel(self.frame_4)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setMinimumSize(QSize(61, 31))
        self.label_35.setMaximumSize(QSize(61, 31))
        self.label_35.setPixmap(QPixmap(u"icone agendamento.png"))
        self.label_35.setScaledContents(True)
        self.label_35.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_12.addWidget(self.label_35)

        self.label_56 = QLabel(self.frame_4)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setMinimumSize(QSize(131, 20))
        self.label_56.setMaximumSize(QSize(131, 20))
        self.label_56.setFont(font5)
        self.label_56.setStyleSheet(u"QLabel {\n"
"	color: rgb(255, 255, 255);\n"
"    \n"
"	background-color: rgb(144, 0, 0);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 0px;\n"
"    border-color: black;\n"
"}")
        self.label_56.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_12.addWidget(self.label_56)

        self.le_cidade = QLineEdit(self.frame_4)
        self.le_cidade.setObjectName(u"le_cidade")
        font7 = QFont()
        font7.setFamily(u"Courier New")
        font7.setPointSize(12)
        font7.setBold(True)
        font7.setUnderline(False)
        font7.setWeight(75)
        font7.setStrikeOut(False)
        font7.setKerning(True)
        self.le_cidade.setFont(font7)
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


        self.verticalLayout_7.addLayout(self.horizontalLayout_12)


        self.horizontalLayout_15.addWidget(self.frame_4)

        self.frame_6 = QFrame(self.page_novo_municipe)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy3.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy3)
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_15.addWidget(self.frame_6)


        self.verticalLayout_15.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_38 = QLabel(self.page_novo_municipe)
        self.label_38.setObjectName(u"label_38")

        self.horizontalLayout_16.addWidget(self.label_38)

        self.btn_novo_cadastro = QPushButton(self.page_novo_municipe)
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

        self.label_27 = QLabel(self.page_novo_municipe)
        self.label_27.setObjectName(u"label_27")

        self.horizontalLayout_16.addWidget(self.label_27)


        self.verticalLayout_15.addLayout(self.horizontalLayout_16)

        self.stackedWidget.addWidget(self.page_novo_municipe)
        self.page_att_municipe = QWidget()
        self.page_att_municipe.setObjectName(u"page_att_municipe")
        self.verticalLayout_19 = QVBoxLayout(self.page_att_municipe)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.label_147 = QLabel(self.page_att_municipe)
        self.label_147.setObjectName(u"label_147")
        self.label_147.setLayoutDirection(Qt.LeftToRight)
        self.label_147.setPixmap(QPixmap(u"att_municipe.png"))
        self.label_147.setScaledContents(False)
        self.label_147.setAlignment(Qt.AlignCenter)

        self.verticalLayout_19.addWidget(self.label_147)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label_11 = QLabel(self.page_att_municipe)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_23.addWidget(self.label_11)

        self.cb_municipes_att = QComboBox(self.page_att_municipe)
        self.cb_municipes_att.setObjectName(u"cb_municipes_att")
        self.cb_municipes_att.setFont(font6)
        self.cb_municipes_att.setMaxVisibleItems(10)

        self.horizontalLayout_23.addWidget(self.cb_municipes_att)

        self.btn_lupa = QPushButton(self.page_att_municipe)
        self.btn_lupa.setObjectName(u"btn_lupa")
        self.btn_lupa.setMinimumSize(QSize(61, 31))
        self.btn_lupa.setMaximumSize(QSize(61, 31))
        self.btn_lupa.setAutoFillBackground(False)
        self.btn_lupa.setStyleSheet(u"image: url(:/newPrefix/LUPA.png);\n"
"background-color: rgb(240, 240, 240);")

        self.horizontalLayout_23.addWidget(self.btn_lupa)

        self.label_13 = QLabel(self.page_att_municipe)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_23.addWidget(self.label_13)


        self.verticalLayout_19.addLayout(self.horizontalLayout_23)

        self.horizontalLayout_57 = QHBoxLayout()
        self.horizontalLayout_57.setSpacing(0)
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.frame_17 = QFrame(self.page_att_municipe)
        self.frame_17.setObjectName(u"frame_17")
        sizePolicy3.setHeightForWidth(self.frame_17.sizePolicy().hasHeightForWidth())
        self.frame_17.setSizePolicy(sizePolicy3)
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_57.addWidget(self.frame_17)

        self.frame_18 = QFrame(self.page_att_municipe)
        self.frame_18.setObjectName(u"frame_18")
        sizePolicy3.setHeightForWidth(self.frame_18.sizePolicy().hasHeightForWidth())
        self.frame_18.setSizePolicy(sizePolicy3)
        self.frame_18.setMinimumSize(QSize(681, 445))
        self.frame_18.setMaximumSize(QSize(681, 445))
        self.frame_18.setStyleSheet(u"border-width: 2px;\n"
"border-color: black;\n"
"border-style: solid;\n"
"display: inline-block;\n"
"border-radius: 8px")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_40 = QVBoxLayout(self.frame_18)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.horizontalLayout_58 = QHBoxLayout()
        self.horizontalLayout_58.setObjectName(u"horizontalLayout_58")
        self.label_125 = QLabel(self.frame_18)
        self.label_125.setObjectName(u"label_125")
        self.label_125.setMinimumSize(QSize(61, 31))
        self.label_125.setMaximumSize(QSize(61, 31))
        self.label_125.setPixmap(QPixmap(u"icone agendamento.png"))
        self.label_125.setScaledContents(True)
        self.label_125.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_58.addWidget(self.label_125)

        self.label_126 = QLabel(self.frame_18)
        self.label_126.setObjectName(u"label_126")
        self.label_126.setMinimumSize(QSize(131, 20))
        self.label_126.setMaximumSize(QSize(131, 20))
        self.label_126.setFont(font5)
        self.label_126.setStyleSheet(u"QLabel {\n"
"	color: rgb(255, 255, 255);\n"
"    \n"
"	background-color: rgb(144, 0, 0);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 0px;\n"
"    border-color: black;\n"
"}")
        self.label_126.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_58.addWidget(self.label_126)

        self.le_nome_3 = QLineEdit(self.frame_18)
        self.le_nome_3.setObjectName(u"le_nome_3")
        self.le_nome_3.setFont(font6)
        self.le_nome_3.setStyleSheet(u"QLineEdit{	\n"
"	color: rgb(0, 0, 0);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: black;\n"
"    min-width: 10em;\n"
"}\n"
"")

        self.horizontalLayout_58.addWidget(self.le_nome_3)


        self.verticalLayout_40.addLayout(self.horizontalLayout_58)

        self.horizontalLayout_59 = QHBoxLayout()
        self.horizontalLayout_59.setObjectName(u"horizontalLayout_59")
        self.label_127 = QLabel(self.frame_18)
        self.label_127.setObjectName(u"label_127")
        self.label_127.setMinimumSize(QSize(61, 31))
        self.label_127.setMaximumSize(QSize(61, 31))
        self.label_127.setPixmap(QPixmap(u"icone agendamento.png"))
        self.label_127.setScaledContents(True)
        self.label_127.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_59.addWidget(self.label_127)

        self.label_128 = QLabel(self.frame_18)
        self.label_128.setObjectName(u"label_128")
        self.label_128.setMinimumSize(QSize(131, 20))
        self.label_128.setMaximumSize(QSize(131, 20))
        self.label_128.setFont(font5)
        self.label_128.setStyleSheet(u"QLabel {\n"
"	color: rgb(255, 255, 255);\n"
"    \n"
"	background-color: rgb(144, 0, 0);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 0px;\n"
"    border-color: black;\n"
"}")
        self.label_128.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_59.addWidget(self.label_128)

        self.lv_rg_3 = QLineEdit(self.frame_18)
        self.lv_rg_3.setObjectName(u"lv_rg_3")
        self.lv_rg_3.setFont(font6)
        self.lv_rg_3.setStyleSheet(u"QLineEdit{	\n"
"	color: rgb(0, 0, 0);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: black;\n"
"    min-width: 10em;\n"
"}\n"
"")

        self.horizontalLayout_59.addWidget(self.lv_rg_3)


        self.verticalLayout_40.addLayout(self.horizontalLayout_59)

        self.horizontalLayout_60 = QHBoxLayout()
        self.horizontalLayout_60.setSpacing(6)
        self.horizontalLayout_60.setObjectName(u"horizontalLayout_60")
        self.label_129 = QLabel(self.frame_18)
        self.label_129.setObjectName(u"label_129")
        self.label_129.setMinimumSize(QSize(61, 31))
        self.label_129.setMaximumSize(QSize(61, 31))
        self.label_129.setPixmap(QPixmap(u"icone agendamento.png"))
        self.label_129.setScaledContents(True)
        self.label_129.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_60.addWidget(self.label_129)

        self.label_130 = QLabel(self.frame_18)
        self.label_130.setObjectName(u"label_130")
        self.label_130.setMinimumSize(QSize(131, 20))
        self.label_130.setMaximumSize(QSize(131, 20))
        self.label_130.setFont(font5)
        self.label_130.setStyleSheet(u"QLabel {\n"
"	color: rgb(255, 255, 255);\n"
"    \n"
"	background-color: rgb(144, 0, 0);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 0px;\n"
"    border-color: black;\n"
"}")
        self.label_130.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_60.addWidget(self.label_130)

        self.le_cpf_3 = QLineEdit(self.frame_18)
        self.le_cpf_3.setObjectName(u"le_cpf_3")
        self.le_cpf_3.setFont(font6)
        self.le_cpf_3.setStyleSheet(u"QLineEdit{	\n"
"	color: rgb(0, 0, 0);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: black;\n"
"    min-width: 10em;\n"
"}\n"
"")

        self.horizontalLayout_60.addWidget(self.le_cpf_3)


        self.verticalLayout_40.addLayout(self.horizontalLayout_60)

        self.horizontalLayout_61 = QHBoxLayout()
        self.horizontalLayout_61.setObjectName(u"horizontalLayout_61")
        self.label_131 = QLabel(self.frame_18)
        self.label_131.setObjectName(u"label_131")
        self.label_131.setMinimumSize(QSize(61, 31))
        self.label_131.setMaximumSize(QSize(61, 31))
        self.label_131.setPixmap(QPixmap(u"icone agendamento.png"))
        self.label_131.setScaledContents(True)
        self.label_131.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_61.addWidget(self.label_131)

        self.label_132 = QLabel(self.frame_18)
        self.label_132.setObjectName(u"label_132")
        self.label_132.setMinimumSize(QSize(161, 20))
        self.label_132.setMaximumSize(QSize(161, 20))
        self.label_132.setFont(font5)
        self.label_132.setStyleSheet(u"QLabel {\n"
"	color: rgb(255, 255, 255);\n"
"    \n"
"	background-color: rgb(144, 0, 0);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 0px;\n"
"    border-color: black;\n"
"}")
        self.label_132.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_61.addWidget(self.label_132)

        self.de_data_nascimento_3 = QDateEdit(self.frame_18)
        self.de_data_nascimento_3.setObjectName(u"de_data_nascimento_3")
        self.de_data_nascimento_3.setFont(font6)
        self.de_data_nascimento_3.setStyleSheet(u"QLineEdit{	\n"
"	color: rgb(0, 0, 0);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: black;\n"
"    min-width: 10em;\n"
"}")
        self.de_data_nascimento_3.setCalendarPopup(True)

        self.horizontalLayout_61.addWidget(self.de_data_nascimento_3)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_61.addItem(self.horizontalSpacer_11)


        self.verticalLayout_40.addLayout(self.horizontalLayout_61)

        self.horizontalLayout_62 = QHBoxLayout()
        self.horizontalLayout_62.setObjectName(u"horizontalLayout_62")
        self.label_133 = QLabel(self.frame_18)
        self.label_133.setObjectName(u"label_133")
        self.label_133.setMinimumSize(QSize(61, 31))
        self.label_133.setMaximumSize(QSize(61, 31))
        self.label_133.setPixmap(QPixmap(u"icone agendamento.png"))
        self.label_133.setScaledContents(True)
        self.label_133.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_62.addWidget(self.label_133)

        self.label_134 = QLabel(self.frame_18)
        self.label_134.setObjectName(u"label_134")
        self.label_134.setMinimumSize(QSize(131, 20))
        self.label_134.setMaximumSize(QSize(131, 20))
        self.label_134.setFont(font5)
        self.label_134.setStyleSheet(u"QLabel {\n"
"	color: rgb(255, 255, 255);\n"
"    \n"
"	background-color: rgb(144, 0, 0);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 0px;\n"
"    border-color: black;\n"
"}")
        self.label_134.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_62.addWidget(self.label_134)

        self.le_telefone_3 = QLineEdit(self.frame_18)
        self.le_telefone_3.setObjectName(u"le_telefone_3")
        self.le_telefone_3.setFont(font6)
        self.le_telefone_3.setStyleSheet(u"QLineEdit{	\n"
"	color: rgb(0, 0, 0);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: black;\n"
"    min-width: 10em;\n"
"}\n"
"")

        self.horizontalLayout_62.addWidget(self.le_telefone_3)


        self.verticalLayout_40.addLayout(self.horizontalLayout_62)

        self.horizontalLayout_63 = QHBoxLayout()
        self.horizontalLayout_63.setObjectName(u"horizontalLayout_63")
        self.label_135 = QLabel(self.frame_18)
        self.label_135.setObjectName(u"label_135")
        self.label_135.setMinimumSize(QSize(61, 31))
        self.label_135.setMaximumSize(QSize(61, 31))
        self.label_135.setPixmap(QPixmap(u"icone agendamento.png"))
        self.label_135.setScaledContents(True)
        self.label_135.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_63.addWidget(self.label_135)

        self.label_136 = QLabel(self.frame_18)
        self.label_136.setObjectName(u"label_136")
        self.label_136.setMinimumSize(QSize(131, 20))
        self.label_136.setMaximumSize(QSize(131, 20))
        self.label_136.setFont(font5)
        self.label_136.setStyleSheet(u"QLabel {\n"
"	color: rgb(255, 255, 255);\n"
"    \n"
"	background-color: rgb(144, 0, 0);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 0px;\n"
"    border-color: black;\n"
"}")
        self.label_136.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_63.addWidget(self.label_136)

        self.le_instituicao_3 = QLineEdit(self.frame_18)
        self.le_instituicao_3.setObjectName(u"le_instituicao_3")
        self.le_instituicao_3.setFont(font6)
        self.le_instituicao_3.setStyleSheet(u"QLineEdit{	\n"
"	color: rgb(0, 0, 0);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: black;\n"
"    min-width: 10em;\n"
"}\n"
"")

        self.horizontalLayout_63.addWidget(self.le_instituicao_3)


        self.verticalLayout_40.addLayout(self.horizontalLayout_63)

        self.horizontalLayout_64 = QHBoxLayout()
        self.horizontalLayout_64.setObjectName(u"horizontalLayout_64")
        self.label_137 = QLabel(self.frame_18)
        self.label_137.setObjectName(u"label_137")
        self.label_137.setMinimumSize(QSize(61, 31))
        self.label_137.setMaximumSize(QSize(61, 31))
        self.label_137.setPixmap(QPixmap(u"icone agendamento.png"))
        self.label_137.setScaledContents(True)
        self.label_137.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_64.addWidget(self.label_137)

        self.label_138 = QLabel(self.frame_18)
        self.label_138.setObjectName(u"label_138")
        self.label_138.setMinimumSize(QSize(131, 20))
        self.label_138.setMaximumSize(QSize(131, 20))
        self.label_138.setFont(font5)
        self.label_138.setStyleSheet(u"QLabel {\n"
"	color: rgb(255, 255, 255);\n"
"    \n"
"	background-color: rgb(144, 0, 0);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 0px;\n"
"    border-color: black;\n"
"}")
        self.label_138.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_64.addWidget(self.label_138)

        self.le_cep_3 = QLineEdit(self.frame_18)
        self.le_cep_3.setObjectName(u"le_cep_3")
        self.le_cep_3.setFont(font6)
        self.le_cep_3.setStyleSheet(u"QLineEdit{	\n"
"	color: rgb(0, 0, 0);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: black;\n"
"    min-width: 10em;\n"
"}")

        self.horizontalLayout_64.addWidget(self.le_cep_3)


        self.verticalLayout_40.addLayout(self.horizontalLayout_64)

        self.horizontalLayout_65 = QHBoxLayout()
        self.horizontalLayout_65.setObjectName(u"horizontalLayout_65")
        self.label_139 = QLabel(self.frame_18)
        self.label_139.setObjectName(u"label_139")
        self.label_139.setMinimumSize(QSize(61, 31))
        self.label_139.setMaximumSize(QSize(61, 31))
        self.label_139.setPixmap(QPixmap(u"icone agendamento.png"))
        self.label_139.setScaledContents(True)
        self.label_139.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_65.addWidget(self.label_139)

        self.label_140 = QLabel(self.frame_18)
        self.label_140.setObjectName(u"label_140")
        self.label_140.setMinimumSize(QSize(131, 20))
        self.label_140.setMaximumSize(QSize(131, 20))
        self.label_140.setFont(font5)
        self.label_140.setStyleSheet(u"QLabel {\n"
"	color: rgb(255, 255, 255);\n"
"    \n"
"	background-color: rgb(144, 0, 0);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 0px;\n"
"    border-color: black;\n"
"}")
        self.label_140.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_65.addWidget(self.label_140)

        self.le_endereco_3 = QLineEdit(self.frame_18)
        self.le_endereco_3.setObjectName(u"le_endereco_3")
        self.le_endereco_3.setFont(font6)
        self.le_endereco_3.setStyleSheet(u"QLineEdit{	\n"
"	color: rgb(0, 0, 0);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: black;\n"
"    min-width: 10em;\n"
"}\n"
"")

        self.horizontalLayout_65.addWidget(self.le_endereco_3)


        self.verticalLayout_40.addLayout(self.horizontalLayout_65)

        self.horizontalLayout_66 = QHBoxLayout()
        self.horizontalLayout_66.setObjectName(u"horizontalLayout_66")
        self.label_141 = QLabel(self.frame_18)
        self.label_141.setObjectName(u"label_141")
        self.label_141.setMinimumSize(QSize(61, 31))
        self.label_141.setMaximumSize(QSize(61, 31))
        self.label_141.setPixmap(QPixmap(u"icone agendamento.png"))
        self.label_141.setScaledContents(True)
        self.label_141.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_66.addWidget(self.label_141)

        self.label_142 = QLabel(self.frame_18)
        self.label_142.setObjectName(u"label_142")
        self.label_142.setMinimumSize(QSize(131, 20))
        self.label_142.setMaximumSize(QSize(131, 20))
        self.label_142.setFont(font5)
        self.label_142.setStyleSheet(u"QLabel {\n"
"	color: rgb(255, 255, 255);\n"
"    \n"
"	background-color: rgb(144, 0, 0);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 0px;\n"
"    border-color: black;\n"
"}")
        self.label_142.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_66.addWidget(self.label_142)

        self.le_numero_3 = QLineEdit(self.frame_18)
        self.le_numero_3.setObjectName(u"le_numero_3")
        self.le_numero_3.setFont(font6)
        self.le_numero_3.setStyleSheet(u"QLineEdit{	\n"
"	color: rgb(0, 0, 0);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: black;\n"
"    min-width: 10em;\n"
"}")

        self.horizontalLayout_66.addWidget(self.le_numero_3)


        self.verticalLayout_40.addLayout(self.horizontalLayout_66)

        self.horizontalLayout_67 = QHBoxLayout()
        self.horizontalLayout_67.setObjectName(u"horizontalLayout_67")
        self.label_143 = QLabel(self.frame_18)
        self.label_143.setObjectName(u"label_143")
        self.label_143.setMinimumSize(QSize(61, 31))
        self.label_143.setMaximumSize(QSize(61, 31))
        self.label_143.setPixmap(QPixmap(u"icone agendamento.png"))
        self.label_143.setScaledContents(True)
        self.label_143.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_67.addWidget(self.label_143)

        self.label_144 = QLabel(self.frame_18)
        self.label_144.setObjectName(u"label_144")
        self.label_144.setMinimumSize(QSize(131, 20))
        self.label_144.setMaximumSize(QSize(131, 20))
        self.label_144.setFont(font5)
        self.label_144.setStyleSheet(u"QLabel {\n"
"	color: rgb(255, 255, 255);\n"
"    \n"
"	background-color: rgb(144, 0, 0);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 0px;\n"
"    border-color: black;\n"
"}")
        self.label_144.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_67.addWidget(self.label_144)

        self.le_bairro_3 = QLineEdit(self.frame_18)
        self.le_bairro_3.setObjectName(u"le_bairro_3")
        self.le_bairro_3.setFont(font6)
        self.le_bairro_3.setStyleSheet(u"QLineEdit{	\n"
"	color: rgb(0, 0, 0);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: black;\n"
"    min-width: 10em;\n"
"}")

        self.horizontalLayout_67.addWidget(self.le_bairro_3)


        self.verticalLayout_40.addLayout(self.horizontalLayout_67)

        self.horizontalLayout_68 = QHBoxLayout()
        self.horizontalLayout_68.setObjectName(u"horizontalLayout_68")
        self.label_145 = QLabel(self.frame_18)
        self.label_145.setObjectName(u"label_145")
        self.label_145.setMinimumSize(QSize(61, 31))
        self.label_145.setMaximumSize(QSize(61, 31))
        self.label_145.setPixmap(QPixmap(u"icone agendamento.png"))
        self.label_145.setScaledContents(True)
        self.label_145.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_68.addWidget(self.label_145)

        self.label_146 = QLabel(self.frame_18)
        self.label_146.setObjectName(u"label_146")
        self.label_146.setMinimumSize(QSize(131, 20))
        self.label_146.setMaximumSize(QSize(131, 20))
        self.label_146.setFont(font5)
        self.label_146.setStyleSheet(u"QLabel {\n"
"	color: rgb(255, 255, 255);\n"
"    \n"
"	background-color: rgb(144, 0, 0);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 0px;\n"
"    border-color: black;\n"
"}")
        self.label_146.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_68.addWidget(self.label_146)

        self.le_cidade_3 = QLineEdit(self.frame_18)
        self.le_cidade_3.setObjectName(u"le_cidade_3")
        self.le_cidade_3.setFont(font7)
        self.le_cidade_3.setStyleSheet(u"QLineEdit{	\n"
"	color: rgb(0, 0, 0);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"    border-radius: 10px;\n"
"    border-color: black;\n"
"    min-width: 10em;\n"
"}\n"
"")

        self.horizontalLayout_68.addWidget(self.le_cidade_3)


        self.verticalLayout_40.addLayout(self.horizontalLayout_68)


        self.horizontalLayout_57.addWidget(self.frame_18)

        self.frame_19 = QFrame(self.page_att_municipe)
        self.frame_19.setObjectName(u"frame_19")
        sizePolicy3.setHeightForWidth(self.frame_19.sizePolicy().hasHeightForWidth())
        self.frame_19.setSizePolicy(sizePolicy3)
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_57.addWidget(self.frame_19)


        self.verticalLayout_19.addLayout(self.horizontalLayout_57)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setSpacing(0)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_39 = QLabel(self.page_att_municipe)
        self.label_39.setObjectName(u"label_39")

        self.horizontalLayout_22.addWidget(self.label_39)

        self.btn_update_municipe = QPushButton(self.page_att_municipe)
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

        self.horizontalLayout_22.addWidget(self.btn_update_municipe)

        self.label_40 = QLabel(self.page_att_municipe)
        self.label_40.setObjectName(u"label_40")

        self.horizontalLayout_22.addWidget(self.label_40)


        self.verticalLayout_19.addLayout(self.horizontalLayout_22)

        self.stackedWidget.addWidget(self.page_att_municipe)
        self.page_sobre = QWidget()
        self.page_sobre.setObjectName(u"page_sobre")
        self.verticalLayout_5 = QVBoxLayout(self.page_sobre)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_7 = QLabel(self.page_sobre)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_2.addWidget(self.label_7)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_10 = QLabel(self.page_sobre)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_3.addWidget(self.label_10)

        self.label_2 = QLabel(self.page_sobre)
        self.label_2.setObjectName(u"label_2")
        font8 = QFont()
        font8.setFamily(u"Courier New")
        font8.setPointSize(60)
        font8.setBold(True)
        font8.setWeight(75)
        self.label_2.setFont(font8)
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
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.page_sobre)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
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

        self.verticalLayout_21.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Sistema de Agendamentos DGS", None))
        self.btn_menu_home.setText(QCoreApplication.translate("MainWindow", u"HOME", None))
        self.btn_menu_cadastrar.setText(QCoreApplication.translate("MainWindow", u"CADASTRAR", None))
        self.btn_new_user.setText(QCoreApplication.translate("MainWindow", u"NOVO USUARIO", None))
        self.btn_new_municipe.setText(QCoreApplication.translate("MainWindow", u"NOVO MUNICIPE", None))
        self.btn_new_agendamento.setText(QCoreApplication.translate("MainWindow", u"NOVO AGENDAMENTO", None))
        self.btn_menu_municipes.setText(QCoreApplication.translate("MainWindow", u"MUNICIPES", None))
        self.btn_municipes_cadastrados.setText(QCoreApplication.translate("MainWindow", u"CADASTRADOS", None))
        self.btn_alterar_municipes_cadastros.setText(QCoreApplication.translate("MainWindow", u"ALTERAR CADASTRO", None))
        self.btn_menu_agendamento.setText(QCoreApplication.translate("MainWindow", u"AGENDADOS", None))
        self.btn_menu_sobre.setText(QCoreApplication.translate("MainWindow", u"SOBRE", None))
        self.label_22.setText("")
        self.label_20.setText("")
        self.label_21.setText("")
        self.label_18.setText("")
        self.label_74.setText("")
        self.label_23.setText("")
        self.label_49.setText("")
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
        self.label_17.setText("")
        self.label_26.setText("")
        self.rb_instituicao.setText(QCoreApplication.translate("MainWindow", u"INSTITUI\u00c7\u00c3O", None))
        self.rb_nome.setText(QCoreApplication.translate("MainWindow", u"NOME", None))
        self.rb_cep.setText(QCoreApplication.translate("MainWindow", u"CEP", None))
        self.rb_rg.setText(QCoreApplication.translate("MainWindow", u"RG", None))
        self.rb_telefone.setText(QCoreApplication.translate("MainWindow", u"TELEFONE", None))
        self.rb_endereco.setText(QCoreApplication.translate("MainWindow", u"ENDERE\u00c7O", None))
        self.rb_bairro.setText(QCoreApplication.translate("MainWindow", u"BAIRRO", None))
        self.rb_cidade.setText(QCoreApplication.translate("MainWindow", u"CIDADE", None))
        self.rb_cpf.setText(QCoreApplication.translate("MainWindow", u"CPF", None))
        self.le_pesquisa_municipe.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Filtro", None))
        ___qtablewidgetitem = self.tb_municipes_cadastrados.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"NOME", None));
        ___qtablewidgetitem1 = self.tb_municipes_cadastrados.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"RG", None));
        ___qtablewidgetitem2 = self.tb_municipes_cadastrados.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"CPF", None));
        ___qtablewidgetitem3 = self.tb_municipes_cadastrados.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"NASCIMENTO", None));
        ___qtablewidgetitem4 = self.tb_municipes_cadastrados.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"TELEFONE", None));
        ___qtablewidgetitem5 = self.tb_municipes_cadastrados.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"INSTITUI\u00c7\u00c3O", None));
        ___qtablewidgetitem6 = self.tb_municipes_cadastrados.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"CEP", None));
        ___qtablewidgetitem7 = self.tb_municipes_cadastrados.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"ENDERE\u00c7O", None));
        ___qtablewidgetitem8 = self.tb_municipes_cadastrados.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"NUMERO", None));
        ___qtablewidgetitem9 = self.tb_municipes_cadastrados.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"BAIRRO", None));
        ___qtablewidgetitem10 = self.tb_municipes_cadastrados.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"CIDADE", None));
        self.label_14.setText("")
        self.label_15.setText("")
        self.label_44.setText("")
        self.label_24.setText("")
        self.label_45.setText("")
        self.label_16.setText("")
        self.label_25.setText("")
        self.label_50.setText("")
        self.label_43.setText("")
        self.label_51.setText("")
        self.label_28.setText("")
        self.label_41.setText("")
        self.btn_agendar.setText(QCoreApplication.translate("MainWindow", u"AGENDAR", None))
        ___qtablewidgetitem11 = self.tb_agendamento.horizontalHeaderItem(0)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"DATA", None));
        ___qtablewidgetitem12 = self.tb_agendamento.horizontalHeaderItem(1)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"HOR\u00c1RIO 08:30 A 09:30", None));
        ___qtablewidgetitem13 = self.tb_agendamento.horizontalHeaderItem(2)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"HOR\u00c1RIO 09:30 A 10:30", None));
        ___qtablewidgetitem14 = self.tb_agendamento.horizontalHeaderItem(3)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"HOR\u00c1RIO 10:30 A 11:30", None));
        ___qtablewidgetitem15 = self.tb_agendamento.horizontalHeaderItem(4)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"HOR\u00c1RIO 11:30 A 12:30", None));
        ___qtablewidgetitem16 = self.tb_agendamento.horizontalHeaderItem(5)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"HOR\u00c1RIO 12:30  A 13:30", None));
        ___qtablewidgetitem17 = self.tb_agendamento.horizontalHeaderItem(6)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"HOR\u00c1RIO 13:30 A 14:30", None));
        ___qtablewidgetitem18 = self.tb_agendamento.horizontalHeaderItem(7)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"HOR\u00c1RIO 14:30 A 15:30", None));
        ___qtablewidgetitem19 = self.tb_agendamento.horizontalHeaderItem(8)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"HOR\u00c1RIO 15:30 A 16:30", None));
        ___qtablewidgetitem20 = self.tb_agendamento.horizontalHeaderItem(9)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"HOR\u00c1RIO 16:30 A 17:30", None));
        self.label_4.setText("")
        self.label_12.setText("")
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
        self.label_38.setText("")
        self.btn_novo_cadastro.setText(QCoreApplication.translate("MainWindow", u"CADASTRAR", None))
        self.label_27.setText("")
        self.label_147.setText("")
        self.label_11.setText("")
        self.btn_lupa.setText("")
        self.label_13.setText("")
        self.label_125.setText("")
        self.label_126.setText(QCoreApplication.translate("MainWindow", u"NOME", None))
        self.le_nome_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"NOME", None))
        self.label_127.setText("")
        self.label_128.setText(QCoreApplication.translate("MainWindow", u"RG", None))
        self.lv_rg_3.setText("")
        self.lv_rg_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"RG", None))
        self.label_129.setText("")
        self.label_130.setText(QCoreApplication.translate("MainWindow", u"CPF", None))
        self.le_cpf_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CPF", None))
        self.label_131.setText("")
        self.label_132.setText(QCoreApplication.translate("MainWindow", u"DATA DE NASCIMENTO", None))
        self.label_133.setText("")
        self.label_134.setText(QCoreApplication.translate("MainWindow", u"TELEFONE", None))
        self.le_telefone_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"TELEFONE", None))
        self.label_135.setText("")
        self.label_136.setText(QCoreApplication.translate("MainWindow", u"INSTITUI\u00c7\u00c3O", None))
        self.le_instituicao_3.setText("")
        self.le_instituicao_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"INSTITUI\u00c7\u00c3O", None))
        self.label_137.setText("")
        self.label_138.setText(QCoreApplication.translate("MainWindow", u"CEP", None))
        self.le_cep_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CEP", None))
        self.label_139.setText("")
        self.label_140.setText(QCoreApplication.translate("MainWindow", u"ENDERE\u00c7O", None))
        self.le_endereco_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ENDERE\u00c7O", None))
        self.label_141.setText("")
        self.label_142.setText(QCoreApplication.translate("MainWindow", u"NUMERO", None))
        self.le_numero_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"NUMERO", None))
        self.label_143.setText("")
        self.label_144.setText(QCoreApplication.translate("MainWindow", u"BAIRRO", None))
        self.le_bairro_3.setText("")
        self.le_bairro_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"BAIRRO", None))
        self.label_145.setText("")
        self.label_146.setText(QCoreApplication.translate("MainWindow", u"CIDADE", None))
        self.le_cidade_3.setText("")
        self.le_cidade_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CIDADE", None))
        self.label_39.setText("")
        self.btn_update_municipe.setText(QCoreApplication.translate("MainWindow", u"ATUALIZAR", None))
        self.label_40.setText("")
        self.label_7.setText("")
        self.label_10.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"DESENVOLVEDOR", None))
        self.label_8.setText("")
        self.label_9.setText("")
        self.label_3.setText("")
        self.label.setText("")
        self.label_6.setText("")
        self.label_5.setText("")
    # retranslateUi

