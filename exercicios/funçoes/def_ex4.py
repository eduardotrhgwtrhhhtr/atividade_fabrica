import os
def convertionHoras(horas,minutos):
    if horas<=12 and horas>=0:
        print(horas,":",minutos,"AM")
    elif horas>12 and horas <=23:
        print(horas-12,":",minutos,"PM")
    else:
        print("VALOR INVALIDO...")
while True:
    try:
        horas=int(input("digite as horas: "))
        minutos=int(input("digite os minutos: "))
    except:
        print("VALOR INVALIDO...")
    else: 
        convertionHoras(horas,minutos)
        break
#convertendo horas AM e PM