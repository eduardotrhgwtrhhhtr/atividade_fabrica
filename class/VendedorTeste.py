from Vendedor1 import *
vendedor1 = Vendedor("Ederson",1000)
print (vendedor1.nome)
##############################################################################

a = input("Nome: ")
b = int(input("Valor: "))

vendedor2 = Vendedor(a,b)
print (vendedor2.nome)
print (vendedor2.vendas)