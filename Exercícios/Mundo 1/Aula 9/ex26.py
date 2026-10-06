frase = str(input("Escreva uma frase: ")).upper().strip().replace(" ", "")
print(f"A letra A aparece {frase.count("A")} vezes na frase.")
print(f"A primeira letra A aparece na posição: {frase.find("A")+1}")
print(f"A última vez que a letyra A aparece na frase é na posição: {frase.rfind("A")+1}")