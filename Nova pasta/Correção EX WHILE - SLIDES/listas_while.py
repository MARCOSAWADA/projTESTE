lista = [2,99,28,27,32,38,44,55,66,1,24]
encontrar = int(input("DIGITE O NUMERO QUE DESEJA ENCONTRAR: "))
cont = 0

while cont < len(lista): #testa a condição
    print(lista[cont])
    if lista[cont] == encontrar:
        print(f"Encontramos o encontrar {encontrar}")
        break #sair do while
    else:
        cont = cont + 1 #controle da condição para entrar no while

print("FIM DO PROGRAMA!!!")

