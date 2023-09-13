from PyQt5 import uic, QtWidgets
# Toolbox que permite mostrar mensagem de alerta
# modulo uic: permite-se trabalhar com arquivos .ui
# QtWidgets: permite usar os componentes (mostrar os componentes na tela)

def Troca_Frame_1():
    tela.frame_2.close()

def Troca_Frame_2():
    tela.frame_2.show()

app = QtWidgets.QApplication([]) # inicializa-se a plicação na variavel app
tela = uic.loadUi("Frame.ui") #Importa-se o arquivo "lista.ui" para a variavel lista, através do método loadUI
tela.pushButton_2.clicked.connect(Troca_Frame_1) #Conecta o pushbutton 1 ao metodo listar_dados
tela.pushButton_3.clicked.connect(Troca_Frame_2) #Conecta o pushbutton 1 ao metodo listar_dados

tela.show()
app.exec()