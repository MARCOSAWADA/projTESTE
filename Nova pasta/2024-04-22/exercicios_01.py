### 01. Faça um programa que leia 2 números inteiros e 1 real. 
### Calcule e mostre: o produto do primeiro com a metade do segundo, 
### a soma do triplo do primeiro com o terceiro. O terceiro número digitado ao cubo

n1= int(input("Digite o primeiro número: "))
n2= int(input("Digite o segundo número: "))
n3= float(input("Digite o terceiro número: "))

# Cálculos
produto = n1 * (n2 / 2)
soma = (3 * n1) + n3
cubo_num_real = n3 ** 3

# Exibição dos resultados
print("Produto do primeiro com a metade do segundo:", produto)
print("Soma do triplo do primeiro com o terceiro:", soma)
print("Cubo do terceiro número digitado:", cubo_num_real)