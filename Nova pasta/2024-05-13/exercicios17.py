# 17. Escreva um programa que leia um número inteiro positivo n 
# e calcule a soma dos n primeiros números naturais.

# Lê o valor de n
n = int(input("Digite um número inteiro positivo: "))

# Inicializa a soma
soma = 0

# Calcula a soma dos n primeiros números naturais
i = 1
while i <= n:
    soma += i
    i += 1

# Imprime o resultado
print(f"A soma dos {n} primeiros números naturais é {soma}.")
