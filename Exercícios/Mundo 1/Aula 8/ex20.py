import random
aluno1 = input("Digite o nome do primeiro aluno: ")
aluno2 = input("Digite o nome do segundo aluno: ")
aluno3 = input("Digite o nome do terceiro aluno: ")
aluno4 = input("Digite o nome do quarto aluno: ")
alunos = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(alunos)
print(f"O primeiro a apagar o quadro é o(a): {alunos[0]}")
print(f"O segundo a apagar o quadro é o(a): {alunos[1]}")
print(f"O terceiro a apagar o quadro é o(a): {alunos[2]}")
print(f"O último a apagar o quadro é o(a): {alunos[3]}")