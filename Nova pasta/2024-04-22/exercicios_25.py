### 25. Crie uma mini calculadora mostre ao usuário um menu com 4 opções de operações matemáticas (as básicas, por exemplo). 
### O usuário escolhe uma das opções e o seu programa então pede dois valores numéricos e realiza a operação, 
### mostrando o resultado e finalizando o programa.

# Função para realizar a operação de adição
def adicao(a, b):
    return a + b

# Função para realizar a operação de subtração
def subtracao(a, b):
    return a - b

# Função para realizar a operação de multiplicação
def multiplicacao(a, b):
    return a * b

# Função para realizar a operação de divisão
def divisao(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: Divisão por zero."

# Mostrar o menu de opções
print("Escolha a operação:")
print("1. Adição")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")

# Ler a escolha do usuário
opcao = input("Digite o número da operação desejada: ")

# Verificar a escolha do usuário e realizar a operação correspondente
if opcao == '1':
    valor1 = float(input("Digite o primeiro valor: "))
    valor2 = float(input("Digite o segundo valor: "))
    resultado = adicao(valor1, valor2)
elif opcao == '2':
    valor1 = float(input("Digite o primeiro valor: "))
    valor2 = float(input("Digite o segundo valor: "))
    resultado = subtracao(valor1, valor2)
elif opcao == '3':
    valor1 = float(input("Digite o primeiro valor: "))
    valor2 = float(input("Digite o segundo valor: "))
    resultado = multiplicacao(valor1, valor2)
elif opcao == '4':
    valor1 = float(input("Digite o primeiro valor: "))
    valor2 = float(input("Digite o segundo valor (diferente de zero): "))
    resultado = divisao(valor1, valor2)
else:
    print("Opção inválida.")
    resultado = None

# Mostrar o resultado da operação
if resultado is not None:
    print("O resultado da operação é:", resultado)

