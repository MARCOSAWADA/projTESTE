# 15. Crie um programa que leia um número inteiro positivo par N e
# imprima todos os números pares de 0 até N em ordem decrescente.

n = int(input("DIGITE QUANTOS NUMEROS: "))
i = n
contador = 0
while contador < n and i >=0:
    print(i)
    i = i -2
    contador = contador + 1