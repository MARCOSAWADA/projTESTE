numeros = [24,12,33,99,7,8.18,10.5,54]

#print(numeros[3]+numeros[4])

#print(len(numeros))

#soma todos da lista []
print(sum(numeros))

#print(sum(numeros))
print("MAIOR NUMERO: ", max(numeros))
print("MENOR NUMERO: ", min(numeros))
print("SOMA: ", sum(numeros))
print("MEDIA: " ,sum(numeros) / len(numeros))

#mostra os numeros em ordem
lista_ordenada = sorted(numeros)
print(lista_ordenada)

#mostra em ordem decrescente
numeros.sort(reverse=True)
print(numeros)