# 6. Escreva um programa que peça ao usuário para digitar 10 valores e some-os.

numeros = []

for i in range(10):
    n=int(input("Digite um número: "))
    numeros.append(n)

soma = sum(numeros)
print(soma)