# Crie uma função que receba como argumento uma lista, com valores de qualquer tipo.
# A função deve imprimir todos os elementos da lista numerando-os. Exemplo:

# 1, Pera
# 2, Uva
# 3, Maçã
# 4, Salada mista

def imprimir_lista_numerada(lista):
    for i, item in enumerate(lista, start=1):
        print(f"{i}, {item}")

# Exemplo de uso
frutas = ["Pera", "Uva", "Maçã", "Salada mista"]
imprimir_lista_numerada(frutas)
