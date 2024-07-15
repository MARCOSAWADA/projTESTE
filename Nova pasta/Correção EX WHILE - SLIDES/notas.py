numero_avaliacoes = int(input("DIGITE O NUMERO DE PROVAS: "))
i = 0
soma = 0
while i < numero_avaliacoes:
    soma += float(input("DIGITE A NOTA: "))
    i = i + 1

media = soma / numero_avaliacoes
print(media)
