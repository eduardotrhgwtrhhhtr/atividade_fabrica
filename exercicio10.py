nome = input("Qual o nome do seu produto? ")
quantidade = int(input("Qual a quantidade que deseja comprar? "))
valor = float(input("Qual o valor do produto? "))
porc = float(input("Qual o valor do desconto? (em %) "))
valor1 = (valor*quantidade)
total = valor1-valor1 * (porc/100)

print ("Olá Sr(a). O produto %s de valor %.2f com a quantidade de %d e com desconto de %.2f custa no total: %s" % (nome,valor,quantidade,porc,total))