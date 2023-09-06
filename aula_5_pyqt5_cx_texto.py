#Classe importante: QtGui
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QToolTip, QLabel, QLineEdit
from PyQt5 import QtGui

class Janela (QMainWindow):

    def __init__(self):
        super().__init__()
        self.topo = 100
        self.esquerda = 100
        self.largura = 800
        self.altura = 800
        self.titulo = "Janela"

        self.caixa_texto = QLineEdit(self)
        self.caixa_texto.move(25,10)
        self.caixa_texto.resize(250,40)

        botao1 = QPushButton('Botão 1', self) 
        botao1.move(150,200) 
        botao1.resize(100,80) 
        botao1.setStyleSheet('QPushButton {background-color:#FF0000;font:bold;font-size:15px}') 
        botao1.clicked.connect(self.botao1_click)

        botao2 = QPushButton('Botão 2', self)
        botao2.move(250,200)
        botao2.resize(100,80)
        botao2.setStyleSheet('QPushButton {background-color:#00C900;font:bold;font-size:15px}')
        botao2.clicked.connect(self.botao2_click)

        botao_caixa = QPushButton('Enviar texto',self)
        botao_caixa.move(350,200) 
        botao_caixa.resize(100,80) 
        botao_caixa.setStyleSheet('QPushButton {background-color:#FF0000;font:bold;font-size:15px}') 
        botao_caixa.clicked.connect(self.mostra_texto)
        
        self.label_1 = QLabel(self)
        self.label_1.resize(400,25)
        self.label_1.move(50,100)
        self.label_1.setStyleSheet('QLabel {font-size:25px;color:"red"}')

        self.label_caixa = QLabel(self)
        self.label_caixa.move(500,100)
        self.label_caixa.setStyleSheet('QLabel {font-size:25px;color:"black"}')
        self.label_caixa.resize(400,100)
        self.label_caixa.setText("Digite um texto:") 

        self.imagem = QLabel(self)
        self.imagem.move(50,400)
        self.imagem.resize(400,400)

        self.CarregarJanela()

    def CarregarJanela(self):
        self.setGeometry(self.esquerda,self.topo,self.largura,self.altura)
        self.setWindowTitle(self.titulo)
        self.show()

    def botao1_click(self):
        self.label_1.setText("Apertou o botão 1")
        self.imagem.setPixmap(QtGui.QPixmap('3.png'))
        self.label_1.setStyleSheet('QLabel {font-size:25px;color:"red"}')
        self.imagem.move(200,400)

    def botao2_click(self):
        self.label_1.setText("Apertou o botão 2")
        self.label_1.setStyleSheet('QLabel {font-size:25px;color:"blue"}')
        self.imagem.move(400,400)
        self.imagem.setPixmap(QtGui.QPixmap('2.png'))

    def mostra_texto(self):
        conteudo = self.caixa_texto.text()
        self.label_caixa.setText("Digitou: " + conteudo)


aplicacao = QApplication(sys.argv)
j= Janela()
sys.exit(aplicacao.exec_())