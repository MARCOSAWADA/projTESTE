from Aluno_correcao2 import Aluno

notas = []
nome = input("DIGITE O NOME DO CABOCLO: ")
ra = int(input("DIGITE O RA DO CABOCLO: "))

i = 0
while i < 4:
    nota = float(input("DIGITE A NOTA DO CABOCLO: "))
    notas.append(nota)
    i = i + 1

a = Aluno(nome, ra, notas)
print(a.mostrar_situacao())