import mysql.connector
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

class MyApp(App):
    def build(self):
        layout = GridLayout(cols=2)

        self.mydb = mysql.connector.connect(
            host="10.28.1.207",
            user="suporte",
            password="suporte",
            database="projeto"
        )

        self.mycursor = self.mydb.cursor()

        self.id_input = TextInput(multiline=False)
        self.name_input = TextInput(multiline=False)
        self.age_input = TextInput(multiline=False)
        self.email_input = TextInput(multiline=False)

        submit_button = Button(text="Adicionar", on_press=self.create_data)
        read_button = Button(text="Ler", on_press=self.read_data)
        update_button = Button(text="Atualizar", on_press=self.update_data)
        delete_button = Button(text="Excluir", on_press=self.delete_data)

        layout.add_widget(Label(text="Id"))
        layout.add_widget(self.id_input)
        layout.add_widget(Label(text="Nome"))
        layout.add_widget(self.name_input)
        layout.add_widget(Label(text="Email"))
        layout.add_widget(self.email_input)
        layout.add_widget(Label(text="Idade"))
        layout.add_widget(self.age_input)
        layout.add_widget(submit_button)
        layout.add_widget(update_button)
        layout.add_widget(delete_button)
        layout.add_widget(read_button)

        return layout

    def create_data(self, instance):
        name = self.name_input.text
        age = int(self.age_input.text)
        email = self.email_input.text

        sql = "INSERT INTO customers (name, age, email) VALUES (%s, %s, %s)"
        val = (name, age, email)
        self.mycursor.execute(sql, val)
        self.mydb.commit()
        print(self.mycursor.rowcount, "registro(s) inserido(s).")

    def read_data(self, instance):
        self.mycursor.execute("SELECT * FROM customers")
        myresult = self.mycursor.fetchall()
        content = GridLayout(cols=1)
        popup = Popup(title='Dados', content=content, size_hint=(None, None), size=(400, 3286))

        for x in myresult:
            content.add_widget(Label(text=str(x)))

        content.add_widget(Button(text="Fechar", on_press=popup.dismiss))

        popup.open()

    def update_data(self, instance):
        id = int(self.id_input.text)
        name = self.name_input.text
        age = int(self.age_input.text)
        email = self.email_input.text

        sql = "UPDATE customers SET name = %s, age = %s, email = %s WHERE id = %s"
        val = (name, age, email, id)
        self.mycursor.execute(sql, val)
        self.mydb.commit()
        print(self.mycursor.rowcount, "registro(s) atualizado(s).")

    def delete_data(self, instance):
        id = int(self.id_input.text)

        sql = "DELETE FROM customers WHERE id = %s"
        val = (id,)
        self.mycursor.execute(sql, val)
        self.mydb.commit()
        print(self.mycursor.rowcount, "registro(s) excluído(s).")

if __name__ == '__main__':
    MyApp().run()