class Aluno:
    def __init__(self, nome, ra, nota1, nota2, nota3, nota4):
        self.nome = nome
        self.ra = ra
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
        self.nota4 = nota4
    
    def mostrar_situacao(self):
        media = (self.nota1 + self.nota2 + self.nota3 + self.nota4) / 4
        
        if media >= 7.0:
            return "APROVADO"
        elif 5.0 <= media < 7.0:
            return "EXAME"
        else:
            return "REPROVADO"

# Criando um objeto aluno1 da classe Aluno
aluno1 = Aluno("Maria", "2021001", 8.0, 7.5, 6.0, 9.0)

# Exemplo de acesso aos atributos e método
print(f"Nome do aluno: {aluno1.nome}")
print(f"RA do aluno: {aluno1.ra}")
print(f"Notas do aluno: {aluno1.nota1}, {aluno1.nota2}, {aluno1.nota3}, {aluno1.nota4}")
print(f"Situação do aluno Maria: {aluno1.mostrar_situacao()}")

# Outro exemplo com um aluno em situação de exame
aluno2 = Aluno("João", "2021002", 6.5, 5.5, 7.0, 5.0)
print(f"Situação do aluno João: {aluno2.mostrar_situacao()}")

# Exemplo com um aluno reprovado
aluno3 = Aluno("Pedro", "2021003", 4.0, 3.5, 4.0, 4.5)
print(f"Situação do aluno Pedro: {aluno3.mostrar_situacao()}")
