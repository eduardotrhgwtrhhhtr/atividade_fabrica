from PySide6.QtWidgets import QApplication,QMainWindow,QPushButton,QLabel,QLineEdit
import sys
from PySide6.QtCore import QSize,Qt
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CADASTRO")
        self.setGeometry(100,100,300,150)
        self.label1 =QLabel("NOME: ",self)
        self.label1.setGeometry(10,10,80,30)
        self.input1 =QLineEdit(self)
        self.input1.setGeometry(100,10,80,30)
        
        self.label2 = QLabel("FONE: ",self)
        self.label2.setGeometry(10,50,80,30)
        self.input2 =QLineEdit(self)
        self.input2.setGeometry(100,50,80,30)
        
        self.label3 = QLabel("CPF: ",self)
        self.label3.setGeometry(10,90,80,30)
        self.input3 = QLineEdit(self)
        self.input3.setGeometry(100,90,80,30)
        
        self.label4 = QLabel("ENDEREÇO: ",self)
        self.label4.setGeometry(10,130,80,30)
        self.input4 = QLineEdit(self)
        self.input4.setGeometry(100,130,80,30)
        
        
    
app = QApplication(sys.argv)
janela=MainWindow()
janela.show()
app.exec()