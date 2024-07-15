class Livro:
    def __init__(self, nome, autor, editora, paginas):
        self.nome = nome
        self.autor = autor
        self.editora = editora
        self.paginas = paginas

    def getPaginas(self):
        print(self.paginas)

    def SetEditora(self,nomenovo):
        self.editora = nomenovo
        print(f"Editora alterada para: {self.editora}")
        

        
livro1 = Livro("A Cabana", "eu não Lembro", "também Não sei", "100")
print(f"O nome do livro é: {livro1.nome}")
print(f"Autor do livro é: {livro1.autor}")
print(f"A editora do livro é: {livro1.editora}")
print(f"Número de páginas do livro é: {livro1.paginas}")

print("*"*50)
livro1.SetEditora("oxe123")