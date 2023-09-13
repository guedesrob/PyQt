from PyQt5 import uic, QtWidgets

def pegar_data():
    data=primeira_tela.calendarWidget.selectedDate() #capatura a data selecionada pelo usuario
    data=str(data) #converte a data para formato string
    data_formatada=data[19:30] #retorna o texto entre as strings 19 a 30
    primeira_tela.label.setText("Data selecionada: " + data_formatada)

app=QtWidgets.QApplication([])
primeira_tela=uic.loadUi("cal.ui")
primeira_tela.calendarWidget.selectionChanged.connect(pegar_data)
primeira_tela.show()


app.exec()