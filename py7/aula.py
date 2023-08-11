import brazilcep
import sys
from PySide6.QtWidgets import QMainWindow, QApplication

class MainWindow(QMainWindow):
    def __initp__(self):
        super().__init__()
        self .setWindowTitle("busca cep")
    
endereco = brazilcep.get_address_from_cep('7900101')
print(endereco)

#criei uma instancia de aplicaçao
app = QApplication(sys.argv)
#cria uma instancia da janela personalizada
window = MainWindow()
#exibir a janela
window.show()
#inicia o loop de eventos da aplicaçao
sys.exit(app.exec_())