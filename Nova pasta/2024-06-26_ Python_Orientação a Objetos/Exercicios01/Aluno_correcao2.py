class Aluno:
    def __init__(self, nome, ra, notas):
        self.nome = nome
        self.ra = ra
        self.notas = notas
    
    def mostrar_situacao(self):
        media = sum(self.notas) / len(self.notas)

        # CORREÇÃO        
        if media < 5:
            return "REPROVADO"
        elif media >= 5 and media <= 6.9:
            return "EXAME"
        else:
            return "APROVADO"

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

# print(f"Nome do aluno: {aluno1.nome}")
# print(f"RA do aluno: {aluno1.ra}")
# print(f"Notas do aluno: {aluno1.nota1}, {aluno1.nota2}, {aluno1.nota3}, {aluno1.nota4}")
# print(f"Situação do aluno Maria: {aluno1.mostrar_situacao()}")


# aluno2 = Aluno("João", "2021002", 6.5, 5.5, 7.0, 5.0)
# print(f"Situação do aluno João: {aluno2.mostrar_situacao()}")


# aluno3 = Aluno("Pedro", "2021003", 4.0, 3.5, 4.0, 4.5)
# print(f"Situação do aluno Pedro: {aluno3.mostrar_situacao()}")
