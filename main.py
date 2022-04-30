from login_agendamentos import Ui_Form
from PySide2.QtCore import QDate
from PySide2.QtWidgets import QApplication, QMessageBox, QMainWindow, QWidget
from MainWindow import Ui_MainWindow
import sys
from bd_system import DataBase
import requests
from PySide2.QtSql import QSqlDatabase, QSqlTableModel
import re






class Login(QWidget, Ui_Form):
    def __init__(self):
        super(Login,self).__init__()
        self.setupUi(self)

        self.btn_login.clicked.connect(self.check_senha)

    def message_critical(self,txt):
        msg = QMessageBox(self)
        msg.setWindowTitle('ERRO DE DADOS')
        msg.setIcon(QMessageBox.Warning)
        msg.setText(f'{txt}')
        msg.exec_()

    def check_senha(self):
        db = DataBase()
        usuario = self.le_usuario.text().strip()
        senha = self.le_senha.text().strip()
        db.conect_db()
        cursor = db.conection.cursor()
        cursor.execute("""SELECT * FROM users""")

        for linha in cursor.fetchall():
            if linha[1] == usuario and linha[2] == senha:
                window.close()
                w = MainWindow()
                w.show()
                db.close_db()
                break
        else:
            self.message_critical('LOGIN INVÁLIDO')








