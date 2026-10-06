print("-=-" * 20)
print("CONVERSÃO DE BASES NÚMERICAS")
print("-=-" * 20)
num = int(input("Insira um número inteiro: "))
binario = bin(num)
octal = oct(num)
hexadecimal = hex(num)
base = int(input("""
Escolha uma base para esta conversão! 
1 - Para Binário.
2 - Para Octal.
3 - Para Hexadecimal.
Opção desejada: """))
if base == 1:
    print(f"O número {num} convertido para Binário fica: {binario}.")
elif base == 2:
    print(f"O número {num} convertido para octal fica : {octal}.")
elif base == 3:
    print(f"O número {num} convertido para HexaDecimal fica: {hexadecimal};")
else:
    print("Erro! Insira uma opção válida!")

