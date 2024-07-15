class Professor2:
    def __init__(self,nome,idade,nota): 

        self.nome = nome 
        self.idade = idade 
        self.nota = nota 

    
    def hello(self): 
        print(f" Olá {self.nome}")

    def mostrardados(self): 

        print(f" Profissao: {self.nome}")
        print(f" Hobby: {self.idade}")
        print(f" Estilo Musical: {self.nota}")

aluno = Professor2("mestre", "ler", "heavy metal")
print(aluno.nome)



print("-"*30)

aluno.hello()

print("-"*30)

aluno.mostrardados()

