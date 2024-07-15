num_avaliacoes = int(input("DIGITE A QUANTIDADE DE PROVAS"))
notas = []
cont = 0

while cont < num_avaliacoes:
    notas.append(float(input("DIGITE A NOTA: ")))
    cont = cont + 1

media = sum(notas) / len(notas)
print(media)
