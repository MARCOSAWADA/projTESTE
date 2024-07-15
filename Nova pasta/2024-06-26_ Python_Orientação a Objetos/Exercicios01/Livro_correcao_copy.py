class Livro:
    def __init__(self, nome: str, autor:str, editora:str, paginas:int):
        self.nome = nome
        self.autor = autor
        self.editora = editora
        self.paginas = paginas

    def getPaginas(self):
        print(self.paginas)

    def setEditora(self,nomenovo):
        self.editora = nomenovo
        print(f"Editora alterada para: {self.editora}")
        

        
livro1 = Livro("A Cabana", "A eu não Lembro", "A também Não sei", "100")
livro2 = Livro("B Cabana", "B eu não Lembro", "B também Não sei", "200")
livro3 = Livro("C Cabana", "C eu não Lembro", "C também Não sei", "300")
livro4 = Livro("D Cabana", "D eu não Lembro", "D também Não sei", "400")

livro4.getPaginas() # 400
print(livro4.editora) # D também Não sei

livro4.setEditora("aloha") # Editora alterada para: aloha => print da linha 13
print(livro4.editora) # aloha