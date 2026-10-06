a = float(input("Insira a medida de uma das retas em cm: "))
b = float(input("Insira mais uma medida de uma das retas em cm: "))
c = float(input("Insira a última medida de uma das retas em cm: "))
if (a + b > c) and (a + c > b) and (b + c > a):
    if a == b == c:
        print("Com estas retas você tem um triângulo Equilátero.")
    elif a == b != c or a == c != b or b == c != a:
        print("Com esta retas você tem um triângulo Isósceles.")
    else:
        print("Com estas retas você tem um triângulo Escaleno.")
else:
    print("Não é possível fazer um triângulo com estas retas.")
