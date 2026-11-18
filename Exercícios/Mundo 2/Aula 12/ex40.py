n1 = float(input("Insira a sua primeira nota: "))
n2 = float(input("Insira a sua segunda nota: "))
media = (n1 + n2) / 2
if media < 5:
    print(f"REPROVADO! Sua média foi {media}.")
elif media >= 5 and media <= 6.9:
    print(f"Você está de RECUPERAÇÃO! Sua média foi de {media}.")
else:
    print(f"APROVADO! Parabéns pelo desempenho, sua média foi {media}.")