nomecomp = str(input("Insira seu nome completo: ")).strip()
nome = nomecomp.split()
print(f"Seu primeiro nome é {nome[0]}")
print(f"Seu último nome é {nome[len(nome)-1]}")