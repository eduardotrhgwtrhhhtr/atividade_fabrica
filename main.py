import shutil
import sys
import os
from PySide6.QtWidgets import *
from PySide6.QtGui import QIcon
from projeto import Ui_MainWindow





class MainWindow(QMainWindow, Ui_MainWindow):
    def init(self):
        super().init()
        self.setupUi(self)
        self.setWindowTitle("organizador de arquivo")
        appIcon = QIcon("folder.png")
        self.setWindowIcon(appIcon)
        self.ok.clicked.connect(self.open_path)
        self.organizar.clicked.connect(self.open_path)
        
    def open_path(self):
        self.path = QFileDialog.getExistingDirectory(self, str('pasta com arquivos'), '/home', QFileDialog.ShowDirsOnly | 
        QFileDialog.DontResolveSymlinks)
        self.txt_path.setText(self.path)
        self.path = str(self.path) 
        
        
        

app = QApplication(sys.argv)

window = MainWindow()
window.show()

sys.exit(app.exec())
