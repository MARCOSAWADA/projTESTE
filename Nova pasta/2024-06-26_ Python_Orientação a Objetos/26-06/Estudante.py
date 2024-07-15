class Estudante: #DEFINIÇÃO DA CLASSE
    def __init__(self,matricula,nome,idade,nota): # MÉTODO CONSTRUTOR
        self.matricula = matricula #ATRIBUTO
        self.nome = nome #ATRIBUTO
        self.idade = idade #ATRIBUTO
        self.nota = nota #ATRIBUTO

    
    def hello(self): # MÉTODO
        print(f" Olá {self.nome}")

    def mostrardados(self): # MÉTODO
        print(f" Matricula: {self.matricula}")
        print(f" Nome: {self.nome}")
        print(f" Idade: {self.idade}")
        print(f" Nota: {self.nota}")

aluno = Estudante(1212, "Pedro", 18,80)
print(aluno.nome)

# _________________________________________

aluno2 = Estudante(1313, "DOMITILA", 22,90)
print(aluno2.nome)

# _________________________________________
aluno.hello()

aluno2.hello()
aluno2.nome = "ANA PATRICIA"


# _________________________________________

aluno2.mostrardados()
aluno.mostrardados()

