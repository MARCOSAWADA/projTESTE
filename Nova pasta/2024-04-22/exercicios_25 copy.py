### 25. Crie uma mini calculadora mostre ao usuário um menu com 4 opções de operações matemáticas (as básicas, por exemplo). 
### O usuário escolhe uma das opções e o seu programa então pede dois valores numéricos e realiza a operação, 
### mostrando o resultado e finalizando o programa.

operacao = input("selecione uma dessas operações [+][-][*][/]: ")

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

if (operacao == "+"):
    res = n1+n2
    print("O resultado é: ", res)
elif (operacao == "-"):
    res = n1-n2
    print("O resultado é: ", res)
elif (operacao == "*"):
    res = n1*n2
    print("O resultado é: ", res)
elif (operacao == "/"):
    res = n1/n2
    print("O resultado é: ", res)