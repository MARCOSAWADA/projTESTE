# 10. Crie um programa que leia um número inteiro N e 
# depois imprima os N primeiros números naturais ímpares.

numeros = int(input("digite um número: "))
i = 1
contador = 0
while contador < numeros:
    print(i)
    i = i + 2
    contador = contador + 1
