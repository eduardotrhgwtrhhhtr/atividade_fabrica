from Controle import *
import os
escolha = 1
while escolha != 0:
    try:
        print("0-sair")
        print("1-muto")
        print("2-desligar")
        print("3-aumentar volume")
        print("4-diminuir o volume")
        escolha=int(input("digite: "))
        escolha2= controle(escolha)
    except:
        print("valor invalido, digite somente numeros inteiros.")
    os.system("pause")
    os.system("cls")