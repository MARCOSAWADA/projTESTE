# 21. Crie um programa que receba dois números. Calcule e mostre:
# • a soma dos números pares desse intervalo de números, incluindo os números digitados;
# • a multiplicação dos números ímpares desse intervalo, incluindo os digitados;



n1 = int(input("DIGITE UM NUM: "))
n2 = int(input("DIGITE UM NUM: "))
multi = 1
soma = 0

for num in range(n1,n2+1):
    if num % 2 != 0:
        multi *= num
    if num % 2 == 0:
        soma += num

# while n1 < n2:
#     if n1 % 2 != 0:
#         multi *= n1
#     if n1 % 2 == 0:
#         soma += n1
#     n1 = n1 +1

print(multi)
print(soma)
