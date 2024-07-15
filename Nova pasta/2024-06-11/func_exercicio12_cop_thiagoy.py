# Crie uma função que receba uma lista como argumento, os valores da lista devem ser numéricos, 
# por fim retorne a média desses valores.

def calcula_media(lista):
    soma = 0
    for num in lista:
        soma += num
    media = soma / len(lista)
    return media

list_de_numeros = [8,9,20,11,3,6,7,10,11]
x = calcula_media(list_de_numeros)
print(x)



# _______________________________________________________________


def calcula_media(lista):
    media = sum(lista) / len(lista)
    return media

list_de_numeros = [50,5,5,5,5,5,5,5,5,5,5,10]
x = calcula_media(list_de_numeros)
print(x)