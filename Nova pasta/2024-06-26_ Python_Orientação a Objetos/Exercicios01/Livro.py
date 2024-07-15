class Livro:
    def __init__(self, nome, autor, editora, paginas):
        self.nome = nome
        self.autor = autor
        self.editora = editora
        self.paginas = paginas
        
    def alterar_editora(self,novaEditora):
        self.editora = novaEditora
        print(f"Editora alterada para: {self.editora}")
        
    def listar_paginas(self):
        return self.paginas
        
x = Livro("A Cabana", "eu não Lembro", "também Não sei", 100)
print(f"O nome do livro é: {x.nome}")
print(f"Autor do livro é: {x.autor}")
print(f"A editora do livro é: {x.editora}")
print(f"Número de páginas do livro é: {x.paginas}")

print("*"*50)
x.alterar_editora("oxe123")