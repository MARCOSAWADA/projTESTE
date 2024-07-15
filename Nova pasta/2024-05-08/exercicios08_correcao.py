#  Faça para 10 números inteiros para um vetor de inteiros.
#  Computar um segundo vetor que terá o resultado da multiplicação 
#  por um escalar inteiro 5.

vet1 = [5,8,9,13,11]
vet2 = []
i = 0
while i < len(vet1):
    vet2.append(vet1[i]*5)
    i = i + 1

print(vet1)
print(vet2)