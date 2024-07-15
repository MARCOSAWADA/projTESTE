# Crie uma função que receba dois números como parâmetros e 
# mostre a potência do número elevado a n vezes, exemplo:
# pot(2,3)
# _______
# 2**1=2
# 2**2=4
# 2**3=8
# _______

def mostrar_potencias(base, n):


    for i in range(1, n + 1):
        resultado = base ** i
        print(f"{base}**{i} = {resultado}")

base = 2
n = 3
mostrar_potencias(base, n)