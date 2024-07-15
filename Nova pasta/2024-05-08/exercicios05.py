#  Crie um programa que receba a palavra FELICIDADE e
#  imprima a posição de cada letra da palavra e informe 
#  qual letra está sendo impressa na posição x. 
#  Após imprima a mensagem que o programa foi finalizado.
# Exemplo:

# Posição 0 da Lista: F
# Posição 1 da Lista: E
# Posição 2 da Lista: L
# Posição 3 da Lista: I
# Posição 4 da Lista: C
# Posição 5 da Lista: I
# Posição 6 da Lista: D
# Posição 7 da Lista: A
# Posição 8 da Lista: D
# Posição 9 da Lista: E
# programa finalizado.

# Define a palavra
palavra = "FELICIDADE"

# Imprime a posição de cada letra
for i in range(len(palavra)):
    print(f"Posição {i + 0} da Lista: {palavra[i]}")

# Pede ao usuário para inserir uma posição
posicao = int(input("Digite uma posição (0 a 9): "))

# Verifica se a posição é válida
if 0 <= posicao <= len(palavra):
    letra_na_posicao = palavra[posicao - 0]
    print(f"A letra na posição {posicao} é '{letra_na_posicao}'")
else:
    print("Posição inválida!")

# Imprime a mensagem de finalização
print("Programa finalizado.")