from PySide6.QtWidgets import QApplication,QMainWindow,QPushButton,QLabel,QLineEdit
import sys
from PySide6.QtCore import QSize,Qt
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(" Ex04")
        self.setGeometry(100,100,300,150)
        self.label1 =QLabel("1* Nota",self)
        self.label1.setGeometry(10,10,80,30)
        self.input1 =QLineEdit(self)
        self.input1.setGeometry(100,10,80,30)
        
        self.label2 = QLabel("2* Nota ",self)
        self.label2.setGeometry(10,50,80,30)
        self.input2 =QLineEdit(self)
        self.input2.setGeometry(100,50,80,30)
        
        self.label3 = QLabel(" 3* Nota",self)
        self.label3.setGeometry(10,90,80,30)
        self.input3 = QLineEdit(self)
        self.input3.setGeometry(100,90,80,30)
        
        self.label4 = QLabel(" 4* Nota",self)
        self.label4.setGeometry(100,130,80,30)
        self.input4 = QLineEdit(self)
        self.input4.setGeometry(100,130,80,30)
        
        self.result_label = QLabel(self)
        self.result_label.setGeometry(10,180,280,30)
        self.button =QPushButton("Média",self)
        self.button.setGeometry(190,200,100,70)
        self.button.clicked.connect(self.media)
        
    def media(self):
        n1 = float(self.input1.text())
        n2 = float(self.input2.text())
        n3 = float(self.input3.text())
        n4 = float(self.input4.text())
        soma =(n1 + n2 + n3 + n4)/4
        self.result_label.setText(f"A média é {soma}")
app = QApplication(sys.argv)
janela=MainWindow()
janela.show()
app.exec()