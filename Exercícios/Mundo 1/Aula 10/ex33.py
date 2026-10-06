num1 = int(input("Insira o 1° número inteiro: "))
num2 = int(input("Insira o 2° número inteiro: "))
num3 = int(input("Insira o 3° número inteiro: "))

if (num1 > num2 and num1 > num3):
    maior = num1
elif (num2 > num1 and num2 > num3):
    maior = num2
elif (num3 > num1 and num3 > num2):
    maior = num3

if (num1 < num2 and num1 < num3):
    menor = num1
elif (num2 < num1 and num2 < num3):
    menor = num2
elif (num3 < num1 and num3 < num2):
    menor = num3
print(f"O número {menor} é o menor e o número {maior} é o maior.")