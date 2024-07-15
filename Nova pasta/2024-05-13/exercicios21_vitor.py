# 21. Crie um programa que receba dois números. Calcule e mostre:
# • a soma dos números pares desse intervalo de números, incluindo os números digitados;
# • a multiplicação dos números ímpares desse intervalo, incluindo os digitados;



i = 1

while i <= 2:
    n = int(input("Digite um número: "))

    i = i + 1
pares = 0
impar = 1
for item in range(n):
    if(item %2 == 0):
        pares = pares + item
    elif(item %2 != 0):
        impar = impar * item

print("A soma: ",pares)
print("A multiplicação dos impares é: ",impar)
