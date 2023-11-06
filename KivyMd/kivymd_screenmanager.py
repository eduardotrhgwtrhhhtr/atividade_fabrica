from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField

class GameLogic(BoxLayout):
    label = ObjectProperty()
    input = ObjectProperty()

    def __init__(self, **kwargs):
        super(GameLogic, self).__init__(**kwargs)
        self.secret_number = 42  # Número a ser adivinhado
        self.attempts = 0

    def verify_number(self):
        user_guess = int(self.input.text)
        self.attempts += 1

        if user_guess < self.secret_number:
            self.label.text = f"Tente um número MAIOR! Tentativas: {self.attempts}"
        elif user_guess > self.secret_number:
            self.label.text = f"Tente um número MENOR! Tentativas: {self.attempts}"
        else:
            self.label.text = f"Parabéns! Você adivinhou o número em {self.attempts} tentativas!"
            self.input.text = ""

if __name__ == "__main__":
    from kivy.app import App
    app = App()
    game = GameLogic()
    app.run()