class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)


        #*****************************BOTOES DE ACESSO DAS PAGINAS*****************************************
        self.btn_sobre.clicked.connect(lambda : self.stackedWidget.setCurrentWidget(self.page_sobre))
        self.btn_home.clicked.connect(lambda : self.stackedWidget.setCurrentWidget(self.page_home))
        self.btn_cadastrar.clicked.connect(lambda : self.stackedWidget.setCurrentWidget(self.page_cadastrar))
        self.btn_cadastrados.clicked.connect(lambda : self.stackedWidget.setCurrentWidget(self.page_cadastrados))
        self.btn_agendamento.clicked.connect(lambda : self.stackedWidget.setCurrentWidget(self.page_agendamento))
        self.btn_calendario.clicked.connect(lambda : self.stackedWidget.setCurrentWidget(self.page_calendario))
        #**************************************************************************************************

        #*********************BOTOES DA PAGINA DE CADASTRO DE MUNICIPE******************************************
        self.btn_novo_cadastro.clicked.connect(self.novo_municipe)
        self.le_cep.textChanged.connect(self.busca_cep)
        self.le_cpf.textChanged.connect(self.cpf_validate)
        self.btn_update_municipe_id.clicked.connect(self.get_dados_municipe)
        # **************************************************************************************************

        # *******************BOTOES DA PAGINA DE MUNICIPES CADASTRADOS***************************************************

        self.btn_update_municipe.clicked.connect(self.update_table_municipes)
        self.btn_delete_municipe.clicked.connect(self.delete_municipe)
        # **************************************************************************************************

        # ********************FILTRO DA TABELA MUNICIPES********************************************************
        self.le_pesquisa_municipe.textChanged.connect(self.filtro_municipes)
        # **************************************************************************************************

        # *******************ADICIONA A LISTA DE MUNICIPES AO COMBO BOX DA PAGINA AGENDAMENTOS*******************************************************************************
        self.add_municipes_combobox()
        # **************************************************************************************************

        # *********************ATUALIZA AS TABELAS DO SISTEMA*****************************************************************************
        self.table_reset()
        # **************************************************************************************************

    #FUNÇÃO QUE CRIA CAIXA DE DIALOGO DE ERRO
    def message_critical(self,txt):
        msg = QMessageBox(self)
        msg.setWindowTitle('ERRO DE DADOS')
        msg.setIcon(QMessageBox.Warning)
        msg.setText(f'{txt}')
        msg.exec_()

    #FUNÇÃO QUE CRIA CAIXA DE DIALOGO DE INFORMAÇÃO
    def message_information(self,txt):
        msg = QMessageBox(self)
        msg.setWindowTitle('DADOS ACEITOS')
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
            self.message_critical('O CAMPO "NOME" ESTA VAZIO')
        elif rg == '':
            self.message_critical('O CAMPO "RG" ESTA VAZIO')
        elif rg.isalpha():
            self.message_critical('O CAMPO "RG" DEVE SER NUMERICO')
            self.lv_rg.setText('')

        elif cpf == '':
            self.message_critical('O CAMPO "CPF" ESTA VAZIO')

        elif len(cpf) != 11:
            self.message_critical('O CAMPO "CPF" DEVE TER 11 DIGITOS')
            self.le_cpf.setText('')

        elif telefone == '':
            self.message_critical('O CAMPO "TELEFONE" ESTA VAZIO')

        elif telefone.isalpha():
            self.message_critical('O CAMPO "TELEFONE" DEVE SER NUMERICO')
            self.le_telefone.setText('')

        elif cep == '':
            self.message_critical('O CAMPO "CEP" ESTA VAZIO')

        elif endereco == '':
            self.message_critical('O CAMPO "ENDEREÇO" ESTA VAZIO')
        elif numero == '':
            self.message_critical('O CAMPO "NUMERO" ESTA VAZIO')
        elif bairro == '':
            self.message_critical('O CAMPO "BAIRRO" ESTA VAZIO')
        elif cidade == '':
            self.message_critical('O CAMPO "CIDADE" ESTA VAZIO')
        else:
            db.insert_municipes(nome, rg, cpf, data,telefone,instituicao, cep, endereco,numero,bairro,cidade)
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
            self.message_information('CADASTRO REALIZADO COM SUCESSO!!!')
            db.close_db()

    #FUNÇÃO QUE CONSOME A API DOS CORREIOS PARA VALIDAR O CEP E INCREMENTAR OS CAMPOS ENDEREÇO,BAIRRO,CIDADE NO CADASTRO
    def busca_cep(self,s):
        try:
            if len(s) == 8:
                cep = self.le_cep.text().strip().title()
                response = requests.get(f'http://viacep.com.br/ws/{cep}/json/')
                response = response.json()
                self.le_endereco.setText(f'{response["logradouro"]}')
                self.le_bairro.setText(f'{response["bairro"]}')
                self.le_cidade.setText(f'{response["localidade"]}')
        except:
            self.message_critical('CEP INVÁLIDO')
            self.le_cep.setText('')

    #FUNÇÃO QUE VALIDA O CPF
    def cpf_validate(self, numbers):
        if len(numbers) == 11:
            #  Obtém os números do CPF e ignora outros caracteres
            cpf = [int(char) for char in numbers if char.isdigit()]


            #  Verifica se o CPF tem todos os números iguais, ex: 111.111.111-11
            #  Esses CPFs são considerados inválidos mas passam na validação dos dígitos
            #  Antigo código para referência: if all(cpf[i] == cpf[i+1] for i in range (0, len(cpf)-1))
            if cpf == cpf[::-1]:
                self.message_critical('O CPF É INVÁLIDO')
                self.le_cpf.setText('')

            #  Valida os dois dígitos verificadores
            for i in range(9, 11):
                value = sum((cpf[num] * ((i + 1) - num) for num in range(0, i)))
                digit = ((value * 10) % 11) % 10
                if digit != cpf[i]:
                    return self.message_critical('CPF INVALIDO') , self.le_cpf.setText('')

            self.le_cpf.setText(numbers)

    #FUNÇÃO QUE PUXA OS DADOS DO BANCO DE DADOS E INCREMENTA OS CAMPOS DO CADASTRO PARA FAZER ALTERAÇÃO
    def get_dados_municipe(self):
        try:
            id = self.le_update_municipe.text()
            db = DataBase()
            db.conect_db()
            cursor = db.conection.cursor()
            cursor.execute(f'''
            SELECT * FROM municipes WHERE ID = '{id}';
            ''')
            municipe = cursor.fetchall()
            self.stackedWidget.setCurrentWidget(self.page_cadastrar)
            self.le_nome.setText(municipe[0][1])
            self.lv_rg.setText(municipe[0][2])
            self.le_cpf.setText(municipe[0][3])
            self.de_data_nascimento.setDate(QDate(int(municipe[0][4][6:]), int(municipe[0][4][3:5]), int(municipe[0][4][:2])))
            self.le_telefone.setText(municipe[0][5])
            self.le_instituicao.setText(municipe[0][6])
            self.le_cep.setText(municipe[0][7])
            # self.le_endereco.setText(municipe[0][8])
            self.le_numero.setText(municipe[0][9])
            # self.le_bairro.setText(municipe[0][10])
            # self.le_cidade.setText(municipe[0][11])


            db.close_db()
        except:
            self.stackedWidget.setCurrentWidget(self.page_cadastrados)
            self.le_update_municipe.setText('')
            self.message_critical('MUNICIPE NÃO ENCONTRADO')

    #FUNÇÃO QUE ATUALIZA A TABLEVIEW DO SISTEMA
    def update_table_municipes(self):
        msg = QMessageBox(self)
        msg.setWindowTitle('INFORMATIVO')
        msg.setText('TEM CERTEZA QUE DESEJA ATUALIZAR OS DADOS?')
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        result = msg.exec_()
        if result == QMessageBox.Yes:
            try:
                db = DataBase()
                db.conect_db()
                cursor = db.conection.cursor()
                id = self.le_update_municipe.text()
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

                cursor.execute(f'''
                UPDATE municipes set NOME = '{nome}', RG = '{rg}', CPF = '{cpf}', DATA_DE_NASCIMENTO = '{data}', TELEFONE = '{telefone}', INSTITUIÇÃO = '{instituicao}', CEP = '{cep}', ENDEREÇO = '{endereco}', NUMERO = '{numero}', BAIRRO = '{bairro}', CIDADE = '{cidade}' WHERE ID = {id};
    
                ''')
                db.conection.commit()
                self.le_update_municipe.setText('')
                self.le_nome.setText('')
                self.de_data_nascimento.setDate(QDate(2000, 1,1))
                self.lv_rg.setText('')
                self.le_cpf.setText('')
                self.le_telefone.setText('')
                self.le_instituicao.setText('')
                self.le_cep.setText('')
                self.le_endereco.setText('')
                self.le_numero.setText('')
                self.le_bairro.setText('')
                self.le_cidade.setText('')
                self.message_information('CADASTRO ALTERADO COM SUCESSO!!!')
                self.table_reset()
                db.close_db()
            except:
                pass
        else:
            pass

    #FUNÇÃO QUE PASSA DO BANCO DE DADOS MUNICIPE PARA A TABLEVIEW DO SISTEMA
    def show_table_municipe(self):
        db = QSqlDatabase('QSQLITE')
        db.setDatabaseName('system.db')
        db.open()

        self.model = QSqlTableModel(db=db)
        self.tb_municipes_cadastrados.setModel(self.model)
        self.model.setTable('municipes')
        self.model.select()

    # FUNÇÃO QUE PASSA DO BANCO DE DADOS AGENDAMENTOS PARA A TABLEVIEW DO SISTEMA
    def show_table_agendamentos(self):
        db = QSqlDatabase('QSQLITE')
        db.setDatabaseName('system.db')
        db.open()

        self.model = QSqlTableModel(db=db)
        self.tableView_agendamento.setModel(self.model)
        self.model.setTable('agendamentos')
        self.model.select()


    #FUNÇÃO QUE CARREGA AS TABLEVIEW NO SISTEMA AO SER INICIADO
    def table_reset(self):
        self.tb_municipes_cadastrados.update()
        self.tableView_agendamento.update()
        self.show_table_municipe()
        self.show_table_agendamentos()

    #FUNÇÃO PARA FILTRAR ATRAVÉS DO NOME OS MUNICIPES NA JANELA CADASTRADOS
    def filtro_municipes(self,s):
        s = re.sub('[\W_]+','',s)
        filter_str = f'NOME LIKE "%{s}%"'
        self.model.setFilter(filter_str)

    #FUNÇÃO QUE ADICIONA A LISTA DE MUNICIPES CADASTRADOS AO COMBO BOX
    def add_municipes_combobox(self):
        db = DataBase()
        db.conect_db()
        cursor = db.conection.cursor()
        cursor.execute('SELECT NOME FROM municipes')
        for nome in cursor.fetchall():
            self.comboBox_municipe.addItem(nome[0])
        db.close_db()

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
            msg.setText(f'TEM CERTEZA QUE DESEJA DELETAR O CADASTRO DE "{nome[0]}"?')
            msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            result = msg.exec_()
            if result == QMessageBox.No: self.le_delete_municipe.setText('')
            else:
                cursor.execute(f'DELETE FROM municipes WHERE ID = {id}')
                db.conection.commit()
                self.le_delete_municipe.setText('')
                self.table_reset()
                db.conect_db()
        except:
            self.message_critical('MUNICIPE NÃO ENCONTRADO')
            self.le_delete_municipe.setText('')




















if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Login()
    window.show()
    app.exec_()
