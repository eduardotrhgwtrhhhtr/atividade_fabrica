import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox

class TaxCalculatorApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculadora de Impostos")
        self.setGeometry(100, 100, 400, 300)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.name_label = QLabel("Nome:")
        self.income_label = QLabel("Renda Anual:")
        self.special_expense_label = QLabel("Gastos com Saúde:")

        self.name_input = QLineEdit()
        self.income_input = QLineEdit()
        self.special_expense_input = QLineEdit()

        self.calc_button = QPushButton("Calcular Imposto")
        self.calc_button.clicked.connect(self.calculate_tax)

        self.layout.addWidget(self.name_label)
        self.layout.addWidget(self.name_input)
        self.layout.addWidget(self.income_label)
        self.layout.addWidget(self.income_input)
        self.layout.addWidget(self.special_expense_label)
        self.layout.addWidget(self.special_expense_input)
        self.layout.addWidget(self.calc_button)

    def calculate_tax(self):
        name = self.name_input.text()
        income = float(self.income_input.text())
        special_expense = float(self.special_expense_input.text())

        if income < 20000:
            tax = income * 0.15
        else:
            tax
