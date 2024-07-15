# Elaborar uma função para retornar o maior de três números recebidos por parâmetro.

def encontrar_maior(a,b,c):
    return max(a, b, c)

num1 = 0
num2= 25
num3 = 55
maior_numero = encontrar_maior(num1, num2, num3)
print(f"O maior número entre {num1}, {num2}, {num3} é {maior_numero}.")