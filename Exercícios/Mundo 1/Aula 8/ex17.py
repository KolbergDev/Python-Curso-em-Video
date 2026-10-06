from math import hypot
cat_adj = float(input("Insira o comprimento do cateto adjacente (cm): "))
cat_op = float(input("Insira o comprimento do cateto oposto (cm): "))
hipo = hypot(cat_adj, cat_op)
print(f"A hipotenusa do triangulo com essas medidas de catetos é: {hipo}cm")