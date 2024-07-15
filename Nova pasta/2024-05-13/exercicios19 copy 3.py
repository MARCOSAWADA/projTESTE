# 19. Escreva um algoritmo que leia um número inteiro entre 100 e 9999 
# e imprima na saída cada um dos algarismos que compõem o número.



numero = int(input("Digite um número entre 100 e 9999: "))


while numero < 100 or numero > 9999:
    numero = int(input("Número inválido! Digite um número entre 100 e 9999: "))


unidade = numero % 10
numero //= 10
dezena = numero % 10
numero //= 10
centena = numero % 10
milhar = numero // 10

print("Dezena:", dezena)
print("Unidade:", unidade)
print("centena:", centena)
print("milhar:", milhar)