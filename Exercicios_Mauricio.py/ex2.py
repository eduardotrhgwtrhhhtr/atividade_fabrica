import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget

class Employee:
    def __init__(self, name, hours_worked, hourly_rate):
        self.name = name
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

class OutsourcedEmployee(Employee):
    def __init__(self, name, hours_worked, hourly_rate, additional_expense):
        super().__init__(name, hours_worked, hourly_rate)
        self.additional_expense = additional_expense

def calculate_payment(employee):
    if isinstance(employee, OutsourcedEmployee):
        return (employee.hourly_rate * employee.hours_worked) + (1.10 * employee.additional_expense)
    else:
        return employee.hourly_rate * employee.hours_worked

class PayrollApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Payroll App")
        self.setGeometry(100, 100, 400, 300)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        self.label = QLabel("Enter number of employees:")
        self.layout.addWidget(self.label)

        self.input_field = QLineEdit()
        self.layout.addWidget(self.input_field)

        self.button = QPushButton("Submit")
        self.button.clicked.connect(self.process_employees)
        self.layout.addWidget(self.button)

        self.result_label = QLabel("")
        self.layout.addWidget(self.result_label)

        self.central_widget.setLayout(self.layout)

    def process_employees(self):
        try:
            num_employees = int(self.input_field.text())
            employees = []

            for _ in range(num_employees):
                employee_type = input("Employee type (1 for regular, 2 for outsourced): ")
                name = input("Name: ")
                hours_worked = float(input("Hours worked: "))
                hourly_rate = float(input("Hourly rate: "))
                
                if employee_type == '2':
                    additional_expense = float(input("Additional expense: "))
                    employee = OutsourcedEmployee(name, hours_worked, hourly_rate, additional_expense)
                else:
                    employee = Employee(name, hours_worked, hourly_rate)
                
                employees.append(employee)
            
            payment_details = []
            for employee in employees:
                payment = calculate_payment(employee)
                payment_details.append(f"Name: {employee.name}, Payment: ${payment:.2f}")

            self.result_label.setText("\n".join(payment_details))

        except ValueError:
            self.result_label.setText("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PayrollApp()
    window.show()
    sys.exit(app.exec_())
