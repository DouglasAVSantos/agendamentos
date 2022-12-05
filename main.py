from PySide2 import QtCore, QtGui
from time import sleep
from login_agendamentos import Ui_Form
from PySide2.QtCore import QDate
from PySide2.QtWidgets import QApplication, QMessageBox, QMainWindow, QWidget
from MainWindow import Ui_MainWindow
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import sys
from bd_system import DataBase
import requests
from PySide2.QtSql import QSqlDatabase, QSqlTableModel
import re
from datetime import datetime
from PySide2.QtCore import Qt


class Login(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.btn_login.clicked.connect(self.verifica_senha)

    def message_critical(self,title,txt):
        msg = QMessageBox(self)
        msg.setWindowTitle(title)
        msg.setIcon(QMessageBox.Critical)
        msg.setText(f'{txt}')
        msg.exec_()

    def verifica_senha(self):
        # try:
            db = DataBase()
            db.conect_db()
            if db.db_check_user_admin(self.le_usuario.text().strip(),self.le_senha.text().strip()) == 'user':
                self.login = self.le_usuario.text()
                self.senha = self.le_senha.text()
                self.w = MainWindow(self.login, self.senha)
                self.w.btn_new_user.hide()
                self.w.show()
                self.close()
                db.close_db()
            elif db.db_check_user_admin(self.le_usuario.text().strip(),self.le_senha.text().strip()) == 'admin':
                self.login = self.le_usuario.text()
                self.senha = self.le_senha.text()
                self.w = MainWindow(self.login, self.senha)
                self.w.show()
                self.close()
                db.close_db()
            elif self.le_usuario.text().strip() == '':
                self.message_critical('CAMPOS VAZIOS','O CAMPO "USUARIO" ESTA VAZIO')
            elif self.le_senha.text().strip() == '':
                self.message_critical('CAMPOS VAZIOS','O CAMPO "SENHA" ESTA VAZIO')
            else:
                self.message_critical('CADASTRO NÃO ENCONTRADO','LOGIN OU SENHA NÃO CADASTRADO')
                self.le_senha.setText('')

        # except:
        #     # abre uma caixa de msg com erro
        #     self.message_critical('LOGIN OU SENHA INVÁLIDOS')
        #     self.le_senha.setText('')


class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self,login,senha):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.login = login
        self.senha = senha

        self.get_usuario(self.login, self.senha)
        # *****************************ANIMAÇÃO DOS BOTOES CADASTRAR E MUNICIPES*********************************************************************
        self.btn_menu_cadastrar.clicked.connect(self.animation_frame_cadastrar)
        self.btn_menu_municipes.clicked.connect(self.animation_frame_municipes)
        # **************************************************************************************************
        #*****************************BOTOES DE ACESSO DAS PAGINAS*****************************************
        self.btn_menu_sobre.clicked.connect(self.pagina_sobre)
        self.btn_menu_home.clicked.connect(self.pagina_home)
        self.btn_municipes_cadastrados.clicked.connect(self.pagina_municipes_cadastrados)
        self.btn_new_municipe.clicked.connect(self.pagina_new_municipe)
        self.btn_new_user.clicked.connect(self.pagina_new_user)
        self.btn_menu_agendamento.clicked.connect(self.get_agendamentos)
        self.btn_new_agendamento.clicked.connect(self.pagina_novo_agendamentos)
        self.btn_alterar_municipes_cadastros.clicked.connect(self.pagina_att_municipe)
        #**************************************************************************************************


        #*********************BOTOES DA PAGINA DE CADASTRO DE MUNICIPE******************************************
        self.btn_novo_cadastro.clicked.connect(self.novo_municipe)
        self.le_cep.textChanged.connect(self.mascara_cep)
        self.le_cep_3.textChanged.connect(self.mascara_cep2)
        self.le_cpf.textChanged.connect(self.mascara_cpf)
        self.le_telefone.textChanged.connect(self.mascara_telefone)
        self.le_telefone_3.textChanged.connect(self.mascara_telefone_3)
        self.btn_lupa.clicked.connect(self.get_dados_municipe)
        # **************************************************************************************************

        # *******************BOTOES DA PAGINA DE MUNICIPES CADASTRADOS***************************************************

        self.btn_update_municipe.clicked.connect(self.update_table_municipes)
        # **************************************************************************************************

        # ********************FILTROS********************************************************
        self.le_pesquisa_municipe.textChanged.connect(self.radio_button_active)
        # self.le_filtro_data.textChanged.connect(self.filtro_datas)
        # **************************************************************************************************

        # *******************ADICIONA A LISTA DE MUNICIPES AO COMBO BOX DA PAGINA AGENDAMENTOS*******************************************************************************
        self.add_municipes_combobox()
        # **************************************************************************************************

        # *********************ATUALIZA AS TABELAS DO SISTEMA*****************************************************************************
        self.table_reset()
        # **************************************************************************************************

        # **************************************************************************************************
        self.btn_agendar.clicked.connect(self.novo_agendamento)
        # **************************************************************************************************

        self.calendarWidget.clicked.connect(self.filtro_datas)

        self.today_agendamentos()

        self.bt_cadastrar_usuario.clicked.connect(self.new_user)
        self.bt_deletar_usuario.clicked.connect(self.delete_user)
        self.tb_municipes_cadastrados.doubleClicked.connect(self.att_municipe_a_partir_da_tabela)
        self.lv_agendamentos_cadastrados.doubleClicked.connect(self.novo_agendamento_a_partir_da_tabela)
        self.tb_agendamento.doubleClicked.connect(self.get_new_agendamento)
        self.mascara_campos()


    def animation_frame_cadastrar(self):
        height = self.frame_cadastrar.height()
        if height == 0:
            newheight = 200
        else:
            newheight = 0
        if self.frame_municipes.height() == 0:
            self.animation = QtCore.QPropertyAnimation(self.frame_cadastrar,b'maximumHeight')
            self.animation.setDuration(500)
            self.animation.setStartValue(height)
            self.animation.setEndValue(newheight)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation.start()
        else:
            self.animation = QtCore.QPropertyAnimation(self.frame_cadastrar, b'maximumHeight')
            self.animation.setDuration(500)
            self.animation.setStartValue(height)
            self.animation.setEndValue(newheight)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation.start()
            self.animation2 = QtCore.QPropertyAnimation(self.frame_municipes, b'maximumHeight')
            self.animation2.setDuration(500)
            self.animation2.setStartValue(200)
            self.animation2.setEndValue(0)
            self.animation2.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation2.start()

    def animation_frame_municipes(self):
        height = self.frame_municipes.height()
        if height == 0:
            newheight = 200
        else:
            newheight = 0
        if self.frame_cadastrar.height() == 0:
            self.animation = QtCore.QPropertyAnimation(self.frame_municipes,b'maximumHeight')
            self.animation.setDuration(500)
            self.animation.setStartValue(height)
            self.animation.setEndValue(newheight)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation.start()
        else:
            self.animation = QtCore.QPropertyAnimation(self.frame_municipes, b'maximumHeight')
            self.animation.setDuration(500)
            self.animation.setStartValue(height)
            self.animation.setEndValue(newheight)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation.start()
            self.animation2 = QtCore.QPropertyAnimation(self.frame_cadastrar, b'maximumHeight')
            self.animation2.setDuration(500)
            self.animation2.setStartValue(200)
            self.animation2.setEndValue(0)
            self.animation2.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation2.start()

    def close_animation(self):
        if self.frame_cadastrar.height() == 0 and self.frame_municipes.height() == 0:
            pass
        elif self.frame_municipes.height() > 0:
            self.animation = QtCore.QPropertyAnimation(self.frame_municipes, b'maximumHeight')
            self.animation.setDuration(500)
            self.animation.setStartValue(200)
            self.animation.setEndValue(0)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation.start()
        elif self.frame_cadastrar.height() > 0:
            self.animation2 = QtCore.QPropertyAnimation(self.frame_cadastrar, b'maximumHeight')
            self.animation2.setDuration(500)
            self.animation2.setStartValue(200)
            self.animation2.setEndValue(0)
            self.animation2.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation2.start()

    def pagina_home(self):
        self.stackedWidget.setCurrentWidget(self.page_home)
        self.close_animation()

    def pagina_att_municipe(self):
        self.stackedWidget.setCurrentWidget(self.page_att_municipe)
        self.close_animation()

    def pagina_novo_agendamentos(self):
        self.stackedWidget.setCurrentWidget(self.page_novo_agendamento)
        self.close_animation()

    def pagina_sobre(self):
        self.stackedWidget.setCurrentWidget(self.page_sobre)
        self.close_animation()

    def pagina_new_user(self):
        self.stackedWidget.setCurrentWidget(self.page_new_user)
        self.close_animation()

    def pagina_new_municipe(self):
        self.stackedWidget.setCurrentWidget(self.page_novo_municipe)
        self.close_animation()

    def pagina_municipes_cadastrados(self):
        self.stackedWidget.setCurrentWidget(self.page_cadastrados)
        self.close_animation()

    def att_municipe_a_partir_da_tabela(self):
        y = self.tb_municipes_cadastrados.currentIndex()
        x = self.model.primaryValues(y.row())
        cpf = x.value('CPF')
        msg = QMessageBox(self)
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle('ALTERAR MUNICIPE?')
        msg.setText('GOSTARIA DE ALTERAR O MUNICIPE SELECIONADO?')
        msg.setStandardButtons(QMessageBox.Yes|QMessageBox.No)
        msg.setButtonText(QMessageBox.Yes,'SIM')
        msg.setButtonText(QMessageBox.No,'NÃO')
        result = msg.exec_()
        if result == QMessageBox.Yes:
            db = DataBase()
            db.conect_db()
            cursor = db.conection.cursor()
            cursor.execute(f'''
                    SELECT * FROM municipes WHERE cpf = '{cpf}';
                    ''')
            municipe = cursor.fetchall()
            for x in municipe:
                self.pagina_att_municipe()
                self.cb_municipes_att.setCurrentText(x[0])
                self.le_nome_3.setText(x[0])
                self.lv_rg_3.setText(x[1])
                self.le_cpf_3.setText(x[2])
                self.mascara_cpf_3()
                self.le_cpf_3.setReadOnly(True)
                self.de_data_nascimento_3.setDate(QDate(int(x[3][6:]), int(x[3][3:5]), int(x[3][:2])))
                self.le_telefone_3.setText(x[4])
                self.le_instituicao_3.setText(x[5])
                self.le_cep_3.setText(x[6])
                self.le_numero_3.setText(x[8])
            db.close_db()
        else:
            msg.close()

    def get_new_agendamento(self):
        y = self.tb_agendamento.currentIndex()
        x = self.model3.primaryValues(y.row())
        z = y.column()
        data = x.value('data')
        if z == 1:
            z = 'Horario_08h30'
            hora = 8
            minuto = 30
        elif z == 2:
            z = 'Horario_09h30'
            hora = 9
            minuto = 30
        elif z == 3:
            z = 'Horario_10h30'
            hora = 10
            minuto = 30
        elif z == 4:
            z = 'Horario_11h30'
            hora = 11
            minuto = 30
        elif z == 5:
            z = 'Horario_12h30'
            hora = 12
            minuto = 30
        elif z == 6:
            z = 'Horario_13h30'
            hora = 13
            minuto = 30
        elif z == 7:
            z = 'Horario_14h30'
            hora = 14
            minuto = 30
        elif z == 8:
            z = 'Horario_15h30'
            hora = 15
            minuto = 30
        elif z == 9:
            z = 'Horario_16h30'
            hora = 16
            minuto = 30
        self.de_data_do_agendamento.setDate(QDate(int(data[6:]), int(data[3:5]), int(data[:2])))
        self.te_horario_agendamento.setTime(QTime(hora, minuto))

    def novo_agendamento_a_partir_da_tabela(self):
        y = self.lv_agendamentos_cadastrados.currentIndex()
        x = self.model2.primaryValues(y.row())
        z = y.column()
        data = x.value('data')
        if z == 1:
            z = 'Horario_08h30'
            hora = 8
            minuto = 30
        elif z == 2:
            z = 'Horario_09h30'
            hora = 9
            minuto = 30
        elif z == 3:
            z = 'Horario_10h30'
            hora = 10
            minuto = 30
        elif z == 4:
            z = 'Horario_11h30'
            hora = 11
            minuto = 30
        elif z == 5:
            z = 'Horario_12h30'
            hora = 12
            minuto = 30
        elif z == 6:
            z = 'Horario_13h30'
            hora = 13
            minuto = 30
        elif z == 7:
            z = 'Horario_14h30'
            hora = 14
            minuto = 30
        elif z == 8:
            z = 'Horario_15h30'
            hora = 15
            minuto = 30
        elif z == 9:
            z = 'Horario_16h30'
            hora = 16
            minuto = 30
        if x.value(z) == '':
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle('NOVO AGENDAMENTO?')
            msg.setText(f'GOSTARIA DE CRIAR UM NOVO AGENDAMENTO?\nData: {data} - {z} ')
            msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            msg.setButtonText(QMessageBox.Yes, 'SIM')
            msg.setButtonText(QMessageBox.No, 'NÃO')
            result = msg.exec_()
            if result == QMessageBox.Yes:
                self.pagina_novo_agendamentos()
                self.de_data_do_agendamento.setDate(QDate(int(data[6:]), int(data[3:5]), int(data[:2])))
                self.te_horario_agendamento.setTime(QTime(hora,minuto))
            else:
                msg.close()

        else:
            self.message_information('Cadastro Existente','Agendamento Já Cadastrado')

        # data = x.value('CPF')
        # horario = x.value()

    def mascara_cpf(self,s):
        mascara = self.le_cpf
        mascara.setMaxLength(14)
        l = [i for i in s if i.isdigit()]
        p = ''
        for i in l:
            p += str(i).strip()

        p1 = p[0:3]
        p2 = p[3:6]
        p3 = p[6:9]
        p4 = p[9:11]
        if len(p) == 3:
            self.le_cpf.setText(f'{p1}.')
        elif len(p) > 3 and len(p) < 6:
            self.le_cpf.setText(f'{p1}.{p2}')
        elif len(p) == 6:
            self.le_cpf.setText(f'{p1}.{p2}.')
        elif len(p) > 6 and len(p) < 9:
            self.le_cpf.setText(f'{p1}.{p2}.{p3}')
        elif len(p) == 9:
            self.le_cpf.setText(f'{p1}.{p2}.{p3}-')
        elif len(p) > 9 and len(p) < 11:
            self.le_cpf.setText(f'{p1}.{p2}.{p3}-{p4}')
        elif len(p) == 11:
            self.le_cpf.setText(f'{p1}.{p2}.{p3}-{p4}')
            self.cpf_validate(p)
        else:
            self.le_cpf.setText(p)

    def mascara_cpf_3(self):
        p = self.le_cpf_3.text()
        p1 = p[0:3]
        p2 = p[3:6]
        p3 = p[6:9]
        p4 = p[9:11]
        self.le_cpf_3.setText(f'{p1}.{p2}.{p3}-{p4}')

    def mascara_cep(self,s):
        self.le_cep.setMaxLength(10)

        l = [i for i in s if i.isdigit()]
        p = ''
        for i in l:
            p += str(i).strip()

        p1 = p[0:2]
        p2 = p[2:5]
        p3 = p[5:9]
        if len(p) == 2:
            self.le_cep.setText(f'{p1}.')
        elif len(p) > 2 and len(p) < 5:
            self.le_cep.setText(f'{p1}.{p2}')
        elif len(p) == 5:
            self.le_cep.setText(f'{p1}.{p2}-')
        elif len(p) > 5 and len(p) < 8:
            self.le_cep.setText(f'{p1}.{p2}-{p3}')
        elif len(p) == 8:
            self.busca_cep1(p)
        else:
            self.le_cep.setText(p)

    def mascara_cep2(self,s):
        self.le_cep.setMaxLength(10)

        l = [i for i in s if i.isdigit()]
        p = ''
        for i in l:
            p += str(i).strip()

        p1 = p[0:2]
        p2 = p[2:5]
        p3 = p[5:9]
        if len(p) == 2:
            self.le_cep_3.setText(f'{p1}.')
        elif len(p) > 2 and len(p) < 5:
            self.le_cep_3.setText(f'{p1}.{p2}')
        elif len(p) == 5:
            self.le_cep_3.setText(f'{p1}.{p2}-')
        elif len(p) > 5 and len(p) < 8:
            self.le_cep_3.setText(f'{p1}.{p2}-{p3}')
        elif len(p) == 8:
            self.le_cep_3.setText(f'{p1}.{p2}-{p3}')
            self.busca_cep2(p)
        else:
            self.le_cep_3.setText(p)

    def mascara_campos(self):
        self.le_numero.setMaxLength(15)
        self.le_numero_3.setMaxLength(15)
        self.lv_rg.setMaxLength(14)
        self.lv_rg_3.setMaxLength(14)

    def mascara_telefone(self,s):
        mascara = self.le_telefone
        mascara.setMaxLength(14)
        l = [i for i in s if i.isdigit()]
        p = ''
        for i in l:
            p += str(i).strip()

        p1 = p[0:2]
        p2 = p[2:]
        if len(p) == 2:
            self.le_telefone.setText(f'({p1})')
        elif len(p) > 2:
            self.le_telefone.setText(f'({p1}){p2}')
        else:
            self.le_telefone.setText(p)

    def mascara_telefone_3(self,s):
        mascara = self.le_telefone_3
        mascara.setMaxLength(14)
        l = [i for i in s if i.isdigit()]
        p = ''
        for i in l:
            p += str(i).strip()

        p1 = p[0:2]
        p2 = p[2:]
        if len(p) == 2:
            self.le_telefone_3.setText(f'({p1})')
        elif len(p) > 2:
            self.le_telefone_3.setText(f'({p1}){p2}')
        else:
            self.le_telefone_3.setText(p)

    def get_usuario(self,login,senha):
        try:
            db = DataBase()
            db.conect_db()
            cursor = db.conection.cursor()
            cursor.execute(f'select user from users where login = "{login}" and senha = "{senha}" ')
            usuario = cursor.fetchone()
            self.usuario = usuario[0]
            print(self.usuario)
            db.close_db()
        except:
            self.message_critical('Usuario não encontrado','O Usuario não foi encontrado')

    #FUNÇÃO QUE CRIA CAIXA DE DIALOGO DE ERRO
    def message_critical(self,title,txt):
        msg = QMessageBox(self)
        msg.setWindowTitle(title)
        msg.setIcon(QMessageBox.Warning)
        msg.setText(f'{txt}')
        msg.exec_()

    #FUNÇÃO QUE CRIA CAIXA DE DIALOGO DE INFORMAÇÃO
    def message_information(self,title,txt):
        msg = QMessageBox(self)
        msg.setWindowTitle(title)
        msg.setIcon(QMessageBox().Information)
        msg.setText(f'{txt}')
        msg.exec_()

    #FUNÇÃO QUE CADASTRA UM NOVO MUNICIPE AO BANCO DE DADOS ATRAVÉS DO SISTEMA
    def novo_municipe(self):
        db = DataBase()
        db.conect_db()
        nome = self.le_nome.text().strip().title()
        rg = self.lv_rg.text().strip().title()
        cpf = self.le_cpf.text().strip().title()
        data = self.de_data_nascimento.text()
        telefone = self.le_telefone.text().strip().title()
        instituicao = self.le_instituicao.text().strip().title()
        cep = self.le_cep.text().strip().title()
        endereco = self.le_endereco.text().strip().title()
        numero = self.le_numero.text().strip().title()
        bairro = self.le_bairro.text().strip().title()
        cidade = self.le_cidade.text().strip().title()

        if nome == '':
            self.message_critical('CAMPO VAZIO','O CAMPO "NOME" ESTA VAZIO')
        elif rg == '':
            self.message_critical('CAMPO VAZIO','O CAMPO "RG" ESTA VAZIO')

        elif cpf == '':
            self.message_critical('CAMPO VAZIO','O CAMPO "CPF" ESTA VAZIO')

        elif telefone == '':
            self.message_critical('CAMPO VAZIO','O CAMPO "TELEFONE" ESTA VAZIO')

        elif cep == '':
            self.message_critical('CAMPO VAZIO','O CAMPO "CEP" ESTA VAZIO')

        elif endereco == '':
            self.message_critical('CAMPO VAZIO','O CAMPO "ENDEREÇO" ESTA VAZIO')
        elif numero == '':
            self.message_critical('CAMPO VAZIO','O CAMPO "NUMERO" ESTA VAZIO')
        elif bairro == '':
            self.message_critical('CAMPO VAZIO','O CAMPO "BAIRRO" ESTA VAZIO')
        elif cidade == '':
            self.message_critical('CAMPO VAZIO','O CAMPO "CIDADE" ESTA VAZIO')
        else:
            db.insert_municipes(nome, rg, cpf.replace('.','').replace('-',''), data,telefone.replace('(','').replace(')',''), cep, endereco,numero,bairro,cidade,instituicao)
            self.le_nome.setText('')
            self.lv_rg.setText('')
            self.le_cpf.setText('')
            self.le_telefone.setText('')
            self.le_instituicao.setText('')
            self.le_cep.setText('')
            self.le_endereco.setText('')
            self.le_numero.setText('')
            self.le_bairro.setText('')
            self.le_cidade.setText('')
            self.message_information('CADASTRO REALIZADO','CADASTRO REALIZADO COM SUCESSO!!!')
            self.table_reset()
            self.add_municipes_combobox()
            db.close_db()

    # FUNÇÃO QUE CADASTRA UM NOVO AGENDAMENTO AO BANCO DE DADOS ATRAVÉS DO SISTEMA
    def novo_agendamento(self):
        db = DataBase()
        db.conect_db()
        cursor = db.conection.cursor()
        self.d = datetime.now()
        self.dia_hoje = self.d.day
        self.mes_hoje = self.d.month
        self.ano_hoje = self.d.year
        self.hora = f'{self.d.hour}:{self.d.minute}' if len(str(self.d.minute)) == 2 else f'{self.d.hour}:0{self.d.minute}'
        self.strdate = f' - Agendado por: "{self.usuario}" Dia: {self.dia_hoje}/{self.mes_hoje}/{self.ano_hoje} Às {self.hora}'
        municipe = f'{self.comboBox_municipe.currentText()}{self.strdate}'
        municipe2 = self.comboBox_municipe.currentText()
        data = self.de_data_do_agendamento.text()
        horario = self.te_horario_agendamento.text()
        msg = QMessageBox(self)
        msg.setWindowTitle('INFORMATIVO')
        msg.setIcon(QMessageBox.Information)
        msg.setText(f'TEM CERTEZA QUE DESEJA CADASTRAR O AGENDAMENTO:\n"{municipe}"\nDATA DO AGENDAMENTO: {data} ÀS "{horario}"')
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msg.setButtonText(QMessageBox.Yes, 'SIM')
        msg.setButtonText(QMessageBox.No, 'NÃO')
        result = msg.exec_()
        if result == QMessageBox.Yes:

            if horario == '08:30':
                if self.check_agendamentos('Horario_08h30', data):
                    if not self.check_data(data):
                        cursor.execute(f'''
                        INSERT INTO agendamentos (DATA,Horario_08h30) VALUES ('{data}','{municipe}');
                        ''')
                        db.conection.commit()
                        self.table_reset()
                        self.add_municipes_combobox()
                        db.close_db()
                    else:
                        cursor.execute(f'''
                        UPDATE agendamentos set Horario_08h30 = '{municipe}' WHERE DATA = '{data}';
                        ''')
                        db.conection.commit()
                        self.table_reset()
                        self.add_municipes_combobox()
                        db.close_db()
                else:
                    self.message_critical('AGENDAMENTO EXISTENTE','O HORÁRIO JÁ FOI RESERVADO\nPESQUISE EM "AGENDADOS" OS AGENDAMENTOS JA REALIZADOS')

            elif horario == '09:30':
                if self.check_agendamentos('Horario_09h30', data):
                    if not self.check_data(data):
                        cursor.execute(f'''
                        INSERT INTO agendamentos (DATA,Horario_09h30) VALUES ('{data}','{municipe}');
                        ''')
                        db.conection.commit()
                        self.table_reset()
                        self.add_municipes_combobox()
                        db.close_db()
                    else:
                        cursor.execute(f'''
                        UPDATE agendamentos set Horario_09h30 = '{municipe}' WHERE DATA = '{data}';
                        ''')
                        db.conection.commit()
                        self.table_reset()
                        self.add_municipes_combobox()
                        db.close_db()
                else:
                    self.message_critical('AGENDAMENTO EXISTENTE','O HORÁRIO JÁ FOI RESERVADO\nPESQUISE EM "AGENDADOS" OS AGENDAMENTOS JA REALIZADOS')
            elif horario == '10:30':
                if self.check_agendamentos('Horario_10h30', data):
                    if not self.check_data(data):
                        cursor.execute(f'''
                        INSERT INTO agendamentos (DATA,Horario_10h30) VALUES ('{data}','{municipe}');
                        ''')
                        db.conection.commit()
                        self.table_reset()
                        self.add_municipes_combobox()
                        db.close_db()
                    else:
                        cursor.execute(f'''
                        UPDATE agendamentos set Horario_10h30 = '{municipe}' WHERE DATA = '{data}';
                        ''')
                        db.conection.commit()
                        self.table_reset()
                        self.add_municipes_combobox()
                        db.close_db()
                else:
                    self.message_critical('AGENDAMENTO EXISTENTE','O HORÁRIO JÁ FOI RESERVADO\nPESQUISE EM "AGENDADOS" OS AGENDAMENTOS JA REALIZADOS')
            elif horario == '11:30':
                if self.check_agendamentos('Horario_11h30', data):
                    if not self.check_data(data):
                        cursor.execute(f'''
                        INSERT INTO agendamentos (DATA,Horario_11h30) VALUES ('{data}','{municipe}');
                        ''')
                        db.conection.commit()
                        self.table_reset()
                        self.add_municipes_combobox()
                        db.close_db()
                    else:
                        cursor.execute(f'''
                        UPDATE agendamentos set Horario_11h30 = '{municipe}' WHERE DATA = '{data}';
                        ''')
                        db.conection.commit()
                        self.table_reset()
                        self.add_municipes_combobox()
                        db.close_db()
                else:
                    self.message_critical('AGENDAMENTO EXISTENTE','O HORÁRIO JÁ FOI RESERVADO\nPESQUISE EM "AGENDADOS" OS AGENDAMENTOS JA REALIZADOS')
            elif horario == '12:30':
                if self.check_agendamentos('Horario_12h30', data):
                    if not self.check_data(data):
                        cursor.execute(f'''
                        INSERT INTO agendamentos (DATA,Horario_12h30) VALUES ('{data}','{municipe}');
                        ''')
                        db.conection.commit()
                        self.table_reset()
                        self.add_municipes_combobox()
                        db.close_db()
                    else:
                        cursor.execute(f'''
                        UPDATE agendamentos set Horario_12h30 = '{municipe}' WHERE DATA = '{data}';
                        ''')
                        db.conection.commit()
                        self.table_reset()
                        self.add_municipes_combobox()
                        db.close_db()
                else:
                    self.message_critical('AGENDAMENTO EXISTENTE','O HORÁRIO JÁ FOI RESERVADO\nPESQUISE EM "AGENDADOS" OS AGENDAMENTOS JA REALIZADOS')
            elif horario == '13:30':
                if self.check_agendamentos('Horario_13h30', data):
                    if not self.check_data(data):
                        cursor.execute(f'''
                        INSERT INTO agendamentos (DATA,Horario_13h30) VALUES ('{data}','{municipe}');
                        ''')
                        db.conection.commit()
                        self.table_reset()
                        self.add_municipes_combobox()
                        db.close_db()
                    else:
                        cursor.execute(f'''
                        UPDATE agendamentos set Horario_13h30 = '{municipe}' WHERE DATA = '{data}';
                        ''')
                        db.conection.commit()
                        self.table_reset()
                        self.add_municipes_combobox()
                        db.close_db()
                else:
                    self.message_critical('AGENDAMENTO EXISTENTE','O HORÁRIO JÁ FOI RESERVADO\nPESQUISE EM "AGENDADOS" OS AGENDAMENTOS JA REALIZADOS')
            elif horario == '14:30':
                if self.check_agendamentos('Horario_14h30', data):
                    if not self.check_data(data):
                        cursor.execute(f'''
                        INSERT INTO agendamentos (DATA,Horario_14h30) VALUES ('{data}','{municipe}');
                        ''')
                        db.conection.commit()
                        self.table_reset()
                        self.add_municipes_combobox()
                        db.close_db()
                    else:
                        cursor.execute(f'''
                        UPDATE agendamentos set Horario_14h30 = '{municipe}' WHERE DATA = '{data}';
                        ''')
                        db.conection.commit()
                        self.table_reset()
                        self.add_municipes_combobox()
                        db.close_db()
                else:
                    self.message_critical('AGENDAMENTO EXISTENTE','O HORÁRIO JÁ FOI RESERVADO\nPESQUISE EM "AGENDADOS" OS AGENDAMENTOS JA REALIZADOS')
            elif horario == '15:30':
                if self.check_agendamentos('Horario_15h30', data):
                    if not self.check_data(data):
                        cursor.execute(f'''
                        INSERT INTO agendamentos (DATA,Horario_15h30) VALUES ('{data}','{municipe}');
                        ''')
                        db.conection.commit()
                        self.table_reset()
                        self.add_municipes_combobox()
                        db.close_db()
                    else:
                        cursor.execute(f'''
                        UPDATE agendamentos set Horario_15h30 = '{municipe}' WHERE DATA = '{data}';
                        ''')
                        db.conection.commit()
                        self.table_reset()
                        self.add_municipes_combobox()
                        db.close_db()
                else:
                    self.message_critical('AGENDAMENTO EXISTENTE','O HORÁRIO JÁ FOI RESERVADO\nPESQUISE EM "AGENDADOS" OS AGENDAMENTOS JA REALIZADOS')
            elif horario == '16:30':
                if self.check_agendamentos('Horario_16h30', data):
                    if not self.check_data(data):
                        cursor.execute(f'''
                        INSERT INTO agendamentos (DATA,Horario_16h30) VALUES ('{data}','{municipe}');
                        ''')
                        db.conection.commit()
                        self.table_reset()
                        self.add_municipes_combobox()
                        db.close_db()
                    else:
                        cursor.execute(f'''
                        UPDATE agendamentos set Horario_16h30 = '{municipe}' WHERE DATA = '{data}';
                        ''')
                        db.conection.commit()
                        self.table_reset()
                        self.add_municipes_combobox()
                        db.close_db()
                else:
                    self.message_critical('AGENDAMENTO EXISTENTE','O HORÁRIO JÁ FOI RESERVADO\nPESQUISE EM "AGENDADOS" OS AGENDAMENTOS JA REALIZADOS')

        else:
            msg.close()

        db.close_db()

    def check_data(self,s):
            db = DataBase()
            db.conect_db()
            cursor = db.conection.cursor()
            cursor.execute('select data from agendamentos;')
            for linha in cursor.fetchall():
                if linha[0] == s: return True
                else: continue
            return False
            db.close_db()

    #FUNÇÃO QUE CONSOME A API DOS CORREIOS PARA VALIDAR O CEP E INCREMENTAR OS CAMPOS ENDEREÇO,BAIRRO,CIDADE NO CADASTRO
    def busca_cep1(self,s):
        try:
            if len(s) == 8:
                cep = self.le_cep.text().strip().title().replace('.','').replace('-','')
                response = requests.get(f'http://viacep.com.br/ws/{cep}/json/')
                response = response.json()
                self.le_endereco.setText(f'{response["logradouro"]}')
                self.le_bairro.setText(f'{response["bairro"]}')
                self.le_cidade.setText(f'{response["localidade"]}')
        except:
            self.message_critical('CEP NÃO ENCONTRADO','O CEP INFORMDO NÃO FOI ENCONTRADO')


    def busca_cep2(self,s):
        try:
            if len(s) == 8:
                cep = self.le_cep_3.text().strip().title().replace('.','').replace('-','')
                response = requests.get(f'http://viacep.com.br/ws/{cep}/json/')
                response = response.json()
                self.le_endereco_3.setText(f'{response["logradouro"]}')
                self.le_bairro_3.setText(f'{response["bairro"]}')
                self.le_cidade_3.setText(f'{response["localidade"]}')
        except:
            self.message_critical('CEP NÃO ENCONTRADO','O CEP INFORMDO NÃO FOI ENCONTRADO')


    #FUNÇÃO QUE VALIDA O CPF
    def cpf_validate(self, numbers):
        if len(numbers) == 11:
            #  Obtém os números do CPF e ignora outros caracteres
            cpf = [int(char) for char in numbers if char.isdigit()]


            #  Verifica se o CPF tem todos os números iguais, ex: 111.111.111-11
            #  Esses CPFs são considerados inválidos mas passam na validação dos dígitos
            #  Antigo código para referência: if all(cpf[i] == cpf[i+1] for i in range (0, len(cpf)-1))
            if cpf == cpf[::-1]:
                return self.message_critical('DADOS INVÁLIDOS','O CPF DIGITADO É INVÁLIDO'),self.le_cpf.setText('')


            #  Valida os dois dígitos verificadores
            for i in range(9, 11):
                value = sum((cpf[num] * ((i + 1) - num) for num in range(0, i)))
                digit = ((value * 10) % 11) % 10
                if digit != cpf[i]:
                    return self.message_critical('DADOS INVÁLIDOS','O CPF DIGITADO É INVÁLIDO'),self.le_cpf.setText('')
            db = DataBase()
            db.conect_db()
            cursor = db.conection.cursor()
            cursor.execute(f'select cpf from municipes where cpf = "{numbers}"')
            if cursor.fetchone()[0] == numbers:
                db.close_db()
                return self.message_critical('CADASTRO JÁ REALIZADO','ESSE USUARIO JÁ ESTÁ CADASTRADO\nVERIFIQUE OS USUARIOS CADASTRADOS EM "MUNICIPES"->"MUNICIPES CADASTRADOS"'),self.le_cpf.setText('')

    #FUNÇÃO QUE PUXA OS DADOS DO BANCO DE DADOS E INCREMENTA OS CAMPOS DO CADASTRO PARA FAZER ALTERAÇÃO
    def get_dados_municipe(self):
        nome = self.cb_municipes_att.currentText()
        db = DataBase()
        db.conect_db()
        cursor = db.conection.cursor()
        cursor.execute(f'''
        SELECT * FROM municipes WHERE nome = '{nome}';
        ''')
        municipe = cursor.fetchall()
        self.le_nome_3.setText(municipe[0][0])
        self.lv_rg_3.setText(municipe[0][1])
        self.le_cpf_3.setText(municipe[0][2])
        self.mascara_cpf_3()
        self.le_cpf_3.setReadOnly(True)
        self.de_data_nascimento_3.setDate(QDate(int(municipe[0][3][6:]), int(municipe[0][3][3:5]), int(municipe[0][3][:2])))
        self.le_telefone_3.setText(municipe[0][4])
        self.le_instituicao_3.setText(municipe[0][5])
        self.le_cep_3.setText(municipe[0][6])
        self.le_numero_3.setText(municipe[0][8])
        db.close_db()

    #FUNÇÃO QUE ATUALIZA A TABLEVIEW DO SISTEMA
    def update_table_municipes(self):
        msg = QMessageBox(self)
        msg.setWindowTitle('ATUALIZAR DADOS?')
        msg.setIcon(QMessageBox.Information)
        msg.setText('TEM CERTEZA QUE DESEJA ATUALIZAR OS DADOS?')
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msg.setButtonText(QMessageBox.Yes, 'SIM')
        msg.setButtonText(QMessageBox.No, 'NÃO')
        result = msg.exec_()
        if result == QMessageBox.Yes:
            db = DataBase()
            db.conect_db()
            cursor = db.conection.cursor()
            nome = self.le_nome_3.text().strip().title()
            rg = self.lv_rg_3.text().strip().title()
            cpf = self.le_cpf_3.text().strip().title().replace('.','').replace('-','')
            data = self.de_data_nascimento_3.text()
            telefone = self.le_telefone_3.text().strip().title().replace('(','').replace(')','')
            instituicao = self.le_instituicao_3.text().strip().title()
            cep = self.le_cep_3.text().strip().title()
            endereco = self.le_endereco_3.text().strip().title()
            numero = self.le_numero_3.text().strip().title()
            bairro = self.le_bairro_3.text().strip().title()
            cidade = self.le_cidade_3.text().strip().title()

            if nome == '':
                self.message_critical('CAMPO VAZIO', 'O CAMPO "NOME" ESTA VAZIO')
            elif rg == '':
                self.message_critical('CAMPO VAZIO', 'O CAMPO "RG" ESTA VAZIO')
            elif cpf == '':
                self.message_critical('CAMPO VAZIO', 'O CAMPO "CPF" ESTA VAZIO')
            elif telefone == '':
                self.message_critical('CAMPO VAZIO', 'O CAMPO "TELEFONE" ESTA VAZIO')
            elif cep == '':
                self.message_critical('CAMPO VAZIO', 'O CAMPO "CEP" ESTA VAZIO')
            elif endereco == '':
                self.message_critical('CAMPO VAZIO', 'O CAMPO "ENDEREÇO" ESTA VAZIO')
            elif numero == '':
                self.message_critical('CAMPO VAZIO', 'O CAMPO "NUMERO" ESTA VAZIO')
            elif bairro == '':
                self.message_critical('CAMPO VAZIO', 'O CAMPO "BAIRRO" ESTA VAZIO')
            elif cidade == '':
                self.message_critical('CAMPO VAZIO', 'O CAMPO "CIDADE" ESTA VAZIO')
            else:
                cursor.execute(f'''
                UPDATE municipes set NOME = '{nome}', RG = '{rg}', DATA_DE_NASCIMENTO = '{data}', TELEFONE = '{telefone}', INSTITUIÇÃO = '{instituicao}', CEP = '{cep}', ENDEREÇO = '{endereco}', NUMERO = '{numero}', BAIRRO = '{bairro}', CIDADE = '{cidade}' WHERE cpf = {cpf};
    
                ''')
                db.conection.commit()
                self.le_nome_3.setText('')
                self.de_data_nascimento_3.setDate(QDate(2000, 1,1))
                self.lv_rg_3.setText('')
                self.le_cpf_3.setText('')
                self.le_telefone_3.setText('')
                self.le_instituicao_3.setText('')
                self.le_cep_3.setText('')
                self.le_endereco_3.setText('')
                self.le_numero_3.setText('')
                self.le_bairro_3.setText('')
                self.le_cidade_3.setText('')
                self.message_information('CADASTRO ALTERADO','CADASTRO ALTERADO COM SUCESSO!!!')
                self.table_reset()
                self.add_municipes_combobox()
                db.close_db()
        else:
            msg.close()

    #FUNÇÃO QUE PASSA DO BANCO DE DADOS MUNICIPE PARA A TABLEVIEW DO SISTEMA
    def show_table_municipe(self):
        db = DataBase()
        db.conect_db()
        cursor = db.conection.cursor()
        cursor.execute('select * from municipes order by nome')
        clientes = cursor.fetchall()


        self.tb_municipes_cadastrados.clearContents()
        self.tb_municipes_cadastrados.setRowCount(len(clientes))

        for linha, txt in enumerate(clientes):
            for colum, data in enumerate(txt):
                if data == None:
                    data = ''
                self.tb_municipes_cadastrados.setItem(linha, colum, QTableWidgetItem(str(data)))


        for i in range(0, 11):
            self.tb_municipes_cadastrados.resizeColumnToContents(i)
        db.close_db()

    def show_tableview_municipe(self):
        db = QSqlDatabase('QSQLITE')
        db.setDatabaseName('system.db')
        db.open()

        self.model = QSqlTableModel(db=db)
        self.tb_municipes_cadastrados.setModel(self.model)
        self.model.setTable('municipes')
        self.model.select()
        self.tb_municipes_cadastrados.sortByColumn(0, Qt.AscendingOrder)
        for i in range (0,11):
            self.tb_municipes_cadastrados.resizeColumnToContents(i)

    # FUNÇÃO QUE PASSA DO BANCO DE DADOS AGENDAMENTOS PARA A TABLEVIEW DO SISTEMA
    def show_table_agendamentos(self):
        db = QSqlDatabase('QSQLITE')
        db.setDatabaseName('system.db')
        db.open()

        self.model3 = QSqlTableModel(db=db)
        self.tb_agendamento.setModel(self.model3)
        self.model3.setTable('agendamentos')
        self.model3.select()
        self.tb_agendamento.sortByColumn(0, Qt.AscendingOrder)
        for i in range(0, 11):
            self.tb_agendamento.resizeColumnToContents(i)

    def show_table_agendados(self):
        db = QSqlDatabase('QSQLITE')
        db.setDatabaseName('system.db')
        db.open()

        self.model2 = QSqlTableModel(db=db)
        self.lv_agendamentos_cadastrados.setModel(self.model2)
        self.model2.setTable('agendamentos')
        self.model2.select()
        self.lv_agendamentos_cadastrados.sortByColumn(0, Qt.AscendingOrder)
        for i in range (0,11):
            self.lv_agendamentos_cadastrados.resizeColumnToContents(i)

    def radio_button_active(self,s):
        if self.rb_nome.isChecked():
            self.show_tableview_municipe()
            s = re.sub('[\W_]+','',s)
            filter_str2 = f'NOME LIKE "%{s}%"'
            self.model.setFilter(filter_str2)
        elif self.rb_rg.isChecked():
            self.show_tableview_municipe()
            s = re.sub('[\W_]+', '', s)
            filter_str2 = f'RG LIKE "%{s}%"'
            self.model.setFilter(filter_str2)
        elif self.rb_cpf.isChecked():
            self.show_tableview_municipe()
            s = re.sub('[\W_]+', '', s)
            filter_str2 = f'CPF LIKE "%{s}%"'
            self.model.setFilter(filter_str2)
        elif self.rb_telefone.isChecked():
            self.show_tableview_municipe()
            s = re.sub('[\W_]+', '', s)
            filter_str2 = f'TELEFONE LIKE "%{s}%"'
            self.model.setFilter(filter_str2)
        elif self.rb_instituicao.isChecked():
            self.show_tableview_municipe()
            s = re.sub('[\W_]+', '', s)
            filter_str2 = f'INSTITUICAO LIKE "%{s}%"'
            self.model.setFilter(filter_str2)
        elif self.rb_cep.isChecked():
            self.show_tableview_municipe()
            s = re.sub('[\W_]+', '', s)
            filter_str2 = f'CEP LIKE "%{s}%"'
            self.model.setFilter(filter_str2)
        elif self.rb_endereco.isChecked():
            self.show_tableview_municipe()
            s = re.sub('[\W_]+', '', s)
            filter_str2 = f'ENDEREÇO LIKE "%{s}%"'
            self.model.setFilter(filter_str2)
        elif self.rb_bairro.isChecked():
            self.show_tableview_municipe()
            s = re.sub('[\W_]+', '', s)
            filter_str2 = f'BAIRRO LIKE "%{s}%"'
            self.model.setFilter(filter_str2)
        elif self.rb_cidade.isChecked():
            self.show_tableview_municipe()
            s = re.sub('[\W_]+', '', s)
            filter_str2 = f'CIDADE LIKE "%{s}%"'
            self.model.setFilter(filter_str2)

    #FUNÇÃO QUE CARREGA AS TABLEVIEW NO SISTEMA AO SER INICIADO
    def table_reset(self):
        self.lv_agendamentos_cadastrados.update()
        self.tb_municipes_cadastrados.update()
        self.tb_agendamento.update()
        self.show_table_agendados()
        self.show_table_agendamentos()
        self.show_tableview_municipe()

    def filtro_datas(self):
        self.show_table_agendados()
        s = self.calendarWidget.selectedDate()
        if len(str(s.day())) <=1 and len(str(s.month())) <=1:
            s = f'0{s.day()}/0{s.month()}/{s.year()}'
        elif len(str(s.month())) <=1:
            s = f'{s.day()}/0{s.month()}/{s.year()}'
        elif len(str(s.day())) <=1:
            s = f'0{s.day()}/{s.month()}/{s.year()}'
        else:
            s = f'{s.day()}/{s.month()}/{s.year()}'
        filter_str = f'DATA = "{s}"'
        self.model2.setFilter(filter_str)

    #FUNÇÃO QUE ADICIONA A LISTA DE MUNICIPES CADASTRADOS AO COMBO BOX
    def add_municipes_combobox(self):
        db = DataBase()
        db.conect_db()
        cursor = db.conection.cursor()
        cursor.execute('SELECT NOME FROM municipes order by nome')
        self.comboBox_municipe.clear()
        self.cb_municipes_att.clear()
        for nome in cursor.fetchall():
            self.comboBox_municipe.addItem(nome[0])
            self.cb_municipes_att.addItem(nome[0])
        db.close_db()

    def get_agendamentos(self):
        self.stackedWidget.setCurrentWidget(self.page_agendados)
        self.close_animation()
        self.table_reset()

    #FUNÇÃO QUE DELETA O MUNICIPE DO BANCO DE DADOS
    def delete_municipe(self):
        id = self.le_delete_municipe.text().strip()
        try:
            db = DataBase()
            db.conect_db()
            cursor = db.conection.cursor()
            cursor.execute(f'SELECT NOME FROM municipes WHERE ID = {id}')
            nome = cursor.fetchone()
            msg = QMessageBox(self)
            msg.setWindowTitle('INFORMATIVO')
            msg.setIcon(QMessageBox.Information)
            msg.setText(f'TEM CERTEZA QUE DESEJA DELETAR O CADASTRO DE "{nome[0]}"?')
            msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            msg.setButtonText(QMessageBox.Yes, 'SIM')
            msg.setButtonText(QMessageBox.No, 'NÃO')
            result = msg.exec_()
            if result == QMessageBox.No:
                self.le_delete_municipe.setText('')
                msg.close()
            else:
                cursor.execute(f'DELETE FROM municipes WHERE ID = {id}')
                db.conection.commit()
                self.le_delete_municipe.setText('')
                self.table_reset()
                self.add_municipes_combobox()
                db.conect_db()
        except:
            self.message_critical('MUNICIPE NÃO ENCONTRADO')
            self.le_delete_municipe.setText('')

    def today_agendamentos(self):
        self.d = datetime.now()
        self.dia_hoje = self.d.day
        self.mes_hoje = self.d.month
        self.ano_hoje = self.d.year
        self.de_data_do_agendamento.setDate(QDate(self.ano_hoje, self.mes_hoje, self.dia_hoje))

    def delete_user(self):
        db = DataBase()
        db.conect_db()
        usuario = self.le_usuario_deletar.text()

        if self.le_senha_deletar.text() == self.senha and db.check_user_exists(usuario):
            db.delete_user(usuario)
            self.message_information('USUARIO DELETADO','USUARIO DELETADO COM SUCESSO!')
            self.le_usuario_deletar.setText('')
            self.le_senha_deletar.setText('')
            db.close_db()
        else:
            self.message_critical('DADOS NÃO ENCONTRADOS','USUARIO NÃO CADASTRADO\nOU\nSENHA DE ADMINISTRADOR INVÁLIDA')
            self.le_usuario_deletar.setText('')
            self.le_senha_deletar.setText('')
            db.close_db()

    def new_user(self):
        db = DataBase()
        db.conect_db()
        login = self.le_novo_login.text().strip()
        senha = self.le_senha1.text().strip()
        usuario = self.le_novo_usuario.text().strip()
        acess = self.cb_users.currentText()


        if senha != self.le_senha2.text().strip():
            self.message_critical('As senhas informadas não são iguais','Preencha os campos com as senhas iguais.')
            self.le_senha1.setText('')
            self.le_senha2.setText('')
        elif senha == '' or self.le_senha2.text() == '' or usuario == '' or login == '':
            self.message_critical('Campos vazios','Preencha os campos com Usuario e as senhas iguais.')
            self.le_senha1.setText('')
            self.le_senha2.setText('')
        elif db.check_login_exists(login, senha):
            self.message_critical('Usuario e Senha ja Cadastrado','Preencha os campos com um novo Usuario e senha')
            self.le_senha1.setText('')
            self.le_senha2.setText('')
            self.le_novo_usuario.setText('')
        else:
            db.insert_novo_usuario(login,usuario,senha,acess)
            self.message_information('Senha Cadastrada','Senha Cadastrada com Sucesso!')
            self.le_senha1.setText('')
            self.le_novo_login.setText('')
            self.le_novo_usuario.setText('')
            self.le_senha2.setText('')
            db.close_db()
                #FUNÇÃO QUE ADICIONA UM CADASTRO DE CLIENTE NO BANCO DE DADOS

    def check_agendamentos(self, horario, data):
        db = DataBase()
        db.conect_db()
        cursor = db.conection.cursor()
        cursor.execute(f'select {horario} from agendamentos where data = "{data}" ')
        for i in cursor.fetchall():
            if i[0] != None:
                db.close_db()
                return False
        db.close_db()
        return True


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Login()
    window.show()
    app.exec_()
