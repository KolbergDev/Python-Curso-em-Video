lado = float(input("Insira quanto a sua parede tem de largura (m): "))
altura = float(input("Insira quanto a sua parede tem de altura (m): "))
area = lado * altura
tinta = 2
quant = area / tinta
input(f"Para pintar essa área de parede {area}m² serão necessários {quant} litros de tinta.")