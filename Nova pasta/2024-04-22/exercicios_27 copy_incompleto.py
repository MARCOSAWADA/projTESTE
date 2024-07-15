### 27. Escreva o menu de opções abaixo. Leia a opção do usuário e execute a operação escolhida. 
### Escreva uma mensagem de erro se a opção for inválida.
### Escolha a opção:
# 1- Soma de 2 números.
# 2- Diferença entre 2 números (maior pelo menor).
# 3- Produto entre 2 números.
# 4- Divisão entre 2 números (o denominador não pode ser zero).


opcao = input("Digite o número da opção desejada: ")

n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo número: "))


if opcao == '1':
    soma = n1 + n2
    print("soma de 2 numeroes é: ", soma)
elif opcao == '2':
    diferenca = n1 - n2
    print("A diferença entre 2 numeros é: ", diferenca)
elif opcao == '3':
    produto = n1 * n2
    print("o produto ente 2 numeros é: ", produto)
elif opcao == '4':
    if n2 != 0:
        divisao = n1 / n2
        print(" a divisão entre 2 numeros é: ", divisao)
    else:
        divisao = "Erro: Divisão por zero."
else:
    print("Opção inválida.")

