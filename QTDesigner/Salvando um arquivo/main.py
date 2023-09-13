from PyQt5 import uic, QtWidgets

def save():
    nome = tela.lineEdit.text()
    idade = tela.lineEdit_2.text()
    telefone = tela.lineEdit_3.text()
    dados="Nome: "+nome+" Idade: "+idade+" Telefone: "+telefone
    arquivo=QtWidgets.QFileDialog.getSaveFileName()[0] # Retorna janela classica de inserir o caminho p salvar o arquivo
    with open (arquivo + ".txt",'w') as a:
        a.write(dados)

app = QtWidgets.QApplication([]) # inicializa-se a plicação na variavel app
tela = uic.loadUi("Jan_Save.ui") #Importa-se o arquivo "lista.ui" para a variavel lista, através do método loadUI
tela.actionSalvar.triggered.connect(save)

tela.show()
app.exec()