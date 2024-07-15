# Uma pessoa está interessada em comprar um carro e deseja fazer um financiamento. 
# Ela tem uma quantia X para dar de entrada, uma taxa de juros é definida pelo banco e a 
# pessoa pode escolher o número de parcelas que deseja financiar. ​

# Crie uma função que simule um financiamento, levando em consideração o regime de juros compostos. 
# O programa deve solicitar ao usuário o valor do veiculo, o valor da entrada, a taxa de juros e a 
# quantidade de parcelas. 

# Além disso, o programa deve exibir o valor total pago, a quantia dos juros pagos e o valor de cada parcela. 
# O programa deve apresentar as informações de forma clara e objetiva, facilitando a compreensão por parte do usuário.​























def calcular_tempo(tempo_minutos):
    preco_minimo = 9.00  # Valor mínimo por hora
    preco_adicional = 1.50  # Valor por hora adicional
    tempo_horas = tempo_minutos / 60  # Convertendo minutos para horas

    if tempo_minutos < 15:
        return 0  # Se o tempo utilizado for menor que 15 minutos, não há cobrança

    horas_inteiras = int(tempo_horas)
    minutos_restantes = tempo_minutos % 60

    if minutos_restantes > 0:
        horas_inteiras += 1  # Se houver minutos extras, arredonda para cima para a próxima hora

    if horas_inteiras <= 1:
        return preco_minimo  # Se o tempo utilizado for até 1 hora, retorna o valor mínimo

    preco_total = preco_minimo + (horas_inteiras - 1) * preco_adicional  # Calcula o preço total
    return preco_total

# Teste da função
tempo_utilizado = int(input("Informe o tempo utilizado no estacionamento (em minutos): "))
valor_total = calcular_tempo(tempo_utilizado)
print(f"O valor total a ser pago pelo tempo de estacionamento é: R$ {valor_total:.2f}")
