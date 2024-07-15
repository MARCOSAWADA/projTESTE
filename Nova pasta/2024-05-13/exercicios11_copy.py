# 11. Considerando o intervalo de 0 a 100. 
# Crie um programa que calcule e mostre a soma dos 50 primeiros números pares.


# O valor da soma será armazenado nesta variável
soma = 0

# Contador, para registrar a quantidade de números somados
contador = 0

# Estrutura de repetição while
while contador < 50:
    # Incremento no contador
    contador += 1
    
    # Soma dos números pares
    soma += contador * 2

print(f"A soma dos 50 primeiros números pares é: {soma}")
