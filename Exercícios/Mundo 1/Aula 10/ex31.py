distancia = int(input("Insira a distância da viagem em Km: "))
if distancia <= 200:
    print(f"Você deverá pagar R${distancia * 0.50} por esta viagem.")
else: 
    print(f"Você deverá pagar R${distancia * 0.45} por esta viagem.")