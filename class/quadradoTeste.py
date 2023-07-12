from quadrado import*
        
lado=float(input("digite o tamanho do lado do seu quadrado: "))
result= quadrado(lado)
result.mostrar()

lado=float(input("digite o novo lado do quadrado: "))
result.alterar(lado)
    