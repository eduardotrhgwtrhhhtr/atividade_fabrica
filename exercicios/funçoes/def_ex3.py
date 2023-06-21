import os
def somaimposto(custo,imposto):
    finalcusto=custo+(custo*imposto)/100
    return finalcusto
while True:
    try:
        a=float(input("digite o custo do produto: "))
        b=float(input("digite a porcentagem do imposto: "))
    except ValueError:
        os.system("cls")
        print("digite somente numeros...")
        os.system("pause")
        os.system("cls")
    else:
        os.system("cls")
        break
valor=somaimposto(a,b)
print("o custo final será: R$ {:.2f}.".format(valor))
#imprime um produto com uma taxa de imposto informada.
