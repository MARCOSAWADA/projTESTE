def calcular_multa(peso_peixes):
    limite = 50
    valor_multa_por_quilo = 4.00  
    
    if peso_peixes > limite:
        excesso = peso_peixes - limite 
        multa = excesso * valor_multa_por_quilo 
    else:
        excesso = 0
        multa = 0.0
    
    
    print(f"Peso total de peixes: {peso_peixes} kg")
    print(f"Excesso de peso: {excesso} kg")
    print(f"Valor da multa: R$ {multa:.2f}")
    
    return excesso, multa

peso_peixes = float(input("Digite o peso total de peixes (em kg): "))  
excesso, multa = calcular_multa(peso_peixes)  



#def calcular_excesso_e_multa(peso_peixe):
#    limite_peso = 50
#    valor_multa_por_quilo= 4.00

#    excesso = max(0,peso_peixe - limite_peso)
#    multa = excesso * valor_multa_por_quilo

#    print(f"Peso total de peixes {peso_peixe} kg")
#    if excesso >0:
#        print(f"Excesso de peso: {excesso}")
#        print(f" Valor da multa: {multa}")

#peso_peixes = float(input("Digite o peso total de peixes em (kg): "))
#calcular_excesso_e_multa(peso_peixes)    