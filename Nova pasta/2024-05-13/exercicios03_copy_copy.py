# 3. Crie um programa que determine o mostre os 10 primeiros números pares, 
# considerando números maiores que 0.

# Quantidade de números pares que queremos encontrar
n = 10

# Lista para armazenar os números pares
numeros_pares = []

# Encontrando os primeiros n números pares
for i in range(1, n + 1):
    numeros_pares.append(2 * i)

# Exibindo os números pares
print("Os 10 primeiros números pares são:", numeros_pares)

