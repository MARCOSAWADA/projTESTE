### 10. Leia um número real. 
### Se o número for positivo imprima a raiz quadrada. 
### Caso contrário imprima o número ao quadrado.



# Leia um número real
numero = float(input("Digite um número real: "))



if numero >= 0:
    raiz= numero**0.5
    # Se for positivo, imprima a raiz quadrada
    print("A raiz quadrada de", numero, "é", raiz)
else:
    quadrado= numero**2
    # Se for negativo, imprima o número ao quadrado
    print("O quadrado de", numero, "é", quadrado)

