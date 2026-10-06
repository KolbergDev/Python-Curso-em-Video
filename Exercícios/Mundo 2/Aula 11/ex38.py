n1 = int(input("Insira um número inteiro: "))
n2 = int(input("Insira mais um número inteiro: "))
if n1 > n2:
    print(f"O número {n1} é maior que o número {n2}.")
elif n2 > n1:
    print(f"O número {n2} é maior que o número {n1}.")
else:
    print(f"Não existe um maior, {n1} e {n2} são iguais.")