def hello():
    print("ola!!!!")

hello()
#
def hello(nome,idade):
    print("ola!",nome,)
    print("sua idade: ",idade)
a=input("nome: ")
b=input("idade: ")
hello(a,b)
#
def calcular_pagamento(qtd_horas,valor_hora):
    horas=float(qtd_horas)
    taxa=float(valor_hora)
    if horas <=40:
        salario=horas*taxa
    else:
        h_excd=horas-40
        salario=40*taxa+(h_excd*(1.5*taxa))
    print(salario)
calcular_pagamento (200,20)
#
