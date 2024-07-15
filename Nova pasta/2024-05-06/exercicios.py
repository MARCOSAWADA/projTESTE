# Crie uma lista com 5 numeros inteiros
# imprima o tamanho da lista
# adicione 5 numeros decimais usando append
# remova os dois últimos itens da lista
# imprima o tamanho da lista
# imprima a lista ordenada
# inprima o maior e menor numero da lista
# imprima a lista em orde decrescente
# imprima a soma e média
# acrescente mais dois itens na posição 0 e 1

numeros = [1,2,3,4,5]
print(len(numeros))

numeros.append(1.1)
numeros.append(2.1)
numeros.append(3.1)
numeros.append(4.1)
numeros.append(5.1)
print(numeros)

numeros.pop()
numeros.pop()
print(numeros)

print(len(numeros))
ordenada = sorted(numeros)
print(numeros)

print("MAIOR NUMERO É: ", max(numeros))
print("MENOR NUMERO É: ", min(numeros))

numeros.sort(reverse=True)
print(numeros)

print("A SOMA É: ", sum(numeros))
print("A MÉDIA É: ", sum(numeros) / len(numeros))

numeros.insert(0, "PRIMEIRO")
numeros.insert(1, "SEGUNDO")
print(numeros)