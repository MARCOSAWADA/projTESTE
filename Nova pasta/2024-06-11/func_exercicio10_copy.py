# Uma pessoa está interessada em comprar um carro e deseja fazer um financiamento. 
# Ela tem uma quantia X para dar de entrada, uma taxa de juros é definida pelo banco e a 
# pessoa pode escolher o número de parcelas que deseja financiar. ​

# Crie uma função que simule um financiamento, levando em consideração o regime de juros compostos. 
# O programa deve solicitar ao usuário o valor do veiculo, o valor da entrada, a taxa de juros e a 
# quantidade de parcelas. 

# Além disso, o programa deve exibir o valor total pago, a quantia dos juros pagos e o valor de cada parcela. 
# O programa deve apresentar as informações de forma clara e objetiva, facilitando a compreensão por parte do usuário.​


def simular_financiamento(valor_veiculo, entrada, taxa_juros, num_parcelas):
    
    financiamento = valor_veiculo - entrada
    
    
    valor_total_pago = financiamento * (1 + taxa_juros) ** num_parcelas
    
   
    total_juros = valor_total_pago - financiamento
    
    return valor_total_pago, total_juros


valor_veiculo = float(input("Digite o valor do veículo: R$ "))
entrada = float(input("Digite o valor da entrada: R$ "))
taxa_juros = float(input("Digite a taxa de juros (% ao ano): ")) / 100
num_parcelas = int(input("Digite a quantidade de parcelas: "))


total_pago, total_juros = simular_financiamento(valor_veiculo, entrada, taxa_juros, num_parcelas)


valor_parcela = total_pago / num_parcelas


print("Valor total pago: R$ {:.2f}".format(total_pago))
print("Total de juros pagos: R$ {:.2f}".format(total_juros))
print("Valor de cada parcela: R$ {:.2f}".format(valor_parcela))
