from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox # Toolbox que permite mostrar mensagem de alerta
# modulo uic: permite-se trabalhar com arquivos .ui
# QtWidgets: permite usar os componentes (mostrar os componentes na tela)

def exibir_mensagem():
    print(dado_lido)

app = QtWidgets.QApplication([]) # inicializa-se a plicação na variavel app
janela = uic.loadUi("cx.ui") #Importa-se o arquivo "lista.ui" para a variavel lista, através do método loadUI
janela.pushButton.clicked.connect(exibir_mensagem) #Conecta o pushbutton 1 ao metodo listar_dados

janela.show()
app.exec()