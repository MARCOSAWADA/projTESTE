### 03. Crie um programa que receba dois números e mostre qual deles é o maior.

n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))

if(n1 > n2):
    print("n1 é maior que n2")
elif(n2 > n1):
    print("n2 é maior que n1")
else:
    print("Os números são iguais")