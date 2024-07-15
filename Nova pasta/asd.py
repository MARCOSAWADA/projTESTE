class Pessoa:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


    def mandaroi(self):
        return "oi", self.nome
    
    def mostraridade(self):
        return self.idade
    
class Edini:
    def __init__(self, nome):
        self.nome = nome

    def faltas(self):
        if self.nome == "Joao":
            return "FALTA"
        else:
            return "fiz chamada jaKKKK"
        

class Date:
    def __init__(self, datetime):
        self.datetime = datetime

    def dia(self):
        return self.datetime
