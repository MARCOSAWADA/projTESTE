# Crie uma função que receba como argumento a potência elétrica de determinado aparelho e o tempo ligado e 
# retorne o consumo em KWh em seguida chame outra função para calcular a conta de energia,
# levando em consideração o consumo e o valor do KWh como argumentos.

def calcula_valor(consumo, preco):
    valor = consumo * preco
    return valor

def calcula_consumo(potencia, horas, preco):
    consumo = potencia * horas / 1000
    conta = calcula_valor(consumo, preco)
    return conta

potencia = int(input("DIGITE O VALOR DO APARELHO: "))
tempo = int(input("QUANTO TEMPO FOI UTILIZADO NO MES: "))
preco = float(input("VALOR DO KWH: "))

banho = calcula_consumo(potencia, tempo, preco)
print("R$: " , banho)