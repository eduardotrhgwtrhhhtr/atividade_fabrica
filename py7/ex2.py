from PySide6.QtWidgets import QApplication,QMainWindow,QPushButton,QLabel
import sys
from PySide6.QtCore import QSize,Qt
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(" Ex02")
        self.button = QPushButton(" Botão ",self)
        self.button.setGeometry(190,10,100,70)
        self.result_label = QLabel(self)
        self.result_label.setGeometry(10,90,200,30)
        self.button.clicked.connect(self.imprimir)
        
    def imprimir(self):
        numero = 4
        if numero % 2 == 0:
            self.result_label.setText(f"Este número é {numero} par")
        else:
            self.result_label.setText(f"Este nnúmero é {numero} impar")
        

app = QApplication(sys.argv)
janela=MainWindow()
janela.show()
app.exec()
