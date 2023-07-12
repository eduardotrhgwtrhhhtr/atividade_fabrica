from quadrado import*
import os
lado=1
while lado != 0:
    if lado==0:
        break
    try:
        print("digite 0 para sair.")
        
        lado=float(input("digite o tamanho do lado do seu quadrado: "))
        result= quadrado(lado)
        result.mostrar()

        lado=float(input("digite o novo lado do quadrado: "))
        result.alterar(lado)
    except:
        print("valor invalido, digite somente numeros inteiros.")
os.system("cls")
os.system("pause")
os.system("cls")