class quadrado: 
    def __init__(self,lado):
        self.lado=lado
        
    def mostrar(self):
        self.area=self.lado*self.lado
        print(self.area)

    def alterar(self,novoValor):
        self.lado=novoValor
        self.area=self.lado*self.lado
        print(self.area)