# Crie uma função que receba múltiplos argumentos não nomeados, 
# considere que a função receba números inteiros como argumentos e 
# retorne a soma dos argumentos.​

def soma(*args):
    total = 0
    for num in args:
        total += num
    return total


print(soma(1, 2, 3))  # Saída: 6
print(soma(5, 10, 15, 20))  # Saída: 50
print(soma(-1, 5, 7, -3, 10))  # Saída: 18

