# 20
import random
def sorteiaaluno(num):
    alunos = []
    while len(alunos) < num:
        nome = input("Digite o nome do aluno: ")
        alunos.append(nome)
    x = len(alunos)
    escolher = random.randint(0, x)
    print(alunos[escolher])

sorteiaaluno(4)