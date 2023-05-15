nota=float(input("primeira nota: "))
nota2=float(input("segunda nota: "))

result = (nota + nota2)/2

if result >=7 and result <= 10:
    print("aprovado!")
elif result >=6.99 and result <=10:
    print("recuperação!")
else:
    print("reprovado!")