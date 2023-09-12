#Classe importante: QtGui
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QToolTip, QLabel
from PyQt5 import QtGui

class Janela (QMainWindow):

    def __init__(self):
        super().__init__()
        self.topo = 100
        self.esquerda = 100
        self.largura = 800
        self.altura = 800
        self.titulo = "Aperte o botão"

        botao1 = QPushButton('Botão 1', self) 
        botao1.move(150,200) 
        botao1.resize(150,80) 
        botao1.setStyleSheet('QPushButton {background-color:"red";font:bold;font-size:15px}') 
        botao1.clicked.connect(self.botao1_click)

        botao2 = QPushButton('Botão 2', self)
        botao2.move(350,200)
        botao2.resize(200,80)
        botao2.setStyleSheet('QPushButton {background-color:"yellow";font:bold;font-size:15px}')
        botao2.clicked.connect(self.botao2_click)
        
        self.label_1 = QLabel(self)
        self.label_1.resize(400,25)
        self.label_1.move(50,50)
        self.label_1.setStyleSheet('QLabel {font-size:25px;color:"red"}')

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
        self.imagem.setPixmap(QtGui.QPixmap('1.png'))
        self.label_1.setStyleSheet('QLabel {font-size:25px;color:"red"}')
        self.imagem.move(200,400)

    def botao2_click(self):
        self.label_1.setText("RUN ahahahahaha")
        self.label_1.setStyleSheet('QLabel {font-size:25px;color:"blue"}')
        self.imagem.move(400,400)
        self.imagem.setPixmap(QtGui.QPixmap('2.png'))

aplicacao = QApplication(sys.argv)
j= Janela()
sys.exit(aplicacao.exec_())