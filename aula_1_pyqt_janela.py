# Classes importantes: QApplication, QMainWindow
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

# Cria-se o objeto, instância do QApplication
aplicacao = QApplication(sys.argv)
# sys.argv meche nos parametros do sistema, responsavel por fechar a janela
# Cria-se outro objeto que vai instanciar a classe janela
j= Janela() # Cria-se um objeto da classe janela, carregando a janela

# Comentário Lucas:
# codigo_de_saida = aplicacao.exec_() #Executa o aplicativo. 
# Para a execução do código, abre a janela, e deixa o usuário interagir com ela.
# sys.exit(codigo_de_saida) #fecha o sistema que está sendo executado, retornando 
# o mesmo código de saída do aplicativo.
# https://doc.qt.io/qt-5/qapplication.html#exec

sys.exit(aplicacao.exec_())

# Alternativa:
# codigo_de_saida = aplicacao.exec_()
# sys.exit(codigo_de_saida)

# import sys
# O módulo sys é usado para parâmetros e funções específicas do sistema. 
# Fornece acesso a algumas variáveis utilizadas ou mantidas pelo intérprete 
# e a funções que interagem fortemente com o intérprete. Por exemplo, 
# fornece acesso à lista de argumentos de linha de comando passados para 
# um script Python1.