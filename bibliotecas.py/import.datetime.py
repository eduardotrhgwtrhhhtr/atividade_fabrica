import datetime as dt
#mostrar a data
print(dt.date.today()) 
#formatando datas
print(dt.date.today().strftime("%d/%m/%y"))
#mostra as horas
print(dt.datetime.now())
#data e hora
import os
while True:
    print(dt.datetime.now().strftime("%d/%M/%Y/%H:%M"))
    os.system("cls")#limpa a tela
