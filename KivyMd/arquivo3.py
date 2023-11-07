from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from arquivo1 import MenuScreen
from arquivo2 import OutraTela


class MyApp(App):
    def build(self):
        screen_manager = ScreenManager()
        screen_manager.add_widget(MenuScreen(name='menu'))
        screen_manager.add_widget(OutraTela(name='outra_tela'))
        return screen_manager

if __name__ == '__main__':
    MyApp().run()
