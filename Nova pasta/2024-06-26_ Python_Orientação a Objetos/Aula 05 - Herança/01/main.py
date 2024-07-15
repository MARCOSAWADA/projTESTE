from Filme import Filme
from Filme import Acao
from Filme import Drama


filme = Filme("DURO DE MATAR 2",199)
filme.setNome("DURO DE COZINHAR 3")

print(filme.getNome())

naufrago = Drama("NAUFRAGO",185,"TOM HANKS")

naufrago.play()

lista_explosivos = ['BOMBA','GRANADA','DINAMITE','BOMBA NUCLEAR']
john = Acao("Jonh Wick",140,lista_explosivos)

john.play()