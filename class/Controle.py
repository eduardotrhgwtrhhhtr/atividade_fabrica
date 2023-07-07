class controle():
    def __init__(self,buttons):
        self.buttons=buttons
        if buttons==1:
            print("voce mutou.")
        elif buttons==2:
            print("voce desligou.")
        elif buttons==3:
            print("voce aumentou o volume.")
        elif buttons==4:
            print("voce diminiu o volume.")
        elif buttons==0:
            print("voce saiu.")
    def netflix(self):
        if self.buttons==5:
            print("voce entrou na netflix.")