### 13. Escreva um programa que, dados dois números inteiros, mostre na tela o maior deles, 
### assim como a diferença existente entre ambos.

# Leia dois números inteiros
numero1 = int(input("Digite o primeiro número inteiro: "))
numero2 = int(input("Digite o segundo número inteiro: "))

# Verifique qual é o maior número
if numero1 > numero2:
    maior = numero1
    diferenca = numero1 - numero2
else:
    maior = numero2
    diferenca = numero2 - numero1

# Mostre o maior número e a diferença entre eles
print("O maior número é:", maior)
print("A diferença entre os números é:", diferenca)