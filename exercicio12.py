a="fofinho"
print(len(a))                 #conta quantas strings 
print(a.capitalize())         #deixa a primeira letra em maiusculo
print(a.upper())              #deixa toda a variavel em maiusculo
print(a.casefold())           #deixa toda a variavel em minusculo
print(a.islower())            #pergunta se esta em minusculo
print(a.isupper())            #pergunta se esta em maiusculo



#como verificar se uma string só possui números
a= "12345"
print(a.isdigit())
print(a)
b= "12345abc"
print(b.isdigit())
print(b)



# O replace serve para substituir uma string
a = "eduardo jheron"
print(a.replace("jheron","dos santos"))



# O split separa uma string com vírgula
a= "eduardo-jheron-dos-santos"
print(a.split("-"))


# find localiza qual o numero da string
a= "eduardo Jheron Dos Santos"
print(a.find("Santos"))

# O rfind localiza o numero da string da direita pra esquerda
a= "Eduardo Jheron Dos Santos"
print(a.rfind("Jheron"))

#verifica se tem uma string dentro da variavel, se tiver da correto, se não da falso
a= "Eduardo Jheron Dos Santos"
print("Santos"in a)


# conta quantas (a letra digitada) tem dentro da sua string
a= "Eduardo Jheron Dos Santos"
print(a.count("a"))


# diz os numeros das letras que voce por no print
s = "olá, mundo!"
print(s[0])
print(s[2])
print(s[1:3])







