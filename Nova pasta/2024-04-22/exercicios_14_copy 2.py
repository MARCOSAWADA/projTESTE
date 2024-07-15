### 14. Crie um programa que receba dois números e mostre o maior. 
###Se por acaso, os dois números forem iguais, imprima a mensagem: Números iguais.


numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))


if numero1 > numero2:
    print(numero1, "foi o maior numero digitado no primeiro numero.")
elif numero2 > numero1:
    print(numero2, "foi o maior numero digitado no segundo numero.")
else:
    print("Números iguais.")