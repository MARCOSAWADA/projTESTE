# 9. Escreva um programa que leia 10 números e escreva o menor valor lido e o maior valor lido.

numeros = []

for i in range(10):
    n=int(input("Digite um número: "))
    numeros.append(n)

print("MENOR NUMERO É: ", min(numeros))
print("MAIOR NUMERO É: ", max(numeros))
