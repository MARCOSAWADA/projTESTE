# 9. Escreva um programa que leia 10 números e escreva o menor valor lido e o maior valor lido.

numeros = []
contador = 0
while contador < 10:
    numeros.append(int(input("Digite um numero: ")))
    contador = contador + 1
print("MENOR NUMERO É: ", min(numeros))
print("MAIOR NUMERO É: ", max(numeros))