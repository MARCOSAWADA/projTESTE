# 14. Crie um programa que leia um número inteiro positivo par N e 
# imprima todos os números pares de 0 até N em ordem crescente.

n = int(input("DIGITE QUANTOS NUMEROS: "))
i = 0
contador = 0
while contador < n and i <= n:
    print(i)
    i = i + 2
    contador = contador + 1