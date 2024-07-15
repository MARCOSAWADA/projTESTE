# Crie uma função que receba como argumento uma lista, com valores de qualquer tipo.
# A função deve imprimir todos os elementos da lista numerando-os. Exemplo:

# 1, Pera
# 2, Uva
# 3, Maçã
# 4, Salada mista

def imprime(lista):
    cont = 0
    while cont < len(lista):
        print(f"{cont+1}, {lista[cont]}")
        cont+=1

listadecompra = ['Pera', 'Uva', 'Maçã', 'Salada mista']
imprime(listadecompra)
