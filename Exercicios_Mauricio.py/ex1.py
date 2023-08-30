import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget

class BankAccount:
    def __init__(self, account_number, account_holder, initial_deposit=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = initial_deposit

class AccountCreationWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Account Creation")
        self.setGeometry(100, 100, 300, 200)

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.number_label = QLabel("Account Number:")
        self.number_input = QLineEdit()
        layout.addWidget(self.number_label)
        layout.addWidget(self.number_input)

        self.name_label = QLabel("Account Holder Name:")
        self.name_input = QLineEdit()
        layout.addWidget(self.name_label)
        layout.addWidget(self.name_input)

        self.deposit_label = QLabel("Initial Deposit:")
        self.deposit_input = QLineEdit()
        layout.addWidget(self.deposit_label)
        layout.addWidget(self.deposit_input)

        self.create_button = QPushButton("Create Account")
        self.create_button.clicked.connect(self.create_account)
        layout.addWidget(self.create_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def create_account(self):
        account_number = self.number_input.text()
        account_holder = self.name_input.text()
        initial_deposit = float(self.deposit_input.text()) if self.deposit_input.text() else 0.0

        account = BankAccount(account_number, account_holder, initial_deposit)
        print("Account created:")
        print("Account Number:", account.account_number)
        print("Account Holder:", account.account_holder)
        print("Initial Balance:", account.balance)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AccountCreationWindow()
    window.show()
    sys.exit(app.exec())
