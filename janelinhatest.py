import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton

class Janelinha(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Janelinha")
        self.setGeometry(600, 100, 800, 600)
        self.setFixedWidth(800)

        #TITULO
        self.titulo_label = QLabel("Welcome to E-mail")
        self.titulo_label.setStyleSheet("QLabel { font-family: saura; font-weight: bold; font-size: 30pt; color: #000000; }")
        self.titulo_label.setAlignment(Qt.AlignCenter)
        self.titulo_label.setFixedHeight(100)

        #SUBTITULO
        self.subtitulo_label = QLabel("Please enter your e-mail and password to continue")
        self.subtitulo_label.setStyleSheet("QLabel { font-family: comic-sans; font-weight: bold; font-size: 15pt; color: #000000; }")
        self.subtitulo_label.setAlignment(Qt.AlignCenter)
        self.subtitulo_label.setFixedHeight(100)

        #EMAIL
        self.email_label = QLabel("E-mail Address:")
        self.email_label.setAlignment(Qt.AlignCenter)
        self.email_edit = QLineEdit()
        self.email_edit.setStyleSheet("QLineEdit { font-size: 15pt; padding: 5px; }")

        #PASSWORD
        self.password_label = QLabel("Password:")
        self.password_label.setAlignment(Qt.AlignCenter)
        self.password_edit = QLineEdit()
        self.password_edit.setStyleSheet("QLineEdit { font-size: 15pt; padding: 5px; }")
        self.password_edit.setEchoMode(QLineEdit.Password)

        #BOTAO
        self.login_button = QPushButton("Login")
        self.login_button.setFixedWidth(200)
        
        #LAYOUT
        layout = QVBoxLayout()
        layout.setContentsMargins(50, 30, 50, 30)
        layout.setSpacing(5)
        layout.addStretch()
        layout.addWidget(self.titulo_label)
        layout.addWidget(self.subtitulo_label)
        layout.addWidget(self.email_label)
        layout.addWidget(self.email_edit)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_edit)
        layout.addWidget(self.login_button, alignment=Qt.AlignTop)
        layout.addStretch()

        self.setLayout(layout)

        # Vamos vincular o funcinamento da janela com
# o gerenciamento do sistema operacional. Assim
# o sistema operacional saberá lidar com a janela
# em memória
app = QApplication(sys.argv)
# instância da janela para por em funcionamento
janela = Janelinha()
# exibir a janela na tela
janela.show()
# executar a janela
app.exec_()