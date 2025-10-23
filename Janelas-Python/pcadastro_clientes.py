import sys
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QLabel,QLineEdit, QComboBox, QVBoxLayout, QHBoxLayout, QPushButton

class CadastroClientes(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Cadastro de Clientes")
        self.setGeometry(50,50,1000,800)
        self.setFixedSize(1200,800)

        self.setWindowIcon(QIcon(".venv/iconecliente1.png"))

        self.horizontal_layout = QHBoxLayout()
        self.esquerda_label = QLabel()
        self.esquerda_label.setPixmap(QPixmap(".venv/clientes.jpg"))
        self.esquerda_label.setFixedWidth(600)
        self.esquerda_label.setScaledContents(True)



        self.direita_label = QLabel()
        self.direita_label.setFixedWidth(600)
        self.direita_label.setStyleSheet("QLabel{background-color:white}")

        self.vertical_layout = QVBoxLayout()
        self.titulo_label = QLabel("Cadastro de Clientes")
        self.titulo_label.setStyleSheet("QLabel{font-family:tahoma; font-weight:bold; font-style:italic; font-size:20pt;color:#DB7D66}")
        self.vertical_layout.addWidget(self.titulo_label)

        # ------------- Nome do cliente -----------------------------------
        self.nome_label = QLabel("Nome Completo")
        self.nome_label.setStyleSheet("QLabel{font-size:15pt}")

        self.nome_edit = QLineEdit()
        self.nome_edit.setStyleSheet("QLineEdit{font-size:15pt}")

        self.vertical_layout.addWidget(self.nome_label)
        self.vertical_layout.addWidget(self.nome_edit)
        #  --------------- Fim do Nome do cliente ------------------------------


        # -------------- E-Mail do cliente -------------------------------------
        self.email_label = QLabel("E-Mail")
        self.email_label.setStyleSheet("QLabel{font-size:15pt}")

        self.email_edit = QLineEdit()
        self.email_edit.setStyleSheet("QLineEdit{font-size:15pt}")

        self.vertical_layout.addWidget(self.email_label)
        self.vertical_layout.addWidget(self.email_edit)
        # --------------- Fim do E-mail -----------------------------------------

        # ---------------- Telefone do cliente ----------------------------------
        self.telefone_label = QLabel("Telefone")
        self.telefone_label.setStyleSheet("QLabel{font-size:15pt}")

        self.telefone_edit = QLineEdit()
        self.telefone_edit.setStyleSheet("QLineEdit{font-size:15pt}")

        self.vertical_layout.addWidget(self.telefone_label)
        self.vertical_layout.addWidget(self.telefone_edit)

        # ------------------ Fim do telefone ----------------------------------------

        # -------------------- CPF do cliente ---------------------------------------
        self.cpf_label = QLabel("CPF")
        self.cpf_label.setStyleSheet("QLabel{font-size:15pt}")

        self.cpf_edit = QLineEdit()
        self.cpf_edit.setStyleSheet("QLineEdit{font-size:15pt}")

        self.vertical_layout.addWidget(self.cpf_label)
        self.vertical_layout.addWidget(self.cpf_edit)
        # ---------------------- Fim ------------------------------------

        # ---------------------- Data de Nascimento ------------------------

        self.datanascimento_label = QLabel("Data de Nascimento")
        self.datanascimento_label.setStyleSheet("QLabel{font-size:15pt}")

        self.datanascimento_edit = QLineEdit()
        self.datanascimento_edit.setStyleSheet("QLineEdit{font-size:15pt}")

        self.vertical_layout.addWidget(self.datanascimento_label)
        self.vertical_layout.addWidget(self.datanascimento_edit)
        # ---------------------- Fim data nascimento --------------------------------

        # ---------------------- Endereco ----------------------------------
        self.endereco_label = QLabel("Endereço")
        self.endereco_label.setStyleSheet("QLabel{font-size:15pt}")

        self.endereco_edit = QLineEdit()
        self.endereco_edit.setStyleSheet("QLabel{font-size:15pt}")

        self.vertical_layout.addWidget(self.endereco_label)
        self.vertical_layout.addWidget(self.endereco_edit)
        # -------------------- Fim do Endereco --------------------------

        self.sexo_label = QLabel("Sexo")
        self.sexo_label.setStyleSheet("QLabel{font-size:15pt}")

        self.sexo_combo = QComboBox()
        self.sexo_combo.setStyleSheet("QComboBox{font-size:15pt}")
        self.sexo_combo.addItem("Selecione ... ")
        self.sexo_combo.addItem("Masculino")
        self.sexo_combo.addItem("Feminino")
        

        self.vertical_layout.addWidget(self.sexo_label)
        self.vertical_layout.addWidget(self.sexo_combo)
        # ---------------------------------------------------------------

        self.gravar_button = QPushButton("Gravar")
        self.gravar_button.clicked.connect(self.gravar)
        self.gravar_button.setStyleSheet("QPushButton{font-size:15pt}")
        self.vertical_layout.addWidget(self.gravar_button)



        self.direita_label.setLayout(self.vertical_layout)

        self.horizontal_layout.addWidget(self.esquerda_label)
        self.horizontal_layout.addWidget(self.direita_label)
        
        self.setLayout(self.horizontal_layout)

    def gravar(self):
        print("Clicou no botão")


app = QApplication(sys.argv)
janela = CadastroClientes()
janela.show()
app.exec_()