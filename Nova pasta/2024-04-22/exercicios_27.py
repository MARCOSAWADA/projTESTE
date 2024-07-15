### 27. Escreva o menu de opções abaixo. Leia a opção do usuário e execute a operação escolhida. 
### Escreva uma mensagem de erro se a opção for inválida.
### Escolha a opção:
# 1- Soma de 2 números.
# 2- Diferença entre 2 números (maior pelo menor).
# 3- Produto entre 2 números.
# 4- Divisão entre 2 números (o denominador não pode ser zero).

# Mostrar o menu de opções
print("Escolha a opção:")
print("1- Soma de 2 números.")
print("2- Diferença entre 2 números (maior pelo menor).")
print("3- Produto entre 2 números.")
print("4- Divisão entre 2 números (o denominador não pode ser zero).")

# Ler a escolha do usuário
opcao = input("Digite o número da opção desejada: ")

# Realizar a operação correspondente à opção escolhida
if opcao == '1':
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    resultado = num1 + num2
elif opcao == '2':
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    resultado = abs(num1 - num2)
elif opcao == '3':
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    resultado = num1 * num2
elif opcao == '4':
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número (diferente de zero): "))
    if num2 != 0:
        resultado = num1 / num2
    else:
        resultado = "Erro: Divisão por zero."
else:
    print("Opção inválida.")
    resultado = None

# Mostrar o resultado da operação
if resultado is not None:
    print("O resultado da operação é:", resultado)