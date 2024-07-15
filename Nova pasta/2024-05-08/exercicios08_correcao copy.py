#  Faça para 10 números inteiros para um vetor de inteiros.
#  Computar um segundo vetor que terá o resultado da multiplicação 
#  por um escalar inteiro 5.

vet1 = []
vet2 = []
i = 0

while i < 5:
    num = int(input("Digite um numero: "))
    vet1.append(num)
    vet2.append(num*5)
    i = i + 1

print(vet1)
print(vet2)