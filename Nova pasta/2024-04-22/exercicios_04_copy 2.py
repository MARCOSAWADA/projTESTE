### 4. Crie um programa que receba três números e mostre-os em ordem crescente.

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))

lista=[n1,n2,n3]
lista = sorted(lista)

print("Os números em ordem crescente são:", lista)

