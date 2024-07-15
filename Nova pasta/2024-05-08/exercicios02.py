# Faça um algoritmo que inicialize uma lista de 10 cidades que
# deseja conhecer e apresente em ordem decrescente
# (da última para a primeira)

# Inicialize a lista de cidades
cidades = ["Nova York", "Paris", "Tóquio", "Londres", "Roma", "Sydney", "Rio de Janeiro", "Cairo", "Pequim", "Mumbai"]

# Ordene a lista em ordem decrescente
cidades.sort(reverse=True)

# Apresente as cidades em ordem decrescente
print("Cidades que desejo conhecer (em ordem decrescente):")
for cidade in cidades:
    print(cidade)