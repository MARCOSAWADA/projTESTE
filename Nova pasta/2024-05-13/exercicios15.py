# 15. Crie um programa que leia um número inteiro positivo par N e
# imprima todos os números pares de 0 até N em ordem decrescente.

n = int(input("DIGITE QUANTOS NUMEROS: "))
i = 0
contador = 2
while contador <= n:
    print(i)
    i = i -2
    contador = contador + 1