### 13. Escreva um programa que, dados dois números inteiros, mostre na tela o maior deles, 
### assim como a diferença existente entre ambos.


numero1 = int(input("Digite o primeiro número inteiro: "))
numero2 = int(input("Digite o segundo número inteiro: "))

diferenca = 0

if numero1 > numero2:
    diferenca = numero1 - numero2
    print(numero1, "foi o maior numero digitado no primeiro numero.")

elif numero2 > numero1:
    diferenca = numero2 - numero1
    print(numero2, "foi o maior numero digitado no segundo numero.")

else: 
    print("Numeros iguais ")    
    
print(f"A diferença entre os ambos é {diferenca} ")