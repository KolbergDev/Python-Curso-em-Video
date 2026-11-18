print("-=-" * 18)
print("                Testando Palíndromos")
print("-=-" * 18)
try:
    frase = input("Digite uma frase ou palavra: ").lower().strip()

    if frase == "":
        raise ValueError("A entrada não pode ser vazia.")

    limpo = ""
    for c in frase:
        if c.isalpha():
            limpo += c

    if limpo == "":
        raise ValueError("A entrada não possui dados válidos.")

    if limpo == limpo[::-1]:
        print(f"A frase/palavra '{frase}' é um Palíndromo.")
    else:
        print(f"A frase/palavra '{frase}' não é um Palíndromo.")

except ValueError as e:
    print("Erro: Insira somente letras e espaços.")