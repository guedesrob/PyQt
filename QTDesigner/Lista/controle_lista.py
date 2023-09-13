from PyQt5 import uic, QtWidgets
# modulo uic: permite-se trabalhar com arquivos .ui
# QtWidgets: permite usar os componentes (mostrar os componentes na tela)

def listar_dados():
    dado_lido = lista.lineEdit.text() # Le e armazena o que foi digitado na lineEdit ao se clicar no pushButton
    lista.listWidget.addItem(dado_lido) # Add Ao listwidget o que esta armazenado em dado_lido
    lista.lineEdit.setText("") # Limpa o campo do lineEdit, após digitação

def deletar():
    lista.listWidget.clear() # limpa todos os valores da lista

app = QtWidgets.QApplication([]) # inicializa-se a plicação na variavel app
lista = uic.loadUi("lista.ui") #Importa-se o arquivo "lista.ui" para a variavel lista, através do método loadUI
lista.pushButton.clicked.connect(listar_dados) #Conecta o pushbutton 1 ao metodo listar_dados
lista.pushButton_2.clicked.connect(deletar) #Conecta o pushbutton 2 ao metodo deletar

lista.show()
app.exec()