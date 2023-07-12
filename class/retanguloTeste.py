from retangulo import*

lado1=float(input("digite o tamanho da base do retangulo: "))
lado2=float(input("digite o tamanho da altura do retangulo: "))
if lado1==lado2:
    print("nao é um retangulo...")

else:
    print("a area do retangulo é:")
    result=retangulo(lado1,lado2)
    result.mostrar()
    print("o valor do perimetro é: ")
    result.perimetro()

    lado1=float(input("digite o novo tamanho da base do retangulo: "))
    lado2=float(input("digite o novo tamanho da altura do retangulo: "))
    print("a area do retangulo é:")
    result.alterar(lado1,lado2)
    print("o novo perimetro é: ")
    result.perimetro2()
    result.rodape()