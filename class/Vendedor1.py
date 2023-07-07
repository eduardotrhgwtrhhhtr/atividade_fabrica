class Vendedor():
    def __init__(self,nome,vendas):
        self.nome = nome
        self.vendas = vendas
    def vendeu(self,vendas):
        self.vendas=vendas
        self.vendas
        print(self.vendas)
    def bateu_meta(self,meta):
        if self.vendas>=meta:
            print("bateu a meta.")
        else:
            print("nao bateu a meta.")

