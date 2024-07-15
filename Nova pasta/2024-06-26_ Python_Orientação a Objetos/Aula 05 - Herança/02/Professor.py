from Pessoa1 import Pessoa1

class Professor(Pessoa1):
    def __init__(self, matricula, nome, idade,formacao,disciplina,cargahora,salario):
        super().__init__(matricula, nome, idade)
        self.formacao = formacao
        self.disciplina = disciplina
        self.carga = cargahora
        self.sal = salario

    def lecionar(self):
        return f"O melhor prof. {self.nome} acordou inspirado para lecionar"
    