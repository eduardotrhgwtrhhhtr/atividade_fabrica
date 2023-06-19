print("TABELA DE PREÇOS: ")
valor=1.99
for a in range(1,51):
    print("{:d}- R$ {:.2f}".format(a,valor))
    valor=valor+1.99

