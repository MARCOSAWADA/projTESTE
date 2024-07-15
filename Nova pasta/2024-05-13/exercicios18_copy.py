# 18. Escreva um algoritmo que leia certa quantidade de números e imprima o maior deles. 
# A quantidade de números a serem lidos deve ser fornecida pelo usuário.


quantidade = int(input("Digite a quantidade de números: "))


maior = int(input("Digite um número: "))


while quantidade > 1:
    numero = int(input("Digite outros números: "))
    if numero > maior:
        maior = numero
    quantidade = quantidade - 1


print("O maior número digitado foi: ", maior)
