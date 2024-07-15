# 19. Escreva um algoritmo que leia um número inteiro entre 100 e 9999 
# e imprima na saída cada um dos algarismos que compõem o número.

# Lê o número inteiro
numero = int(input("Digite um número entre 100 e 9999: "))

# Verifica se o número está dentro do intervalo
while numero < 100 or numero > 9999:
    numero = int(input("Número inválido! Digite um número entre 100 e 9999: "))

# Separa os algarismos
milhar = numero // 1000
centena = (numero % 1000) // 100
dezena = (numero % 100) // 10
unidade = numero % 10

# Imprime os algarismos
print(f"Milhar: {milhar}, Centena: {centena}, Dezena: {dezena}, Unidade: {unidade}")
