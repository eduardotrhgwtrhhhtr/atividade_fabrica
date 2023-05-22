listanome=[]
listasobrenome=[]
listaendereco=[]
listabairro=[]
listacidade=[]
listaestado=[]
listapais=[]
listafone=[]
listacpf=[]
listapeso=[]
listaaltura=[]
listaidade=[]
listancartao=[]
listaemail=[]
listaemail=[]
listacep=[]
listamedia=[]
listaserie=[]
listasexo=[]
listaclasse=[]
listasexo=[]
listacor=[]
while True:
    nome=input("digite seu nome: ")
    listanome.append(nome)
    sobrenome=input("digite seu sobrenome: ")
    listasobrenome.append(sobrenome)
    endereço=input("digite sua rua e numero de sua casa: ")
    listaendereco.append(endereço)
    bairro=input("digite seu bairro: ")
    listabairro.append(bairro)
    cidade=input("digite sua cidade: ")
    listacidade.append(cidade)
    estado=input("qual seu estado: ")
    listaestado.append(estado)
    pais=input("qual pais voce mora: ")
    listapais.append(pais)
    fone=input("qual seu numero: ")
    listafone.append(fone)
    cpf=input("qual seu cpf: ")
    listacpf.append(cpf)
    peso=float(input("qual seu peso: "))
    listapeso.append(peso)
    altura=float(input("qual sua altura: "))
    listaaltura.append(altura)
    idade=input("qual sua idade: ")
    listaidade.append(idade)
    ncartao=input("numero do cartao: ")
    listancartao.append(ncartao)
    email=input("qual seu email: ")
    listaemail.append(email)
    cep=input("qual seu cep: ")
    listacep.append(cep)
    nota1=float(input("primeira nota: "))
    nota2=float(input("segunda nota: "))
    nota3=float(input("terceira nota: "))
    nota4=float(input("quarta nota: ")) 
    media=(nota1+nota2+nota3+nota4)/4
    print(media)
    listamedia.append(media)
    serie=input("qual sua serie: ")
    listaserie.append(serie)
    classe=input("qual sua classe: ")
    listaclasse.append(classe)
    sexo=input("qual seu sexo: ")
    listasexo.append(sexo)
    cor=input("qual a cor da sua pele: ")
    listacor.append(cor)
    pare=input("voce deseja continuar S/N: ")
    if pare=="N":
        break
print(listanome)
print(listasobrenome)
print(listasobrenome)
print(listaendereco)
print(listabairro)
print(listacidade)
print(listaestado)
print(listapais)
print(listafone)
print(listacpf)
print(listapeso)
print(listaaltura)
print(listaidade)
print(listancartao)
print(listaemail)
print(listaemail)
print(listacep)
print(listamedia)
print(listaserie)
print(listasexo)
print(listaclasse)
print(listasexo)
print(listacor)
