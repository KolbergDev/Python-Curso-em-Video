nasc = int(input("Insira seu ano de nascimento: "))
ano_atual = 2026
idade = ano_atual - nasc
if idade < 18:
    tempo = 18 - idade
    print(f"Você não precisa se alistar, você tem {idade} anos de idade e só se alistará daqui {tempo} anos!")
elif idade > 18:
    tempo = idade - 18
    print(f"Você deve comparecer urgentemente em uma junta militar!! Já passou {tempo} ano(s) da hora do seu alistamento.")
else: 
    print(f"Você já tem {idade} anos, compareça a uma junta mlitar para realizar seu alistamento.")
