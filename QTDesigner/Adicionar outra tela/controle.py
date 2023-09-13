from PyQt5 import uic, QtWidgets
# modulo uic: permite-se trabalhar com arquivos .ui
# QtWidgets: permite usar os componentes (mostrar os componentes na tela)

def chama_segunda_tela():
    segunda_tela.show()
    # segunda_tela.label.setText("Esta é a segunda Tela")

app = QtWidgets.QApplication([]) # inicializa-se a plicação na variavel app
primeira_tela = uic.loadUi("Jan_1.ui")
segunda_tela = uic.loadUi("Jan_2.ui")

primeira_tela.pushButton.clicked.connect(chama_segunda_tela) #Conecta o pushbutton 1 ao metodo listar_dados

primeira_tela.show()
app.exec()