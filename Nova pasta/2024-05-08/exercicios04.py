#  Faça um algoritmo que receba o número de avaliações do estudante
#  que será (utilizado como contador), após receba as notas e
# apresente a média do estudante.

# Pede ao usuário para inserir o número de avaliações
num_avaliacoes = int(input("Digite o número de avaliações: "))

# Inicializa a variável para armazenar a soma das notas
soma_notas = 0

# Pede ao usuário para inserir as notas
for i in range(num_avaliacoes):
    nota = float(input(f"Digite a nota {i + 1}: "))
    soma_notas += nota

# Calcula a média das notas
media = soma_notas / num_avaliacoes

# Imprime a média
print(f"A média do estudante é: {media:.2f}")
