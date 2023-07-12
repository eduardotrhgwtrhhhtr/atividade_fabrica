class bola:
    def __init__(self,bolota):
        self.bolota=bolota
        if bolota==1:
            print("a circunferencia é de 68cm a 70cm.")
        elif bolota==2:
            print("a cor é amarelo.")
        elif bolota==3:
            print("o tecido é de pano e borracha")
        elif bolota==4:
            cor=input("qual a cor que voce deseja: ")
            print(cor)
        else:
            print("erro...")