from Hamburger import Hamburger

########INTERFACE DO USUÁRIO
codigo = int(input("Digite o código do Produto: "))
preco = float(input("Digite o preço do Produto: "))

lista = ['BACON','PAO','SALADA','CHEDDAR','DOUBLE BURGER','CEBOLA CARAMELIZADA']

###########MÉTODO DE CLASSE -> FUNÇÃO / AÇÃO
########### CLASSE -> ESTRUTURA
########### OBJETO -> VARIÁVEL NO SISTEMA QUE TEM OS MOLDES
########### ATRIBUTOS -> SÃO COMO UMA VARIÁVEL DA CLASSE, VOCE PODE ALTERAR OS DADOS

xbancon = Hamburger(codigo,preco,lista)

preco = xbancon.getPreco()
print("PRECO DO XBACON: ",preco)

xbancon.getIngredientes()

xbancon.setPreco(99.90)

print(xbancon.preco)