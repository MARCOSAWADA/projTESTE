### 10. Leia um número real. 
### Se o número for positivo imprima a raiz quadrada. 
### Caso contrário imprima o número ao quadrado.

import math

# Leia um número real
numero = float(input("Digite um número real: "))

# Verifique se o número é positivo ou negativo
if numero >= 0:
    # Se for positivo, imprima a raiz quadrada
    print("A raiz quadrada de", numero, "é", math.sqrt(numero))
else:
    # Se for negativo, imprima o número ao quadrado
    print("O quadrado de", numero, "é", numero ** 2)

