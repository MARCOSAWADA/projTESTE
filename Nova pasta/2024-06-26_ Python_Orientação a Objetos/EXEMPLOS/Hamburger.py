class Hamburger:
    def __init__(self,cod : int,preco : float,ingredientes : list):
        self.cod = cod
        self.preco = preco
        self.ingredientes = ingredientes
        
    def getPreco(self):
        return self.preco
    
    def setPreco(self,novoPreco):
        self.preco = novoPreco

    def getIngredientes(self):
        for item in self.ingredientes:
            print(item)



