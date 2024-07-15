#  Receba um número inteiro positivo na entrada e 
#  imprima os n primeiros números ímpares naturais.
#  Para a saída, siga o formato do exemplo abaixo.

# 1   Digite o valor de n: 5
# 2   1
# 3   3
# 4   5
# 5   7
# 6   9

numero = int(input("Digite um número: "))

for impar in range(1, numero,2):
    print(impar)

