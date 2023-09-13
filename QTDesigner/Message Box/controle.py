from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMessageBox # Toolbox que permite mostrar mensagem de alerta
# modulo uic: permite-se trabalhar com arquivos .ui
# QtWidgets: permite usar os componentes (mostrar os componentes na tela)

def exibir_mensagem():
    dado_lido = janela.lineEdit.text() # Le e armazena o que foi digitado na lineEdit ao se clicar no pushButton
    print(dado_lido)
    janela.lineEdit.setText("")
    if dado_lido=="":
        QMessageBox.about(janela,"alerta","Nenhum nome digitado") # exibe um alerta caso nada seja digitado
    else:
        QMessageBox.about(janela,"alerta","Olá: "+dado_lido) # Exibe uma saldação ao nome digitado

app = QtWidgets.QApplication([]) # inicializa-se a plicação na variavel app
janela = uic.loadUi("cx.ui") #Importa-se o arquivo "lista.ui" para a variavel lista, através do método loadUI
janela.pushButton.clicked.connect(exibir_mensagem) #Conecta o pushbutton 1 ao metodo listar_dados

janela.show()
app.exec()