

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(518, 314)
        Form.setMinimumSize(QSize(518, 314))
        Form.setMaximumSize(QSize(518, 314))
        icon = QIcon()
        icon.addFile(u"logo.png", QSize(), QIcon.Normal, QIcon.Off)
        Form.setWindowIcon(icon)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(9, 9, 9, 9)
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(-10, -20, 502, 311))
        self.label.setPixmap(QPixmap(u"Prefeitura Municipal de Sorocaba.jpg"))
        self.label.setScaledContents(True)
        self.le_usuario = QLineEdit(self.frame)
        self.le_usuario.setObjectName(u"le_usuario")
        self.le_usuario.setGeometry(QRect(20, 250, 141, 20))
        self.le_usuario.setMinimumSize(QSize(141, 20))
        self.le_usuario.setMaximumSize(QSize(141, 20))
        font = QFont()
        font.setFamily(u"Courier")
        font.setPointSize(12)
        self.le_usuario.setFont(font)
        self.le_usuario.setAlignment(Qt.AlignCenter)
        self.le_senha = QLineEdit(self.frame)
        self.le_senha.setObjectName(u"le_senha")
        self.le_senha.setGeometry(QRect(170, 250, 141, 20))
        self.le_senha.setMinimumSize(QSize(141, 20))
        self.le_senha.setMaximumSize(QSize(141, 20))
        self.le_senha.setFont(font)
        self.le_senha.setEchoMode(QLineEdit.Password)
        self.le_senha.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 20, 311, 51))
        font1 = QFont()
        font1.setPointSize(15)
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.btn_login = QPushButton(self.frame)
        self.btn_login.setObjectName(u"btn_login")
        self.btn_login.setGeometry(QRect(330, 230, 151, 51))
        font2 = QFont()
        font2.setFamily(u"Courier New")
        font2.setPointSize(15)
        font2.setBold(False)
        font2.setUnderline(False)
        font2.setWeight(12)
        font2.setStrikeOut(False)
        self.btn_login.setFont(font2)
        self.btn_login.setStyleSheet(u".QPushButton {\n"
"   background: rgba(247, 0, 0, 0.54);\n"
"   background-image: -webkit-linear-gradient(top, rgba(247, 0, 0, 0.54), #CAD01E);\n"
"   background-image: -moz-linear-gradient(top, rgba(247, 0, 0, 0.54), #CAD01E);\n"
"   background-image: -ms-linear-gradient(top, rgba(247, 0, 0, 0.54), #CAD01E);\n"
"   background-image: -o-linear-gradient(top, rgba(247, 0, 0, 0.54), #CAD01E);\n"
"   background-image: -webkit-gradient(to bottom, rgba(247, 0, 0, 0.54), #CAD01E);\n"
"   -webkit-border-radius: 20px;\n"
"   -moz-border-radius: 20px;\n"
"   border-radius: 20px;\n"
"   height: 4px;\n"
"   line-height: 4px;\n"
"   color: #FFFFFF;\n"
"   font-family: Courier New;\n"
"   width: 149px;\n"
"   padding: 15px;\n"
"   -webkit-box-shadow: -9px 1px 20px 0 #FFAE00;\n"
"   -moz-box-shadow: -9px 1px 20px 0 #FFAE00;\n"
"   box-shadow: -9px 1px 20px 0 #FFAE00;\n"
"   text-shadow: -15px 1px 20px #000000;\n"
"   border: solid #337FED 0;\n"
"   text-decoration: none;\n"
"   display: inline-block;\n"
"   cursor: pointer;\n"
""
                        "   text-align: center;\n"
"}\n"
"\n"
".QPushButton:hover {\n"
"   border: solid #DD380D 3px;\n"
"   background: #CAD01E;\n"
"   background-image: -webkit-linear-gradient(top, #CAD01E, rgba(247, 0, 0, 0.54));\n"
"   background-image: -moz-linear-gradient(top, #CAD01E, rgba(247, 0, 0, 0.54));\n"
"   background-image: -ms-linear-gradient(top, #CAD01E, rgba(247, 0, 0, 0.54));\n"
"   background-image: -o-linear-gradient(top, #CAD01E, rgba(247, 0, 0, 0.54));\n"
"   background-image: -webkit-gradient(to bottom, #CAD01E, rgba(247, 0, 0, 0.54));\n"
"   -webkit-border-radius: 20px;\n"
"   -moz-border-radius: 20px;\n"
"   border-radius: 20px;\n"
"   text-decoration: none;\n"
"}")

        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Agendamentos JD SIMUS by. Douglas", None))
        self.label.setText("")
        self.le_usuario.setPlaceholderText(QCoreApplication.translate("Form", u"USUARIO", None))
        self.le_senha.setPlaceholderText(QCoreApplication.translate("Form", u"SENHA", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"AGENDAMENTOS C.E. SIMUS", None))
        self.btn_login.setText(QCoreApplication.translate("Form", u"LOGIN", None))
    # retranslateUi

