diasEmAtraso= 0.01
contador = 1
def valorPagamento (valor,dias):
    totalDeDias = dias*diasEmAtraso
    
    totatly = float((totalDeDias+0.03)+valor)
    print ("O valor de dias por atraso é ", diasEmAtraso,"")
    return totalDeDias,totatly

while contador != 0:
    print("0. Sair/mostrar")
    print("1. Escolha para parcela e dias")
    contador = int(input("Escolha: "))
    if contador == 1:
        valor = float(input("Digite o valor da parcela: "))
        dias = int(input("Digite os dias: "))
        valorFInal = valorPagamento(valor,dias)
        print (valorFInal)