'''numero = int(input("Digite o numero para calcular o Fatorial: ") )
resultado=1
count=1
while count <= numero:
    resultado *= count
    count += 1
print(resultado)'''

#FATORAÇAO

def soma(n):
    if n == 1:
        return 1
    else:
        return n * soma (n - 1)

numero = 5
result = soma(numero)
print(f"o fatorial do {numero} é {result}")