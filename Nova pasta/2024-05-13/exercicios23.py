# 23. Escreva um programa que leia um número inteiro e calcule a soma de todos os divisores desse  número, 
# com exceção dele próprio. Ex: a soma dos divisores do número 66 é:
# 1 + 2 + 3 + 6 + 11 + 22 + 33 = 78

# n=int(input("a: "))

# contador=0

# while n >=66:
#     if n


def soma_divisores(numero):
    soma = 0
    for i in range(1, numero + 1):
        if numero % i == 0:
            soma += i
    return soma

# Exemplo de uso:
numero = 66
print("A soma dos divisores de", numero, "é:", soma_divisores(numero))
