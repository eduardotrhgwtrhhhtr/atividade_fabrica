a=(input("digite um produto: "))
b=(input("digite outro produto: "))
c=(input("digite outro produto: "))



a1=float(input("valor do primeiro produto: "))
b2=float(input("valor do segundo produto: "))
c3=float(input("valor do terceiro produto: "))

barato=[a1,b2,c3]
bestbar=min(barato)


if bestbar==a1:
    print(a,a1)
elif bestbar==b2:
    print(b,b2)
elif bestbar==c3:
    print(c,c3)
else:
    print("ERRO. Existem numeros iguais!")
