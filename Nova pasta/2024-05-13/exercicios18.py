# 18. Escreva um algoritmo que leia certa quantidade de números e imprima o maior deles. 
# A quantidade de números a serem lidos deve ser fornecida pelo usuário.

# Lê a quantidade de números a serem lidos
quantidade = int(input("Digite a quantidade de números: "))

# Inicializa a variável para armazenar o maior número
maior = int(input("Digite um número: "))  # Lê o primeiro número como referência

# Lê os números restantes e encontra o maior
while quantidade > 1:
    numero = int(input("Digite um número: "))
    if numero > maior:
        maior = numero
    quantidade -= 1

# Imprime o maior número
print(f"O maior número digitado foi {maior}.")
