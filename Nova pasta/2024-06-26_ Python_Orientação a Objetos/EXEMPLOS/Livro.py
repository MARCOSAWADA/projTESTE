class Livro:
    def __init__(self,nome:str,autor:str,editora:str,pags:int) -> None:
        self.nome = nome
        self.autor = autor
        self.editora = editora
        self.paginas = pags

    def getPaginas(self):
        print(self.paginas)

    def setEditora(self,nomenovo):
        self.editora = nomenovo


livro1 = Livro("Memórias Póstumas de Brás Cubas","Machado de Assis","Atlas","268")

livro2 = Livro("Poesia Concreta","Paulo Leminsk","Tesla","199")

livro3 = Livro("Alberto Caeiro","Fernando Pessoa","Brasil","199")

livro4 = Livro("O Alquimista","Paulo Coelho","OK","150")

livro4.getPaginas()

print(livro4.editora)

livro4.setEditora(123)

print(livro4.editora)

