soma = 0
for num in range (1,7):
   n = int(input(f"Insira o {num}º numero inteiro: "))
   if n % 2 == 0:
        soma += n
print(f"A soma dos números pares é: {soma}")