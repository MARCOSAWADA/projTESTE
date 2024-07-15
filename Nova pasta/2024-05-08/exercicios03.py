#  Faça um algoritmo que receba 10 nomes em uma lista, e ao final 
# apresente todos os nomes recebidos.

# Cria uma lista vazia para armazenar os nomes
nomes = []

# Pede ao usuário para inserir 10 nomes
for i in range(11):
    nome = input("Digite um nome: ")
    nomes.append(nome)

# Imprime todos os nomes recebidos
print("Nomes recebidos: ")
for nome in nomes:
    print(nome)
