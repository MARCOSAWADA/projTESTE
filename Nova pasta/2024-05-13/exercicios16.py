# 16. Escreva um programa que leia um número inteiro positivo ímpar N e 
# imprima todos os números ímpares de 1 até N em ordem crescente

n = int(input("Digite um número: "))
i = 1
contador = 0
while contador < n and i <= n:
    print(i)
    i = i + 2
    contador = contador + 1