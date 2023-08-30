import sys
import datetime
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QPushButton, QLineEdit, QTextBrowser

class Patient:
    def __init__(self, name, phone, email, gender, birthdate, is_pcd):
        self.name = name
        self.phone = phone
        self.email = email
        self.gender = gender
        self.birthdate = birthdate
        self.is_pcd = is_pcd
        self.arrival_time = datetime.datetime.now()
        
class ClinicQueue:
    def __init__(self):
        self.queue = []
        
    def add_patient(self, patient):
        self.queue.append(patient)
        self.sort_queue()
        
    def sort_queue(self):
        self.queue.sort(key=lambda p: (p.is_pcd, p.birthdate > datetime.date(1960, 1, 1), p.arrival_time))
        
    def get_next_patient(self):
        if self.queue:
            return self.queue[0]
        return None
        
class ClinicApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Gerenciamento de Fila - Consultório Médico')
        self.setGeometry(100, 100, 600, 400)
        
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        
        self.layout = QVBoxLayout()
        
        self.queue_label = QLabel('Fila de Espera:')
        self.layout.addWidget(self.queue_label)
        
        self.queue_display = QTextBrowser()
        self.layout.addWidget(self.queue_display)
        
        self.add_patient_button = QPushButton('Adicionar Paciente')
        self.add_patient_button.clicked.connect(self.add_patient)
        self.layout.addWidget(self.add_patient_button)
        
        self.clinic_queue = ClinicQueue()
        
        self.central_widget.setLayout(self.layout)
        
        self.update_queue_display()
        
    def update_queue_display(self):
        self.queue_display.clear()
        for i, patient in enumerate(self.clinic_queue.queue):
            self.queue_display.append(f'{i+1}. {patient.name} ({patient.gender}), PCD: {patient.is_pcd}, Chegada: {patient.arrival_time}')
        
    def add_patient(self):
        name = input('Nome: ')
        phone = input('Telefone: ')
        email = input('Email: ')
        gender = input('Gênero: ')
        birthdate = input('Data de Nascimento (AAAA-MM-DD): ')
        is_pcd = input('Paciente PCD? (s/n): ').lower() == 's'
        
        patient = Patient(name, phone, email, gender, datetime.datetime.strptime(birthdate, '%Y-%m-%d').date(), is_pcd)
        self.clinic_queue.add_patient(patient)
        
        self.update_queue_display()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    clinic_app = ClinicApp()
    clinic_app.show()
    sys.exit(app.exec_())
