### 14. Crie um programa que receba dois números e mostre o maior. 
###Se por acaso, os dois números forem iguais, imprima a mensagem: Números iguais.

# Leia dois números
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

# Verifique se os números são iguais
if numero1 == numero2:
    print("Números iguais.")
else:
    # Determine o maior número
    maior_numero = max(numero1, numero2)
    print("O maior número é:", maior_numero)