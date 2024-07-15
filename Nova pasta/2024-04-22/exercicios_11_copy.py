###11. Crie um programa que leia um número e, caso ele seja positivo, calcule e mostre:
### • O número digitado ao quadrado;
### • A raiz quadrada do número digitado;



numero = float(input("Digite um número: "))

# Verifique se o número é positivo
if numero >= 0:
    quadrado = numero ** 2
    raiz = numero ** 0.5
    print("O número ao quadrado é:", quadrado)
    print("A raiz quadrada do número é:", raiz)
else:
    print("O número digitado não é positivo.")