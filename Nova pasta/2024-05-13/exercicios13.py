# 13. Crie um programa que leia um número inteiro positivo N 
# e imprima todos os números naturais de 0 até N em ordem decrescente.

n = int(input("Digite um número inteiro positivo: "))
for i in range(n, -1, -1):
    print(i)
