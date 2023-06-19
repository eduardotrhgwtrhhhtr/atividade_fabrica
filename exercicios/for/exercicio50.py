# FOR
nomes = ['gabriel','chris','gleisson']
for n in nomes:       #imprime cada um da lista (for)
    print(n)
alunos="felipe"
for a in alunos:       # se for um str ele imprime letra por letra
    print(a)
names=["graveto","vinicius","dieguin"]
for b in names:          #break é usado para parar onde eu quiser
    print(b)
    if b=="graveto":
        break
nomess=["graveto","vinicius","dieguin"]
for c in nomess:
    print(c)
    if c=="graveto":
        continue

#range é um contador que conta até onde eu mandar
for x in range(100,0,-1): #inicio/ fim /icremento
    print(x)
for i in range(5):
    for j in range(6):
        print(i,j)      