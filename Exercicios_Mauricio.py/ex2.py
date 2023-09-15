import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget

class Funcionario:
    def __init__(self, nome, hora_trabalho, valor_hora):
        self.nome = nome
        self.hora_trabalho = hora_trabalho
        self.valor_hora = valor_hora

class FuncionarioTerceirizado(Funcionario):
    def __init__(self, nome, hora_trabalho, valor_hora, despesa_adicional):
        super().__init__(nome, hora_trabalho, valor_hora)
        self.despesa_adicional = despesa_adicional

def Calcular_pagamento(Funcionario):
    if isinstance(Funcionario, FuncionarioTerceirizado):
        return (Funcionario.valor_hora * Funcionario.hora_trabalho) + (1.10 * Funcionario.despesa_adicional)
    else:
        return (Funcionario.valor_hora * Funcionario.hora_trabalho)

class FolhaPagamento(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Folha de Pagamento")
        self.setGeometry(100, 100, 400, 300)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        self.funcionario_label = QLabel("Insira o número de funcionários:")
        self.layout.addWidget(self.funcionario_label)
        self.input_funcionario = QLineEdit()
        self.layout.addWidget(self.input_funcionario)

        self.button = QPushButton("Enviar")
        self.button.clicked.connect(self.FuncionariodoProcesso)
        self.layout.addWidget(self.button)

        self.result_label = QLabel("")
        self.layout.addWidget(self.result_label)

        self.central_widget.setLayout(self.layout)

    def FuncionariodoProcesso(self):
        try:
            num_funcionarios = int(self.input_funcionario.text())
            Funcionario = []

            for _ in range(num_funcionarios):
                tipo_funcionario = input("Tipo de Funcionário (1 para regular, 2 for terceirizado): ")
                nome = input("Nome: ")
                hora_trabalho = float(input("Horas Trabalhadas: "))
                valor_hora = float(input("Valor por hora: "))
                
                if tipo_funcionario == '2':
                    despesa_adicional = float(input("Despesas adicionais  "))
                    Funcionario = FuncionarioTerceirizado(nome, hora_trabalho, valor_hora, despesa_adicional)
                else:
                    Funcionario = Funcionario(nome, hora_trabalho, valor_hora )
                
                    funcionario.append(_)
            
            detalhes_pagamento = []
            for funcionario in _:
                pagamento = Calcular_pagamento(funcionario)
                detalhes_pagamento.append(f"Nome: {Funcionario.nome}, Pagamento: ${pagamento:.2f}")

            self.result_label.setText("\n".join(detalhes_pagamento))

        except ValueError:
            self.result_label.setText("Digito Inválido. Insira números válidos.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FolhaPagamento()
    window.show()
    sys.exit(app.exec_())

