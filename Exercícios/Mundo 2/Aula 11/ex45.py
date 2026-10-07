import random
jokenpo = ['Pedra', 'Papel', 'Tesoura']
escolha_computador = random.choice(jokenpo)
print("-=-" * 20)
print("Vamos jogar Jokenpô!")
print("-=-" * 20)
print(f"Minha escolha: {escolha_computador}")
escolha_usuario = input("""
Escolha uma opção (Pedra, Papel ou Tesoura):
1. Pedra
2. Papel
3. Tesoura
Digite o nome da sua escolha:
""").capitalize()
if escolha_usuario == escolha_computador:
    print(f"Empate! Ambos escolheram {escolha_usuario}.")
elif (escolha_usuario == 'Pedra' and escolha_computador == 'Tesoura') or \
     (escolha_usuario == 'Papel' and escolha_computador == 'Pedra') or \
     (escolha_usuario == 'Tesoura' and escolha_computador == 'Papel'):  
    print(f"Você ganhou! {escolha_usuario} vence {escolha_computador}.")    
else:
    print(f"Você perdeu! {escolha_computador} vence {escolha_usuario}.")