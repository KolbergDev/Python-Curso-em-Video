vel = int(input("Insira a velocidade do carro: "))
multa = float( (vel - 80) * 7)
if (vel > 80):
    print(f"Você ultrapassou os 80km/h, sua multa será de R${multa}")
else: print("Parábens, continue respeitando a velocidade.")