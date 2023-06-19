while True:
    print(" -------------------------------------\n","             CALCULADORA          \n","-------------------------------------")
    option=input("BEM VINDO! O QUE VOCÊ DESEJA CALCULAR?\n1 - ADIÇÃO\n2 - SUBTRAÇÃO\n3 - MULTIPLICAÇÃO\n4 - DIVISÃO\n5 - EXPONENCIAÇÃO\n6 - RAIZ QUADRADA\n7 - ÁREA DE UM QUADRADO\n8 - VOLUME DE UM CUBO\n9 - MÉDIA DE 4 NÚMEROS.\n10 - FATORIAL\n0 - SAIR\n----------------------\n")

    if option=="1":
        a=float(input("Digite o primeiro número: "))
        b=float(input("Digite o segundo número: "))
        result=a+b
        print("O resultado foi {:f}".format(result))
        continue
    elif option=="2":
        a=float(input("Digite o primeiro número: "))
        b=float(input("Digite o segundo número: "))
        result=a-b
        print("O resultado foi {:f}".format(result))       
        continue
    elif option=="3":
        a=float(input("Digite o primeiro número: "))
        b=float(input("Digite o segundo número: "))
        result=a*b
        print("O resultado foi {:f}".format(result))       
        continue
    elif option=="4":
        a=float(input("Digite o primeiro número: "))
        b=float(input("Digite o número que divide o primeiro: "))
        result=a/b
        print("O resultado foi {:f} %2.f" .format(result))      
        continue 
    elif option=="5":
        a=float(input("Digite o primeiro número: "))
        b=float(input("Digite o número que será o exponencial: "))
        result=a**b
        print("O resultado foi {:f}".format(result))      
        continue
    elif option=="6":
        a=float(input("Digite um número para descobrir a raiz quadrada."))
        result=a**0.5
        print("A raiz quadrada do número digitado é {:f}".format(result))      
        continue
    elif option=="7":
        a=float(input("Digite o tamanho em centímetros de um dos lados do quadrado: "))
        result=a**2
        print("A área deste quadrado é {:f}".format(result))        
        continue 
    elif option=="8":
        a=float(input("Digite o comprimento de uma das arestas do cubo: "))
        result=a**3
        print("O volume do cubo é {:f}".format(result))      
        continue 
    elif option=="9":
        a=float(input("Digite o primeiro número: "))
        b=float(input("Digite o segundo número: "))
        c=float(input("Digite o terceiro número: "))
        d=float(input("Digite o quarto número: "))
        result=(a+b+c+d)/4
        print("A média dos quatro números digitados é {:f}".format(result))     
        continue 
    elif option=="10":
        a=int(input("Digite um número para ter seu fatorial: "))
        fat=1
        b=2
        while b<-a:
            fat=fat*b
            b=b+1
        print("O resultado é %d".format(fat))     
        continue
    elif option=="0":
        break
    else:
        print("Erro. Opção não encontrada.")    
        continue
        