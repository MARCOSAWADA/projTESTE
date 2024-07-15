# 1. Faça um algoritmo utilizando o comando while que mostra uma contagem regressiva na tela, 
# iniciando em 10 e terminando em 0. Mostrar uma mensagem “FIM!” após contagem.

contador = int(input("digite um numero: "))

while contador >= 0:
    print(contador)
    contador = contador - 1

print("FIM!")