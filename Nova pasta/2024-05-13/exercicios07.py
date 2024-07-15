# 7. Escreva um programa que leia 10 inteiros e imprima sua média.

inteiro = int(input("Digite a quantidade de números inteiros: "))
numero = []
cont = 0

while cont < inteiro:
    numero.append(float(input("Digite os números: ")))
    cont = cont + 1

media = sum(numero) / len(numero)
print(media)