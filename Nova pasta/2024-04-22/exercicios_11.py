###11. Crie um programa que leia um número e, caso ele seja positivo, calcule e mostre:
### • O número digitado ao quadrado;
### • A raiz quadrada do número digitado;


# Leia um número
numero = float(input("Digite um número: "))

# Verifique se o número é positivo
if numero >= 0:
    # Calcule o quadrado do número
    quadrado = numero ** 2
    # Calcule a raiz quadrada do número
    raiz_quadrada = numero ** 0.5
    
    # Mostre o número ao quadrado
    print("O número ao quadrado é:", quadrado)
    # Mostre a raiz quadrada do número
    print("A raiz quadrada do número é:", raiz_quadrada)
else:
    print("O número digitado não é positivo.")