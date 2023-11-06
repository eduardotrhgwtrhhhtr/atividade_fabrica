from kivy.lang import Builder
from kivymd.app import MDApp
from game_logic import GameLogic

Builder.load_file("game.kv")

class GuessNumberApp(MDApp):
    def build(self):
        return GameLogic()

if __name__ == "__main__":
    GuessNumberApp().run()
