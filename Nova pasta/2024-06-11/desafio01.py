dicionario = {}

nota01= input("digite 1 NOTA: ")
valor01 = int(input("Digite o valor correspondente: "))
nota02= input("digite 2 NOTA: ")
valor02 = int(input("Digite o valor correspondente: "))
nota03= input("digite 3 NOTA: ")
valor03 = int(input("Digite o valor correspondente: "))
nota04= input("digite 4 NOTA: ")
valor04 = int(input("Digite o valor correspondente: "))


dicionario[nota01] = valor01
dicionario[nota02] = valor02
dicionario[nota03] = valor03
dicionario[nota04] = valor04

print("Dicionário atualizado:", dicionario)

media=(valor01+valor02+valor03+valor04) / 4
print(media)

