quantidade = int(input("DIGITE A QUANT NUM PARA VETOR: "))
lista1 = []
lista2 = []
i = 0
while i < quantidade:
    num = int(input("DIGITE UM NUMERO: "))
    lista1.append(num)
    lista2.append(num*5)
    i = i + 1

print(lista1)
print(lista2)