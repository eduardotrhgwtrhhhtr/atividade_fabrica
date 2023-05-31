#numa eleiçao existem 3 candidatos.faça um programa que peça o numero total de eleitores.peça para cada eleitor votar e ao finalmostrar o numero de votos de cada candidato.
num=int(input("quantos candidatos tem? "))
chris=0
graveto=0
pontes=0
total=[]
for nume in range(num):
    print("\n""1- chris \n 2- graveto \n 3- pontes")
    numero=int(input("qual candidato deseja votar: "))
    if numero == 1:
        chris = chris +1
        total.append(chris)
    if numero == 2:
        graveto = graveto +1
        total.append(graveto)
    if numero == 3:
        pontes = pontes +1
        total.append(pontes)
print("eleitor chris: ",chris)
print("eleitor graveto: ",graveto)
print("eleitor pontes: ",pontes)
