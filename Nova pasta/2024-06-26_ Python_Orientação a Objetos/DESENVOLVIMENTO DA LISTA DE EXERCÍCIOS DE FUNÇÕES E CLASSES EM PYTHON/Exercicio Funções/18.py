# 18
import random

def somapar(lista):
    soma = 0
    for i in lista:
        if i % 2 == 0:
            soma += i
    print(soma)

def sorteia():
    numeros = []

    for i in range(5):
        numeros.append(random.randint(1,100))
    return somapar(numeros)

sorteia()
