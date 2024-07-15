
#9. atraves dos inputs adicionar no dicionario
# texto.split() contador da lista dentro do dicionario

dicionario = {}

texto = input("Digite a frase: ")
x = texto.split()
dicionario['Total'] = len(x)
print(dicionario)
print(f"Total de palavras: {len(x)}")