#Classe importante: QLabel
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QToolTip, QLabel

class Janela (QMainWindow):

    def __init__(self):
        super().__init__()
        self.topo = 100
        self.esquerda = 100
        self.largura = 800
        self.altura = 600
        self.titulo = "Primeira Janela"

        botao1 = QPushButton('Botao 1', self) 
        botao1.move(150,200) 
        botao1.resize(150,80) 
        botao1.setStyleSheet('QPushButton {background-color:#20C12B;font:bold;font-size:20px}') 
        botao1.clicked.connect(self.botao1_click)

        botao2 = QPushButton('Botao 2', self)
        botao2.move(350,200)
        botao2.resize(150,80)
        botao2.setStyleSheet('QPushButton {background-color:#20C12B;font:bold;font-size:20px}')
        botao2.clicked.connect(self.botao2_click)
        
        # Para que a label fique visivel fora do construtor, é necessário colocar o "self" antes dele
        self.label_1 = QLabel(self) # Cria-se o objeto label da classe QLabel
        self.label_1.setText("Olá Mundo") # determina o texto da label
        self.label_1.resize(400,25) # dimensiona o tamanho da label
        self.label_1.move(50,50) # move a label na tela
        self.label_1.setStyleSheet('QLabel {font-size:25px;color:"blue"}') # Determina o estilo da Label
        
        self.CarregarJanela()

    def CarregarJanela(self):
        self.setGeometry(self.esquerda,self.topo,self.largura,self.altura)
        self.setWindowTitle(self.titulo)
        self.show()

    def botao1_click(self):
        self.label_1.setText("O botão 1 foi clicado")

    def botao2_click(self):
        self.label_1.setText("O botão 2 foi clicado")

aplicacao = QApplication(sys.argv)
j= Janela()
sys.exit(aplicacao.exec_()