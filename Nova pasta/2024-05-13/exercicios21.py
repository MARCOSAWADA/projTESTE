# 21. Crie um programa que receba dois números. Calcule e mostre:
# • a soma dos números pares desse intervalo de números, incluindo os números digitados;
# • a multiplicação dos números ímpares desse intervalo, incluindo os digitados;


x = int(input("Digite o primeiro número (X): "))
y = int(input("Digite o segundo número (Y): "))

soma_pares = 0
multiplicacao_impares = 1

while x <= y:
    if x % 2 == 0:
        soma_pares += x
    else:
        multiplicacao_impares *= x
    x += 1

print(f"A soma dos números pares entre {x} e {y} é {soma_pares}.")
print(f"A multiplicação dos números ímpares entre {x} e {y} é {multiplicacao_impares}.")
