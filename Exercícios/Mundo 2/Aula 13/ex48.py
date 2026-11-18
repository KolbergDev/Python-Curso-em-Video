impares = 0
for num in range (1, 501):
    if num % 2 != 0 and num % 3 == 0:
        impares += num
print(f"A soma dos números ímpares, múltiplos de 3, de 1 a 500 é: {impares}")
