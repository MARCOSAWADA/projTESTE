# 2. Crie um programa que determine o mostre os 5 primeiros números ímpares, 
# considerando números maiores que 0.

n = int(input("DIGITE QUANTOS NUMEROS: "))
i = 1
contador = 0
while contador < n:
    print(i)
    i = i + 2
    contador = contador + 1
