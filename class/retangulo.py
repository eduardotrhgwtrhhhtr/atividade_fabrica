class retangulo:
    def __init__(self,lado1,lado2):
        self.lado1=lado1
        self.lado2=lado2
    
    def mostrar(self):
        self.area=self.lado1*self.lado2
        print(self.area)

    def perimetro(self):
        self.perimetr=self.lado1+self.lado1+self.lado2+self.lado2
        print(self.perimetr)

    def alterar(self,novoValor1, novoValor2):
        self.lado1=novoValor1
        self.lado2=novoValor2
        self.area=self.lado1*self.lado2
        print(self.area) 

    def perimetro2(self):
        self.perimet=self.lado1+self.lado1+self.lado2+self.lado2
        print(self.perimet)

    def rodape(self):
        self.rodape=self.area*15/100
        print(self.rodape)