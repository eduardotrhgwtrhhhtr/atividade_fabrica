class conta():
    def __init__(self,nome,saldo,cpf,senha):
        self.nome=nome
        self.__saldo=saldo
        self.__cpf=cpf
        self.__senha=senha

    def extrato(self,senha):
        if senha== self.__senha:
            print(f"Ola {self.nome} seu saldo é de: {self.__saldo}")
        else:
            print("senha incorreta.")

    def depositar(self,valor):
        self.__saldo+=valor
        print(f"{self.nome}o seu novo saldo é de: {self.__saldo}")

    def sacar(self,saque,senha):
        if senha==self.__senha:
            self.__saldo -= saque
            print(f"{self.nome} o valor que voce deseja sacar: {saque} o novo saldo é de: {self.__saldo}")