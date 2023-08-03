from PySide6.QtWidgets import QApplication,QMainWindow,QPushButton,QLabel,QLineEdit
import sys
from PySide6.QtCore import QSize,Qt
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(" ex06")
        self.setGeometry(100,100,300,150)
        self.label =QLabel("raio circ ",self)
        self.label.setGeometry(10,10,80,30)
        self.input =QLineEdit(self)
        
        self.input.setGeometry(100,10,80,30)
        self.result_label = QLabel(self)
        self.result_label.setGeometry(10,90,280,30)
        self.button =QPushButton("Calcular",self)
        self.button.setGeometry(190,10,100,70)
        self.button.clicked.connect(self.raio_circulo)
    def raio_circulo(self):
        n = int(self.input.text())
        r= 3.14 * (n**2)
        self.result_label.setText(f"{r}cm")
app = QApplication(sys.argv)
janela=MainWindow()
janela.show()
app.exec()
