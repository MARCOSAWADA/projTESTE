### 09. Leia um número fornecido pelo usuário. Se esse número for positivo, calcule a raiz quadrada do 
### número. Se o número for negativo, mostre uma mensagem dizendo que o número é inválido.

import math

# Leitura do número fornecido pelo usuário
numero = float(input("Digite um número: "))

# Verificação e cálculo da raiz quadrada se o número for positivo
if numero >= 0:
    raiz_quadrada = math.sqrt(numero)
    print("A raiz quadrada de", numero, "é", raiz_quadrada)
else:
    print("Número inválido. O número deve ser positivo.")