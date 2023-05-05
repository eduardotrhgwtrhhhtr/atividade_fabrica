prod=input("digite o produto: ")
quant=int(input ("digite a quantidade do produto: "))
value=float(input("digite o valor do produto: "))
per=float(input("de 1 a 100, digite qual o desconto do produto: "))


totalprod=(value-(value*(per/100)))
totalfinal=(totalprod*quant)

print("o produto %s, na quantidade %d, vale %.2f"%(prod,quant,totalfinal))