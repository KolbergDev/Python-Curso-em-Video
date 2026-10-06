salario = float(input("Insira o seu salário: "))
if salario > 1250:  
    print(f"Seu novo salário é de {(salario * 1.10):.2f}")
else:
    print(f"Seu novo salário é de R$ {(salario * 1.15):.2f}")
    