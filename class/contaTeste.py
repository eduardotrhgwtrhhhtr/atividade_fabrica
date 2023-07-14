from conta import*

cont=conta("Eduardo",1200,12345,"dudu")
cont.extrato("dudu")
cont.depositar(200)
cont.sacar(400,"dudu")
print (cont.nome)
# print (cont.__saldo)