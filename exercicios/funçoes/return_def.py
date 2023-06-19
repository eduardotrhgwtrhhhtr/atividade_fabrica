'''def soma(x,y):
    result=x+y
    return result
a=int(input("Primeiro numero:"))
b=int(input("Segundo numero:"))
vres=soma(a,b)
print("Soma:",res)'''

def inverte(nome,sobrenome):
    nomeinverso=sobrenome+","+nome
    return nomeinverso
nome=input("nome: ")
sobrenome=input("sobrenome: ")
invertido=inverte(nome,sobrenome)
print("EAEEEEEEE",invertido)

 # PAR OU IMPAR COM DEF
'''def par(x):
    if (x%2)==0:
        return True
    else:
        return False
while True:
    num=int(input("insira um numero: "))
    if par(num):
        print("é par")
    else: 
        print("é impar")'''

def cadastro():
    nome=input("qual seu nome: ")
    idade=int(input("idade: "))
    return nome,idade
print("iniciando cadastro...")
name,age=cadastro()
print("cadastro realizado com sucesso.")
print("seu nome é",name,"e você tem",age,"anos de idade")

