import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (
    QApplication, QWidget, QHBoxLayout, QVBoxLayout, QLabel, 
    QTableWidget, QTableWidgetItem, QLineEdit, QMessageBox
)

class caixa2(QWidget):
    def __init__(self):
        super().__init__()

        self.total = 0.0
        self.linha = 0

        self.setGeometry(0, 40, 1700, 1000)

        # === COLUNA ESQUERDA ===
        self.imagem_label = QLabel()
        self.imagem_label.setPixmap(QPixmap(".venv/pao.jpg"))
        self.imagem_label.setScaledContents(True)
        self.imagem_label.setFixedSize(900, 590)

        self.codigo_produto_label = QLabel("Código do Produto")
        self.codigo_edit = QLineEdit()

        self.nome_label = QLabel("Nome do Produto")
        self.nome_edit = QLineEdit()

        self.descricao_label = QLabel("Descrição do Produto")
        self.descricao_edit = QLineEdit()

        self.quantidade_label = QLabel("Quantidade do Produto")
        self.quantidade_edit = QLineEdit()

        self.preco_label = QLabel("Preço Unitário do Produto")
        self.preco_edit = QLineEdit()

        self.subtotal_label = QLabel("Sub Total:")
        self.subtotal_edit = QLineEdit()
        self.subtotal_edit.setEnabled(False)

        self.vertical_esquerda_layout = QVBoxLayout()
        self.vertical_esquerda_layout.addWidget(self.imagem_label)
        self.vertical_esquerda_layout.addWidget(self.codigo_produto_label)
        self.vertical_esquerda_layout.addWidget(self.codigo_edit)
        self.vertical_esquerda_layout.addWidget(self.nome_label)
        self.vertical_esquerda_layout.addWidget(self.nome_edit)
        self.vertical_esquerda_layout.addWidget(self.descricao_label)
        self.vertical_esquerda_layout.addWidget(self.descricao_edit)
        self.vertical_esquerda_layout.addWidget(self.quantidade_label)
        self.vertical_esquerda_layout.addWidget(self.quantidade_edit)
        self.vertical_esquerda_layout.addWidget(self.preco_label)
        self.vertical_esquerda_layout.addWidget(self.preco_edit)
        self.vertical_esquerda_layout.addWidget(self.subtotal_label)
        self.vertical_esquerda_layout.addWidget(self.subtotal_edit)

        self.coluna_esquerda_label = QLabel()
        self.coluna_esquerda_label.setLayout(self.vertical_esquerda_layout)

        # === COLUNA DIREITA ===
        self.coluna_direita_label = QLabel()
        self.layoutvertical_direita = QVBoxLayout()

        self.tabela = QTableWidget()
        self.tabela.setColumnCount(5)
        self.tabela.setHorizontalHeaderLabels(["Código", "Nome", "Quantidade", "Preço Unitário", "Preço Total"])

        self.totalapagar_label = QLabel("Total a Pagar")
        self.totalapagar_edit = QLineEdit("0.00")
        self.totalapagar_edit.setEnabled(False)
        self.totalapagar_edit.setStyleSheet("QLineEdit { font-size: 40pt; font-weight: bold; }")

        self.layoutvertical_direita.addWidget(self.tabela)
        self.layoutvertical_direita.addWidget(self.totalapagar_label)
        self.layoutvertical_direita.addWidget(self.totalapagar_edit)
        self.coluna_direita_label.setLayout(self.layoutvertical_direita)

        # === LAYOUT PRINCIPAL ===
        self.horizontal_layout = QHBoxLayout()
        self.horizontal_layout.addWidget(self.coluna_esquerda_label)
        self.horizontal_layout.addWidget(self.coluna_direita_label)
        self.setLayout(self.horizontal_layout)

        # Evento de teclado
        self.keyPressEvent = self.capturaTecla

    # === CAPTURA DE TECLAS ===
    def capturaTecla(self, e):
        # F2 → calcula subtotal
        if e.key() == Qt.Key_F2:
            try:
                quantidade = float(self.quantidade_edit.text())
                preco = float(self.preco_edit.text())
                subtotal = quantidade * preco
                self.subtotal_edit.setText(f"{subtotal:.2f}")
            except ValueError:
                QMessageBox.warning(self, "Erro", "Digite valores numéricos válidos!")

        # F3 → adiciona item à tabela e soma total
        elif e.key() == Qt.Key_F3:
            try:
                codigo = self.codigo_edit.text()
                nome = self.nome_edit.text()
                quantidade = float(self.quantidade_edit.text())
                preco = float(self.preco_edit.text())
                subtotal = quantidade * preco

                self.tabela.insertRow(self.linha)
                self.tabela.setItem(self.linha, 0, QTableWidgetItem(codigo))
                self.tabela.setItem(self.linha, 1, QTableWidgetItem(nome))
                self.tabela.setItem(self.linha, 2, QTableWidgetItem(str(quantidade)))
                self.tabela.setItem(self.linha, 3, QTableWidgetItem(f"{preco:.2f}"))
                self.tabela.setItem(self.linha, 4, QTableWidgetItem(f"{subtotal:.2f}"))

                # soma no total geral
                self.total += subtotal
                self.totalapagar_edit.setText(f"{self.total:.2f}")

                self.linha += 1


            except ValueError:
                QMessageBox.warning(self, "Erro", "Preencha os campos corretamente!")

        # F4 → confirma pagamento
        elif e.key() == Qt.Key_F4:
            op = QMessageBox.question(self, "Pagamento", "Deseja efetuar o pagamento?")
            if op == QMessageBox.Yes:
                QMessageBox.information(self, "Pagamento", "Pagamento efetuado com sucesso!")
                self.tabela.setRowCount(0)
                self.totalapagar_edit.setText("0.00")
                self.total = 0.0
                self.linha = 0
            else:
                QMessageBox.information(self, "Pagamento", "Pagamento cancelado.")

# === EXECUÇÃO ===
app = QApplication(sys.argv)
janela = caixa2()
janela.show()
app.exec_()
