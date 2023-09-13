from PyQt5 import uic, QtWidgets
# modulo uic: permite-se trabalhar com arquivos .ui
# QtWidgets: permite usar os componentes (mostrar os componentes na tela)
valor=0 # Esta é uma variável global

def incrementar_valor():
    global valor # dentro de funções variáveis globais devem ser declaradas
    valor=valor+10
    primeira_janela.progressBar.setValue(valor)
    if valor >= 100:
        valor=100

def zerar_valor():
    global valor
    valor=0
    primeira_janela.progressBar.setValue(valor)

app = QtWidgets.QApplication([]) # inicializa-se a plicação na variavel app
primeira_janela = uic.loadUi("PB.ui")
primeira_janela.pushButton.clicked.connect(incrementar_valor) #Conecta o pushbutton 1 ao metodo listar_dados
primeira_janela.pushButton_2.clicked.connect(zerar_valor) #Conecta o pushbutton 1 ao metodo listar_dados

primeira_janela.show()
app.exec()