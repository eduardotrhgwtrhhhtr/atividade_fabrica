from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class MenuScreen(Screen):
    def __init__(self, **kwargs):
        super(MenuScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation="vertical")
        
        button = Button(text="Ir para a outra tela")
        button.bind(on_press=self.change_screen)
        
        button2 = Button(text="Fechar o app")
        button2.bind(on_press=self.change_screen_close)
        
        layout.add_widget(button)
        layout.add_widget(button2)
        self.add_widget(layout)
    
    def change_screen(self, instance):
        self.manager.current = 'outra_tela'
    
    def change_screen_close(self, instance):
        App.get_running_app().stop()