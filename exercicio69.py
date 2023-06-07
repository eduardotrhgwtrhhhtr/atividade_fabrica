import os
while True:
    try:
        print("1- CADASTRO CLIENTE")
        print("2- CADASTRO PASSAGEM")
        print("3- CADASTRO AVIAO")
        print("4- CADASTRO TRIPULAÇAO")
        print("5- IMPRIMIR RELATORIO DO CLIENTE")
        print("6- IMPRIMIR RELATORIO DO CADASTRO PASSAGEM")
        print("7- IMPRIMIR RELATORIO DO CADASTRO DO AVIAO")
        print("8- IMPRIMIR RELATORIO DO CADASTRO DA TRIPULAÇAO")
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
                #listanome.append(nome)
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
        print("nome: ", nome)
        print("sobrenome: ", sobrenome)
        print("fone: ",fone)
        print("idade",idade)
        print("rg: ",rg)
        print("cpf: ",cpf)
        print("PROGRAMA FINALIZADO.")
        break
    if opcoes==6:
        print("destino: ",destino)
        print("origem: ",origem)
        print("duraçao: ",duraçao)
        print("valor da passagem: ",valorpass)
        print("desconto: ",desconto)
        print("resultado: ",result)
        print("PROGRAMA FINALIZADO.")
        break
    if opcoes==7:    
        print("ano: ",ano)
        print("horas de voo: ",horasdevoo)
        print("cor: ",cor)
        print("quantidade de passageiros: ",qntdp)
        print("modelo: ",modelo)
        print("PROGRAMA FINALIZADO.")
        break
    if opcoes==8:
        print("nome: ",nome2)
        print("cargo: ",cargo)
        print("idade: ",idade2)
        print("data de admissao: ",datae)
        print("fone: ",fone2)
        break
    if opcoes==0:
        print("programa encerrado.")
        break
