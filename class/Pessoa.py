class Pessoa:
    def __init__(self,nome,idade,endereco,cidade,estado):
        self.nome=nome
        self.idade=idade
        self.endereco=endereco
        self.cidade=cidade
        self.estado=estado

    def relatorio(self):
        print("nome...",self.nome)
        print("idade...",self.idade)
        print("endereço...",self.endereco)
        print("cidade...",self.cidade)
        print("estado...",self.estado)

class Aluno(Pessoa):
    def __init__(self,mensalidade,idade,endereco,cidade,estado):
        super().__init__(idade,endereco,cidade,estado)
        self.mensalidade=mensalidade
        print("------------------------")
        print("seja bem vindo aluno")
        super().relatorio()
        print("mensalidade: ", self.mensalidade)
        print("------------------------")
        
class professor(Pessoa):
    def __init__(self,salario,idade,endereco,cidade,estado):
        super().__init__(idade,endereco,cidade,estado)
        self.salario=salario
        print("------------------------")
        print("seja bem vindo professor")
        super().relatorio()
        print("salario...",self.salario)
        print("_-----------------------")
