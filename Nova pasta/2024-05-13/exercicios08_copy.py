# 8. Escreva um programa que leia 10 inteiros positivos, ignorando não positivos, 
# e imprima sua média.

total_numeros = 10
soma = 0
contador = 0

print("Digite 10 números inteiros positivos: ")

while contador < total_numeros:
    numero = int(input("Digite o número: "))
    if numero >= 0:
        soma = soma + numero
        contador = contador + 1
    else:
        print("Número não positivo. Digite novamente.")

media = soma / total_numeros
print("A média dos números positivos é: " ,media)
