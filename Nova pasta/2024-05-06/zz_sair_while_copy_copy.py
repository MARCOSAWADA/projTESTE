numeros = [28,11,2,4,6,99,55,56,57,27]
cont = 0
print(len(numeros))
print(numeros[cont])

while cont < len(numeros):
    print(numeros[cont])
    if numeros[cont] == 55:
        print("Achamos o numero 55 !")
        break
    else:
        cont = cont + 1