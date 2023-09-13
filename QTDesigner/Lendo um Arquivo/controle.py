from PyQt5 import uic, QtWidgets

def save():
    nome = tela.lineEdit.text()
    idade = tela.lineEdit_2.text()
    telefone = tela.lineEdit_3.text()
    dados="Nome: "+nome+" Idade: "+idade+" Telefone: "+telefone
    arquivo=QtWidgets.QFileDialog.getSaveFileName()[0] # Retorna janela classica de inserir o caminho p salvar o arquivo
    with open (arquivo + ".txt",'w') as a:
        a.write(dados)

def ler_arquivo():
    arquivo=QtWidgets.QFileDialog.getOpenFileName()[0] # Retorna janela classica de inserir o caminho p salvar o arquivo
    with open (arquivo,'r') as a:
        texto=a.read()
    tela.label_5.setText(texto)

app = QtWidgets.QApplication([]) # inicializa-se a plicação na variavel app
tela = uic.loadUi("Jan_Abrir.ui") #Importa-se o arquivo "lista.ui" para a variavel lista, através do método loadUI
tela.actionSalvar.triggered.connect(save)
tela.actionAbrir.triggered.connect(ler_arquivo)

tela.show()
app.exec()