from random import randint
from time import sleep
comp = randint(0, 5)
print("-=-" * 20)
print("Estou pensando em um número, tente adivinhar... ")
print("-=-" * 20)
resp = int(input("Em que número eu pensei? "))
print("Pensando...")
sleep(3)
if resp == comp:
    print(f"Você ACERTOU! Que sorte =)")
else:
    print(f"ERROOOOU!! na verdade pensei em {comp}, não em {resp}")