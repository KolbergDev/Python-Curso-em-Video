a = float(input("Insira a medida de uma das retas em cm: "))
b = float(input("Insira mais uma medida de uma das retas em cm: "))
c = float(input("Insira a última medida de uma das retas em cm: "))
if (a + b > c) and (a + c > b) and (b + c > a):
    print("Com estas retas, é possível fazer um triângulo.")
else: 
    print("Não é possível fazer um triângulo com estas retas.")