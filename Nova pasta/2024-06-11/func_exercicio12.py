# Crie uma função que receba uma lista como argumento, os valores da lista devem ser numéricos, 
# por fim retorne a média desses valores.

def calcular_media(lista):
    if not lista:
        return 0  # Retorna 0 se a lista estiver vazia
    return sum(lista) / len(lista)

# Exemplo de uso
valores = [10, 20, 30, 40, 50]
media = calcular_media(valores)
print(f"A média dos valores é: {media:.2f}")



# ___________________________________________________________

def calcular_media(lista):
    # Verifica se a lista está vazia
    if not lista:
        return 0
    
    # Calcula a soma dos valores na lista
    soma = sum(lista)
    
    # Calcula o número de elementos na lista
    num_elementos = len(lista)
    
    # Calcula a média
    media = soma / num_elementos
    
    return media

# Exemplo de uso da função
valores = [10, 20, 30, 40, 50]
media = calcular_media(valores)
print(f"A média dos valores é: , {media:.2f}")
