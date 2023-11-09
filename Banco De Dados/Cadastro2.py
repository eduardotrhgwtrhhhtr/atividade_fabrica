import mysql.connector 
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.app import App

class MyApp(App):
    def build(self):
        layout = GridLayout(cols=2)
        self.con = mysql.connector.connect(host='10.28.1.207', database='cadastro', user='suporte', password='suporte')

        self.mycursor = self.con.cursor()
        
        self.id_input = TextInput(multiline=False)
        self.name_input = TextInput(multiline=False)
        self.age_input = TextInput(multiline=False)
        self.email_input = TextInput(multiline=False)
        
        button1 = Button(text = "adicionar", on_press = self.adicionar_data)
        button2 = Button(text = "ler", on_press = self.ler_data)
        button3 = Button(text = "atualizar", on_press = self.atualizar_data)
        button4 = Button(text = "deletar", on_press = self.deletar_data)
        
        
        layout.add_widget(Label(text="id: ")) 
        layout.add_widget(self.id_input) 
        layout.add_widget(Label(text="Nome: ")) 
        layout.add_widget(self.name_input) 
        layout.add_widget(Label(text="Idade: ")) 
        layout.add_widget(self.age_input) 
        layout.add_widget(Label(text="Email: ")) 
        layout.add_widget(self.email_input)            
        layout.add_widget(submit_button)
        layout.add_widget() 
        layout.add_widget(atualizar_button) 
        layout.add_widget()  
        
        
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
        
    def atualizar_data(self, instance):
        id = int (self.id_input.text)
        name = self.name_input.text
        age = int(self.age_input.text)
        email = self.email_input.text
        
        
    def deletar_data(self,instance):
        id = int(self.id_input.text)
        
        sql = 
        
        
        
        

'''if con.is_connected():
    db_info = con.get_server_info()
    print("Conectado ao banco de dados=",db_info)


consulta_sql = "select * from usuario"
cursor = con.cursor()
cursor.execute(consulta_sql)
linhas = cursor.fetchall()
print("Número total de registros retornados: ", cursor.rowcount)   




print("\nMostrando os Registros\n")
for linha in linhas:
    print("Nome = ", linha[1])
    print("idade = ", linha[2])   
    print("Email = ", linha[3])
    print("cpf = ", linha[4])


if __name__ == '__main__':
    OutraTela().run()
'''