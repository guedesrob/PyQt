# neste exemplo não convertemos o arquivo .ui em .py
# Operações com Radio Button

from PyQt5 import uic, QtWidgets
# modulo uic: permite-se trabalhar com arquivos .ui
# QtWidgets: poermite usar os componentes (mostrar os componentes na tela)

def funcao_principal():
    if formulario.radioButton.isChecked():
        print("Opção 1 selecionada")
        opcao = "Opção 1 selecionada"
    elif formulario.radioButton_2.isChecked():
        print("Opção 2 selecionada")
        opcao = "Opção 2 selecionada"
    elif formulario.radioButton_3.isChecked():
        print("Opção 3 selecionada")
        opcao = "Opção 3 selecionada"
    elif formulario.radioButton_4.isChecked():
        print("Opção 4 selecionada")
        opcao = "Opção 4 selecionada"
    else:
        print("")
        opcao = ""

    formulario.label_2.setText(opcao) # setText: metodo que edita o texto da label

app = QtWidgets.QApplication([]) # inicializa-se a plicação na variavel app
formulario = uic.loadUi("janela_cores.ui") #Importa-se o arquivo "janela.ui" para a variavel formulario, através do método loadUI
formulario.pushButton.clicked.connect(funcao_principal)

formulario.show()
app.exec()