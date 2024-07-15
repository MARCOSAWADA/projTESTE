# Crie uma função que retorne uma lista como valor padrão.
# Para esta função. consideraremos como argumentos de entrada a QUANTIDADE DE ELEMENTOS e o
# VALOR PADRÃO a ser atribuído a todos eles. Exemplo de retorno:

# {1,1,1,1,1,1,1,1,}
# {"A","A","A","A"}

def criar_lista_padrao(qtd_elementos, valor_padrao):
    return [valor_padrao] * qtd_elementos

# Exemplo de uso
lista_numerica = criar_lista_padrao(8, 1)
lista_letras = criar_lista_padrao(4, 'A')

print(f"Lista numérica: {lista_numerica}")
print(f"Lista de letras: {lista_letras}")


# _____________________________________________________


def criar_lista(valor_padrao, quantidade_elementos):
    # Retorna a lista com o valor padrão repetido a quantidade de vezes especificada
    return [valor_padrao] * quantidade_elementos

# Exemplos de uso da função
lista_1 = criar_lista(1, 9)
print(lista_1)  # Saída: [1, 1, 1, 1, 1, 1, 1, 1, 1]

lista_2 = criar_lista("A", 4)
print(lista_2)  # Saída: ['A', 'A', 'A', 'A']
