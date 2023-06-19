
number1 = float(input("Qual o primeiro numero: "))

if number1 > 1000:
    print ("Ok, seu salario receberá um aumento de 5%")
    number2 = number1 + (number1*0.05)
    print ("Salario anterior era de %.2f com o reajuste foi para %.3f" %(number1,number2)) 
elif number1 >= 500 and number1 <= 1000:
    print ("Ok, seu salario receberá um aumento de 10%")
    number2 = number1 + (number1*0.10)
    print ("Salario anterior era de %.2f com o reajuste foi para %.3f" %(number1,number2)) 
elif number1 <= 500:
    print ("Ok, seu salario receberá um aumento de 15%")
    number2 = number1 + (number1*0.15)
    print ("Salario anterior era de %.2f com o reajuste foi para %.3f" %(number1,number2)) 

