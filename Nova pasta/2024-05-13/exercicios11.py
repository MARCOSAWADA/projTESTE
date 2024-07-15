# 11. Considerando o intervalo de 0 a 100. Crie um programa que calcule 
# e mostre a soma dos 50 primeiros números pares.

# Inicializa as variáveis
n = 50  # Número de termos a serem somados
soma = 0
num = 2  # Primeiro número par

# Calcula a soma dos 50 primeiros números pares
while n > 0:
    soma += num
    num += 2
    n -= 1

# Exibe o resultado
print(f"A soma dos 50 primeiros números pares é {soma}")
