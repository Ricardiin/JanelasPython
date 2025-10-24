import sys
import webbrowser
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap , QIcon
from PyQt5.QtWidgets import QApplication,QWidget,QHBoxLayout,QVBoxLayout,QLabel,QTableWidget,QTableWidgetItem,QLineEdit,QComboBox,QMessageBox,QInputDialog,QCheckBox




class Janelinha(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Janelinha")
        self.setGeometry(600,100,800,800)
        self.setFixedWidth(800)
        #superior
        self.superior_label = QLabel()
        #titulo

        self.titulo_label = QLabel("Welcome to E-mail")
        self.titulo_label.setStyleSheet("QLabel{font-family:saira; font-weight:bold; font-style:bold; font-size:30pt;color:#000000}")
        self.titulo_label.setAlignment(Qt.AlignCenter)
        self.titulo_label.setFixedHeight(100)

        #subtitulo
        self.subtitulo_label = QLabel("Please enter your e-mail and password to continue")
        self.subtitulo_label.setStyleSheet("QLabel{font-family:comic-sans; font-weight:bold;  font-size:15pt;color:#000000}")
        self.subtitulo_label.setAlignment(Qt.AlignCenter)
        self.subtitulo_label.setFixedHeight(50)
        #email
        self.email_label = QLabel("E-mail address:")
        self.email_label.setStyleSheet("QLineEdit{font-size:15pt}")
        self.email_edit = QLineEdit()
        self.email_label.setFixedHeight(15)
        self.email_label.setAlignment(Qt.AlignTop)
        self.email_label.setAlignment(Qt.AlignHCenter)
        


        self.email_edit.setStyleSheet("QLineEdit{font-size:15pt}")



        #password
        self.password_label = QLabel("Password:")
        self.password_label.setAlignment(Qt.AlignCenter)
        self.password_label.setFixedHeight(500)

        self.password_edit = QLineEdit()
        self.password_edit.setStyleSheet("QLineEdit{font-size:15pt}")
        self.password_edit.setEchoMode(QLineEdit.Password)
        self.password_edit.setAlignment(Qt.AlignCenter)
        self.password_label.setAlignment(Qt.AlignTop)


        

        #controles
        self.v_controles = QVBoxLayout()

        self.v_controles.addWidget(self.email_label)
        self.v_controles.addWidget(self.email_edit)
        self.v_controles.addWidget(self.password_label)
        self.v_controles.addWidget(self.password_edit)

        #Controles 
        self.superior_label.setLayout(self.v_controles)

        #controles vertical 
        self.v_layout = QVBoxLayout()

        #self.v_layout.addWidget(self.superior_label)
        self.v_layout.addWidget(self.titulo_label)
        self.v_layout.addWidget(self.subtitulo_label)
        self.v_layout.addWidget(self.email_label)
        self.v_layout.addWidget(self.email_edit)

        self.v_layout.addWidget(self.password_label)
        self.v_layout.addWidget(self.password_edit)

        
        #add nas janelas
        self.setLayout(self.v_layout)
        
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