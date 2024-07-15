lista1 = []
lista2 = []
qtde = int(input("DIGITE QUANTOS NUMEROS VOCE ADD NA LISTA: "))

for elemento in range(qtde):
    num = int(input("Digite um número: "))
    lista1.append(num)
    lista2.append(num*5)

print(lista1)
print(lista2)