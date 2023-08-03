from PySide6.QtWidgets import QApplication,QMainWindow,QLabel
import sys
from PySide6.QtCore import QSize,Qt
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(" Ex01")
        self.setFixedSize(600,400)
        self.lbl = QLabel("Hello WORLD")
        font= self.lbl.font()
        font.setPointSize(35)
        self.lbl.setFont(font)
        self.lbl.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        
        self.setCentralWidget(self.lbl)
app = QApplication(sys.argv)
janela=MainWindow()
janela.show()
app.exec()

