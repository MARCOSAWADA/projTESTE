num_notas = int(input("DIGITE O NUMERO DE AVALICOES"))
provas = []
for nota in range(num_notas):
    provas.append(float(input("DIGITE A NOTA: ")))

media = sum(provas) / num_notas
print(media)