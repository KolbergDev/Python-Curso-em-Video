nasc = int(input("Insira seu ano de nascimento: "))
ano_atual = 2026
idade = ano_atual - nasc
if idade <= 9:
    print(f"Você tem {idade} anos, está na categoria: MIRIM")
elif idade <= 14:
     print(f"Você tem {idade} anos, está na categoria: INFANTIL")
elif idade <= 19: 
     print(f"Você tem {idade} anos, está na categoria: INFANTO")
elif idade <= 20:
      print(f"Você tem {idade} anos, está na categoria: ADULTO")
else: 
     print(f"Você tem {idade} anos, está na categoria: MASTER")
