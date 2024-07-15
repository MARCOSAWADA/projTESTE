# Crie uma função de um programa de teste para o cálculo do volume de uma esfera.
# Sendo que o raio é passado por parametro.
# V = 4/3 * pi * R elevado a 3

def calcular_volume_esfera(raio):

    pi = 3.14159
    volume = (4 / 3) * pi * (raio ** 3)
    return volume


raio_esfera = 5
volume_esfera = calcular_volume_esfera(raio_esfera)
print(f"O volume da esfera com raio {raio_esfera} é {volume_esfera:.2f}.")
