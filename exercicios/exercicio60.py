#crie uma lista vazia,que sera usada para receber 10 numeros,apresente o final o total de números negativos e positivos
list=[]
neg=0
pos=0
for x in range(11): #Lê 10 números.
    list.append(int(input("Digite um número: ")))
for x in list: #2 contadores de positivo e negativo.
    if x>0:
        pos=pos+1
    elif x<0:
        neg=neg+1
for x in list: #Imprime os resultados.
    print(x)
print("Total de Números Negativos: {:d}\nTotal de Números Positivos: {:d}".format(neg,pos))