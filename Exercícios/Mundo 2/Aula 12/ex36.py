print("-=-" * 20)
print("SIMULADOR DE EMPRÉSTIMO")
print("-=-" * 20)
vcasa = float(input("Insira o valor da casa desejada: "))
salario = float(input("Insira o seu salário atual: "))
tempo = int(input("Insira em quantos anos você quer pagar: "))
prestaçao = vcasa / (tempo * 12)
if prestaçao > salario * 30 /100 :
    print(f"Empréstimo NEGADO! Prestação excede 30% de seu salário ({prestaçao:.2f}/{salario:.2f}).")
else:
    print(f"Parabéns, empréstimo APROVADO! Serão {tempo * 12} parcelas de R${prestaçao:.2f}.")