import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
# PyQt5.QtWidgets -> Importar submódulo
# QApplication, QMainWindow -> Importar classes

class Janela (QMainWindow): # Estamos criando uma subclasse Janela, filha da classe QMainWindows

    def __init__(self): # método contrutor
        super().__init__() # Chama o método construtor da superclasse (QMainWindow) por herança
        self.topo = 100 # atributo que define a distância do topo da janela à borda da tela superior (100pixel)
        self.esquerda = 100
        self.largura = 800
        self.altura = 600
        self.titulo = "Primeira Janela"
        self.CarregarJanela() # Carrega o metodo Carregar janela definido a seguir

    def CarregarJanela(self): # Cria o metodo Carregar janela
        self.setGeometry(self.esquerda,self.topo,self.largura,self.altura)
        self.setWindowTitle(self.titulo)
        self.show()

aplicacao = QApplication(sys.argv) # Cria-se o objeto, referencia do qapplication # sys.argv meche nos paranmetros do sistema, responsavel por fechar a janela
j= Janela() # Cria-se outro objeto que vai instanciar a classe janela
sys.exit(aplicacao.exec_()) # Não entendi direito o que esse comando faz ()
# fim