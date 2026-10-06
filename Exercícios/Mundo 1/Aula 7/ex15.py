km = float(input("Insira a distância percorrida com o carro em Km: "))
dias = int(input("Insira a quantidade de dias que o veículo foi utilizado: "))
taxa_dias = dias * 60
taxa_km = km * 0.15
conta = taxa_dias + taxa_km
print(f"Você percorreu {km}Km em {dias} dias. Você deverá pagar R${conta :.2f} por este uso.")