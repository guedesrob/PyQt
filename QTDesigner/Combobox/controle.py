from PyQt5 import uic, QtWidgets
# modulo uic: permite-se trabalhar com arquivos .ui
# QtWidgets: permite usar os componentes (mostrar os componentes na tela)

def opcao_selecionada():
    print("teste")
    cidade=combo_box.comboBox.currentText()
    combo_box.label_2.setText("Cidade: "+cidade)

app = QtWidgets.QApplication([]) # inicializa-se a plicação na variavel app
combo_box = uic.loadUi("combobox.ui")
combo_box.comboBox.addItems(["São Paulo", "Rio de Janeiro","Fortaleza"])
combo_box.pushButton.clicked.connect(opcao_selecionada)

combo_box.show()
app.exec()