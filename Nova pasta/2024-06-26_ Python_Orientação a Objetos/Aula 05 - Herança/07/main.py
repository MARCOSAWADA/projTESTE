from Brinquedos import Brinquedos
from BuzzLightyear import BuzzLightyear
from Woody import Woody
from Carrinho import Carrinho
from Boneca import Boneca

buzz = BuzzLightyear(cor="verde", tamanho="médio", preco=50)
buzz.brincar()
buzz.voar()

woody = Woody(cor="marrom", tamanho="grande", preco=40)
woody.brincar()
woody.laca()

carrinho = Carrinho(cor="vermelho", tamanho="pequeno", preco=20)
carrinho.brincar()
carrinho.correr()

boneca = Boneca(cor="rosa", tamanho="médio", preco=30)
boneca.brincar()
boneca.pentear_cabelo()