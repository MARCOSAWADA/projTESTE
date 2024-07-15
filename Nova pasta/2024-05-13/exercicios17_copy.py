# 17. Escreva um programa que leia um número inteiro positivo n 
# e calcule a soma dos n primeiros números naturais.


n = int(input("Digite um número inteiro positivo: "))


soma = 0


i = 1
while i <= n:
    soma = soma + i
    i = i + 1


print(f"A soma dos {n} primeiros números naturais é {soma}.")
