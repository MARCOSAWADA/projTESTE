numeros = [2,3,4,11,5]
i = 0

# Parando / Encerrando o loop, se 11 for encontrado

while i < len(numeros):
    if numeros[i] == 11:
        print("Encontramos o numero 11!")
        break
    else:
        i = i + 1