# Faça uma função para verificar se um numero é positivo ou negativo.
# Sendo que o valor de retorno será 1 se positivo, -1 se negativo e 
# 0 se for igual a 0.

def verificar_numero(numero):

    if numero > 0:
        return 1
    elif numero < 0:
        return -1
    else:
        return 0


print(verificar_numero(1))
print(verificar_numero(-3))
print(verificar_numero(0))