print("TABELA DE PREÇOS: ")
valor=0.18
for a in range(1,51):
    print("{:d}- R$ {:.2f}".format(a,valor))
    valor=valor+0.18