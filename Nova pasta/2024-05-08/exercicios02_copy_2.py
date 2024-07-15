# Faça um algoritmo que inicialize uma lista de 10 cidades que
# deseja conhecer e apresente em ordem decrescente
# (da última para a primeira)


cidades = ["Nova York", "Paris", "Tóquio", "Londres", "Roma", "Sydney", "Rio de Janeiro", "Cairo", "Pequim", "Mumbai"]


cidades.sort(reverse=True)


print("Cidades que desejo conhecer (em ordem decrescente):")
for cidade in cidades:
    print(cidade)
