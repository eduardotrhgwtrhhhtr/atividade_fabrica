class Vendedor():
    def __init__(self,nome,vendas):
#atributos/caracteristicas.
        self.nome = nome
        self.vendas = vendas
#sel.nome recebera dados da funçao __init__ do atributo nome.
#sempre que tivermos o self, significa que são caracteristicas da classe.
#caso nao seja definido o self, a variavel ficara apenas dentro da função.
vendedor1=Vendedor('Ederson',1000)
print(vendedor1.nome)