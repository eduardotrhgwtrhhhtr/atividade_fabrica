#faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de numeros pares e a quantidade de impares.
par=[]#lista de pares
impar=[]#lista de impares
for a in range(10):
    n=int(input("digite 10 números inteiros: "))
    if n%2==0: #se numero for dividido por 2 igual a 0
        par.append(n) #jogo o numero para a lista par
    elif n%2!=0: #se numero divido por 2 for diferente de 0
        impar.append(n) #jogo o numero para a lista de impares
    else:
        print("oque voce digitou nao foi um numero!") 
print("numeros pares: ",par)
print("numeros impares: ",impar)