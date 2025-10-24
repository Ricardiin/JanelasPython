import sys
from PyQt5.QtCore import Qt 
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout,QLabel, QLineEdit, QPushButton, QCheckBox
from PyQt5.QtGui import QPixmap, QIcon

#começo da janelinha 
class Janelinha(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Janelinha")
        self.setGeometry(600, 100, 800, 600)
        self.setFixedWidth(800)

        self.setWindowIcon(QIcon(".venv/icon.png"))

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
        self.email_edit.setStyleSheet("QLineEdit { font-size: 15pt; padding: 5px; border-radius: 18px;}")
        self.email_edit.setFixedWidth(400)


        #PASSWORD
        self.password_label = QLabel("Password:")
        self.password_label.setAlignment(Qt.AlignCenter)
        self.password_edit = QLineEdit()
        self.password_edit.setStyleSheet("QLineEdit { font-size: 15pt; padding: 5px; border-radius: 18px;}")
        self.password_edit.setEchoMode(QLineEdit.Password)
        self.password_edit.setFixedWidth(400)
        
        #Remember me e forgot
        self.lembrar_label = QLabel ("Remember me ")
        self.lembrar_checkbox = QCheckBox ()

        self.forgot_label = QLabel ("Forgot you password")
        self.forgot_label.setStyleSheet("QLabel { color:blue ; }")

        

        #BOTAO
        self.login_button = QPushButton("Login")
        #self.login_button.setStyleSheet("QPushButton { border: 1px solid red; }")
        self.facebook_button = QPushButton("Facebook")
        self.login_button.setStyleSheet("""
            QPushButton {
                border: 2px solid #0078D7;
                border-radius: 18px;
                background-color: white;
                color: #0078D7;
                padding: 8px 55px;
                font-size: 11pt;
            }
            QPushButton:hover {
                background-color: #0078D7;
                color: white;
            }
        """)

        self.facebook_button.setFixedWidth(150)
        self.google_button = QPushButton("Google")
        self.google_button.setFixedWidth(150)
        self.google_button.setStyleSheet("background-color:red;")
        
        #LAYOUT VERTICAL DA JANELINHA
        layout = QVBoxLayout()
        layout.setContentsMargins(50, 30, 50, 30)
        layout.setSpacing(5)
        layout.addStretch()
        layout.addWidget(self.titulo_label)
        layout.addWidget(self.subtitulo_label)
        layout.addWidget(self.email_label)
        layout.addWidget(self.email_edit,alignment=Qt.AlignCenter)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_edit, alignment=Qt.AlignCenter)
        layout.addWidget(self.login_button, alignment=Qt.AlignCenter)
        layout.addWidget(self.lembrar_checkbox)
        layout.addWidget(self.lembrar_label)
        layout.addWidget(self.forgot_label,alignment=Qt.AlignLeft)
        #layout.addWidget(self.facebook_button,)
        #layout.addWidget(self.google_button)
        
        layout.addStretch()

        self.setLayout(layout)

        #LAYOUT HORIZONTAL DA JANELINHA
        layout_h = QHBoxLayout ()

        layout_h.addWidget(self.facebook_button,alignment=Qt.AlignRight,)
        layout_h.addWidget(self.google_button,alignment=Qt.AlignLeft)

        layout_h = QPushButton("Facebook")
        layout.addWidget(layout_h)
        layout_h.setStyleSheet("""
            QPushButton {
                border: 2px solid #0078D7;
                border-radius: 18px;
                background-color: white;
                color: #0078D7;
                padding: 8px 55px;
                font-size: 11pt;
            }
            QPushButton:hover {
                background-color: #0078D7;
                color: white;
            }
        """)

        self.setLayout(layout)

        layout_h = QPushButton("Google")
        layout.addWidget(layout_h)
        layout_h.setStyleSheet("""
            QPushButton {
                border: 2px solid #0078D7;
                border-radius: 18px;
                background-color: white;
                color: #0078D7;
                padding: 8px 55px;
                font-size: 11pt;
                               
            }
            QPushButton:hover {
                background-color: #0078D7;
                color: white;
            }
        """)
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