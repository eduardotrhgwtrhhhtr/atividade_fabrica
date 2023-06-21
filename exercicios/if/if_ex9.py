max=10
minnot=0

nota=float(input("primeira nota: "))
nota2=float(input("segunda nota: "))

result=(nota+nota2)/2


if result>=7 and result<=max:
    print("aprovado")
    if result==max:
        print("distinção")
elif result<7 and result>=minnot:
    print("reprovado")
else:
    print("Média inválida. ERRO.")