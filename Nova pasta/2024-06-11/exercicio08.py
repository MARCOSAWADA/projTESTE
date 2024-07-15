#8.  input novamente
# if e else

estoque = {
    "chaves": "50",
    "cadeados": "50",
    "alicate": "40",
    "martelo": "5",
}

print(estoque)
print(estoque.keys())
print(estoque.values())

produto= input("Digite um produto do estoque: ")
if produto in estoque:
    print("o produto fornecido: ", produto , "tem no estoque, e a quantidade dele é: ", estoque[produto])
else:
    print("O Produto não está disponível")