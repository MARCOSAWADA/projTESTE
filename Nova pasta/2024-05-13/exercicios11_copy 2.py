# 11. Considerando o intervalo de 0 a 100. 
# Crie um programa que calcule e mostre a soma dos 50 primeiros números pares.


contador = 0
pares = []
i = 2

while contador <= 49:
    if i % 2 == 0:
        pares.append(i)
        i += 2
        contador += 1
print(f"Soma = {sum(pares)}")
