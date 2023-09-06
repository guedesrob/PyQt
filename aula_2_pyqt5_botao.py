# Classe importantante: QPushButton, QToolTip
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QToolTip

class Janela (QMainWindow):

    def __init__(self):
        super().__init__()
        self.topo = 100
        self.esquerda = 100
        self.largura = 800
        self.altura = 600
        self.titulo = "Primeira Janela"

        botao1 = QPushButton('Botao 1', self) # Cria-se o botao: instacia-se a classe QPushButton
        botao1.move(150,200) # Aplica-se o metodo move ao objeto botao1 (posição do botao )
        botao1.resize(150,80) # Aplica-se o metodo resize ao objeto botao1 (dimensões do botao)
        botao1.setStyleSheet('QPushButton {background-color:#20C12B;font:bold;font-size:20px}') # Usar conversor de rgb para hexadecimal
        botao1.clicked.connect(self.botao1_click)

        botao2 = QPushButton('Botao 2', self) # Cria-se o botao: instatia-se a classe QPushButton
        botao2.move(350,200) # Aplica-se o metodo move ao objeto botao1 (posição do botao )
        botao2.resize(150,80) # Aplica-se o metodo resize ao objeto botao1 (dimensões do botao)
        botao2.setStyleSheet('QPushButton {background-color:#20C12B;font:bold;font-size:20px}') # Usar conversor de rgb para hexadecimal
        botao2.clicked.connect(self.botao2_click) # conecta um metodo ao botao

        # botao1 deve ser criado antes de se carregar a janela
        self.CarregarJanela() # Carrega o metodo Carregar janela definido a seguir

    def CarregarJanela(self): # Cria o metodo Carregar janela
        self.setGeometry(self.esquerda,self.topo,self.largura,self.altura)
        self.setWindowTitle(self.titulo)
        self.show()

    def botao1_click(self): # Cria-se um método que printa uma mensagem
        print('O Botao 1 foi clicado')

    def botao2_click(self):
        print('O Botao 2 foi clicado')

aplicacao = QApplication(sys.argv)
j= Janela()
sys.exit(aplicacao.exec_())