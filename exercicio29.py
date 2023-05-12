'''#vetor - lista

a = [10,20,30,40]
print(a)
print(type(a))
b = {"python",3.5,True,1}
print(b)
print(type(b))


#len

a2= [10,20,30,40]
print(a2)
print(type(a2))
b2= {"python",3.5,True,1}
print(b2)
print(type(b2))

#lista dentro de lista

lista= [3,67,"gato",[56,57,"cachorro"],[],3.14,False]
print(lista[3][2][0])

animais=["gato","cachorro"]
print("gato" in animais)
print("cachorro" not in animais)

lista=[1,3,5]
lista2=[2,4,6]
print(lista+lista2)

a=[1,2,3,4,5,6,7,8,9]
print(a)
print(max(a)) #o maximo
print(min(a)) #o menor
print(sum(a)) # a soma

a=("python")
print(a[0:5])

#troca uma palavra dentro da sublista por outra
lista=["flor","azul",[1,"casa"]]
lista[2][1]="escola"
print(lista)

lista=['a','b','c','d','e','f']
lista[2:5] = ['g','h']
print(lista)
#remove oque eu quero
lista=['a','b','c','d','e','f']
print(lista)
print(len(lista))

lista[1:3] = []
print(lista)
print(len(lista))

#insiro oque eu quero
lista=['a','d','f']
lista[1:1]= ['b','c']
print(lista)
lista[4:4]=['e']
print(lista)

#del deleta oque eu quero
a=['um','dois','tres']
del a[1]
print(a)

#eu adiciono ao final da fila(append)
a=[81,82,83]
a.append(5)
print(a)

#sort ordena os numeros
a=[7,4,8,2,3,1]
a.sort()
print(a)

#reverse conta de tras pra frente
a=[3,5,7,8]
a.reverse()
print(a)

#index mostra qual o numero das letras
a=[1,2,3,4,5,6,7,8]
print(a.index(4))

#ele adiciona o numero pra onde eu quiser
a = [1,2,3,4]
a.insert(2,100)
print(a)

#fala quantos do numero digitado tem
a=[1,2,3,4,5,6,7,8,9]
print(a.count(4))

#o pop remove quem estiver dentro do parentese,se nao tiver nada remove o ultimo
a=[1,2,3,4]
a.pop()
print(a)'''

