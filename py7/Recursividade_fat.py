'''numero = int(input("Digite o numero para calcular o Fatorial: ") )
resultado=1
count=1
while count <= numero:
    resultado *= count
    count += 1
print(resultado)

#FATORAÇAO

def soma(n):
    if n == 1:
        return 1
    else:
        return n * soma (n - 1)

numero = 5
result = soma(numero)
print(f"o fatorial do {numero} é {result}")'''

#torre de hanoi

def TorreDeHanoi(n, origem, destino, auxiliar):
    if n == 1:
        print(f"move o disco 1 de {origem} a {destino}")
        return 1
    
    movimentos = 0
    movimentos += TorreDeHanoi(n - 1, origem, auxiliar, destino )
    print(f"move o disco {n} de {origem} a {destino}")
    movimentos += 1
    movimentos += TorreDeHanoi(n-1, auxiliar, destino,  origem)
    return movimentos 

num=3
resultMovim=TorreDeHanoi(num,'A','C','B')
print(f'total de movmentos necessarios: {resultMovim}')