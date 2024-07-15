
i = 0
soma = 0
while i < 10:
    try:
        x = int(input("DIGITE UM NUMERO: "))
        soma += x
        i+=1
    except:
        print("VALOR INVÁLIDO!! TENTE NOVAMENTE!!")


print(soma)