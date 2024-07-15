#  Faça um algoritmo que receba 10 nomes em uma lista, e ao final 
# apresente todos os nomes recebidos.


nomes = []


for i in range(11):
    nome = input("Digite um nome: ")
    nomes.append(nome)


print("Nomes recebidos: ")
for nome in nomes:
    print(nome)
