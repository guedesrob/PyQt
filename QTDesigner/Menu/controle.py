from PyQt5 import uic, QtWidgets

def menu_verde():
    print("O botão Verde foi pressionado")
    tela.label.setText("Verde")
    tela.label.setStyleSheet("color: green")

def menu_azul():
    print("O botão Azul foi pressionado")
    tela.label.setText("Azul")
    tela.label.setStyleSheet("color: blue")

def menu_amarelo():
    print("O botão Amarelo foi pressionado")
    tela.label.setText("Amarelo")
    tela.label.setStyleSheet("color: yellow")

app=QtWidgets.QApplication([]) # Cria o objeto aplicação
tela=uic.loadUi("menu.ui") # Cria o objeto tela a partir da importação dos objetos criados no QTDesigner

tela.actionVerde.triggered.connect(menu_verde)
tela.actionAzul.triggered.connect(menu_azul)
tela.actionAmarelo.triggered.connect(menu_amarelo)
tela.show() # mostra o objeto tela
app.exec() # executa a aplicação