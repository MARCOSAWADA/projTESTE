### 25. Crie uma mini calculadora mostre ao usuário um menu com 4 opções de operações matemáticas (as básicas, por exemplo). 
### O usuário escolhe uma das opções e o seu programa então pede dois valores numéricos e realiza a operação, 
### mostrando o resultado e finalizando o programa.


print("ben vindo a calculadora")
print("---" * 20)
print("para adicao press: +")
print("para subtração press: -")
print("para multiplicação press: *")
print("para divisao press: /")
print("---" * 20)
opcao = input("digite sua opção + - * / :")

if opcao == "+":
    n1 = float(input("digite o n1:"))
    n2 = float(input("digite o n2:"))
    soma = n1 + n2
    print(soma)
elif opcao == "*":
    n1 = float(input("digite o n1: "))
    n2 = float(input("digite o n2: "))
    res = n1 * n2
    print("resultado: ", res)
elif opcao == "/":
    n1 = float(input("digite o n1: "))
    n2 = float(input("digite o n2: "))
    if n2 <= 0:
        print("nao é possivel dividir")
    else:
        res = n1 - n2
        print("resultado: ", res)
else:
    print("opcao invalida")