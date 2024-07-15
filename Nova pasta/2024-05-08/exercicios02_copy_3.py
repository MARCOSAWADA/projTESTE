# Faça um algoritmo que inicialize uma lista de 10 cidades que
# deseja conhecer e apresente em ordem decrescente
# (da última para a primeira)

cidades = ["Los Angeles", "San Francisco", "Nova York", "Paris", "Tóquio", "Londres", "Egito", "Alpes Suíços", "Florianópolis", "Rio de Janeiro"]
contador = len(cidades) - 1

while contador >= 0:
    print(cidades[contador])
    contador = contador - 1
