import os
while True:
    try:
        print("1- CADASTRO CLIENTE")
        print("2- CADASTRO PASSAGEM")
        print("3- CADASTRO AVIAO")
        print("4- CADASTRO TRIPULAÇAO")
        print("5- INPRIMIR RELATORIO")
        print("0- SAIR")
        opcoes=int(input("QUAL SUA ESCOLHA? "))
    except ValueError:
        print("O VALOR DIGITADO NAO É UM NÚMERO!!!!!!!")
        print("TENTE NOVAMENTE...")
        os.system("pause")
        continue
    if opcoes==1:
        while True:          
            try: 
                nome=input("nome: ")
                sobrenome=(input("sobrenome: "))
                fone=input("fone: ")
                idade=(input("idade: "))
                rg=int(input("RG: "))
                cpf=int(input("cpf: "))
                os.system("pause")
                os.system("cls")
            except ValueError:
                print("tente novamente... digite somente numeros.")
            else:
                break
    if opcoes==2:
        while True:
            try:
                destino=(input("destino: "))
                origem=(input("origem: "))
                duraçao=float(input("duraçao: "))
                valorpass=float(input("valor da passagem: "))
                desconto=(5*valorpass)/100
                result=valorpass-desconto
                print(desconto)
                print(result)
                os.system("pause")
                os.system("cls")
            except ValueError:
                print("tente novamente... digite somente numeros.")
            else:
                break
    if opcoes==3:
        while True:           
            try:
                ano=int(input("ano: "))
                horasdevoo=float(input("horas de voo: "))
                cor=(input("cor: "))
                qntdp=int(input("quantidade de passageieros: "))
                modelo=(input("modelo: "))
                os.system("pause")
                os.system("cls")
            except ValueError:
                print("tente novamente... digite somente numeros.")
            else:
                break
    if opcoes==4:
        while True:
            try:
                nome2=input("nome da tripulaçao:")
                cargo=input("descriçao cargo: ")
                idade2=int(input("idade: "))
                datae=int(input("data de admissao: "))
                fone2=int(input("fone: "))
            except ValueError:
                print("tente novamente... digite somente numeros inteiros.")
            else:
                break

    if opcoes==5:
        print(nome)
        print(sobrenome)
        print(fone)
        print(idade)
        print(rg)
        print(cpf) 
        print("=================")
        print(destino)
        print(origem)
        print(duraçao)
        print(valorpass)
        print(desconto)
        print(result)
        print("=============")
        print(ano)
        print(horasdevoo)
        print(cor)
        print(qntdp)
        print(modelo)
        print("=============")
        print(nome2)
        print(cargo)
        print(idade2)
        print(datae)
        print(fone2)
    if opcoes==0:
        break
