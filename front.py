from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.image import Image
from kivy.core.window import Window


class Tela_Principal(MDBoxLayout):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 50
        self.spacing = 20

        img_Tela_principal = Image(source='imagem_tela_principal.jpg', size_hint=(1,3), texture_size='top')
        self.add_widget(img_Tela_principal)

        espaçamento = MDLabel(text=' ', font_style='H1')
        self.add_widget(espaçamento)

        lbl = MDLabel(text='SEJA BEM-VINDO', theme_text_color="Custom", text_color=('#F56C47'), font_style='H5', halign='center')
        self.add_widget(lbl)

        espaçamento_1 = MDLabel(text=' ', font_style='H1')
        self.add_widget(espaçamento_1)

        description = MDLabel(text='Este é o aplicativo de agendamento do Senac\nHub Academy, Aqui você pode se inscrever\npara ser modelo dos cursos de estética e\nbeleza.', halign='center')
        self.add_widget(description)
        
        espaçamento_2 = MDLabel(text=' ', font_style='H1')
        self.add_widget(espaçamento_2)

        btn_ver_serviços = MDRaisedButton(text='Ver Serviços',halign='center', font_size=20, on_release=self.on_button_press, md_bg_color="white", text_color='blue',size_hint=(1,0))
        self.add_widget(btn_ver_serviços)
        
        espaçamento_3 = MDLabel(text=' ', font_style='H1')
        self.add_widget(espaçamento_3)

        logos=Image(source='senac_hub.png', size_hint=(1,1.2))
        self.add_widget(logos)
        #F56C47
        #F37A59D4
        Window.size = (470, 932)

    def on_button_press(self, instance):
        pass

class MyApp(MDApp):
    def build(self):
        return Tela_Principal()

if __name__ == '__main__':
    MyApp().run()
