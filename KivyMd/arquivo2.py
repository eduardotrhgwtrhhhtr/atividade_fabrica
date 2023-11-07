from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
import random


class OutraTela(Screen):
    def __init__(self, **kwargs):
        super(OutraTela, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        
        self.lbl = Label(text="Digite um numero primeiro (1 a 100)")
        self.result = TextInput()
        self.number = random.randint(1,100)
    
        button_guess = Button(text= "Adivinhar Number")
        button_restart = Button(text = "Restart Game")        
        button_exit = Button(text = "Exit Screen")
        button_guess.bind(on_press = self.adivinha_number)
        button_restart.bind(on_press=self.number_restart)
        button_exit.bind(on_press=self.change_screen)
        
        layout.add_widget(self.lbl)
        layout.add_widget(self.result)
        layout.add_widget(button_restart)
        layout.add_widget(button_guess)
        layout.add_widget(button_exit)
        
        self.add_widget(layout)
        print(self.number)
        
    def change_screen(self, instace):
        self.manager.current = 'menu'
        
    def number_restart(self, intance):
        self.number =random.randint(1,100)
        print(self.number)
    
        
    def adivinha_number(self, instace):
        try:
                
            if int( self.result.text) > self.number:
                self.lbl.text = "Numero e menor"
            if int( self.result.text) < self.number:
                self.lbl.text = "Numero e maior"
            if int( self.result.text) == self.number:
                self.lbl.text = "Parabens vc acertou"
        except:
            self.lbl.text = "Valor invalido!"   