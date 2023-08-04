from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QFrame
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
import sys

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(800,600)
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("ratazanas")
        
        self.button_stuart = QPushButton('stuart')
        self.button_ratattoule = QPushButton('ratattoule')
        
        self.image_frame = QFrame(self)
        self.image_frame.setFrameShape(QFrame.Box)
        self.image_frame.setFixedSize(600,400)
        self.image_frame.setLayout(QVBoxLayout())
        
        self.image_label = QLabel(self.image_frame)
        self.image_label.setAlignment(Qt.AlignCenter)
        self.image_frame.layout().addWidget(self.image_label)
        
        layout = QVBoxLayout()
        layout.addWidget(self.button_stuart)
        layout.addWidget(self.button_ratattoule)
        layout.addWidget(self.image_frame)
        
        self.button_stuart.clicked.connect(self.display_stuart)
        self.button_ratattoule.clicked.connect(self.display_ratattoule)
        
        self.setLayout(layout)
    
    def display_stuart(self):
        pixmap = QPixmap('stuart.jpg')
        self.image(pixmap)
    
    def display_ratattoule(self):
        pixmap = QPixmap('ratattoule.jpg')
        self.image(pixmap)
        
    def image(self, pixmap):
        scale_pixmap = pixmap.scaled(600,400, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.image_label.setPixmap(scale_pixmap)
        
       
        
    

app = QApplication(sys.argv)
janela = MainWindow()
janela.show()
app.exec()