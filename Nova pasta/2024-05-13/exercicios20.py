# 20. Ler uma sequência de números inteiros e determinar se eles são pares ou não. 
# Deverá ser informado o número de dados lidos e número de valores pares. 
# O processo termina quando for digitado o número 0.

contador = 0
pares = 0

while True:
    numero = int(input("Digite um número inteiro (0 para sair): "))
    if numero == 0:
        break
    contador = contador + 1
    if numero % 2 == 0:
        pares = pares + 1

print("Foram lidos:",contador ,"números")
print("e números de pares é:" , pares)
