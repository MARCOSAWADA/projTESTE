from Pessoa1 import Pessoa1

class Aluno(Pessoa1):
    def __init__ (self,matricula, nome, idade, notas, media):
        super().__init__(matricula, nome, idade)
        self.notas = notas
        self.media = media

    def calcular_media(self):
        return sum(self.notas) / len(self.notas)

    def estudar(self):
        print(f"{self.nome} está estudando.")
