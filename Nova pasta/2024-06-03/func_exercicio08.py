# Um pescador, comprou um PC para controlar o rendimento diário de seu trabalho. 
# Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do MS (50 Kg) 
# deve pagar uma multa de R$ 4,00 por quilo excedente. 

# O pescador precisa que você crie uma função para ler a quantidade de peixes e calcular o excesso. 
# Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que 
# o pescador deverá pagar. 

# Imprima os dados do programa com as mensagens adequadas.​

def calcular_multa(peso_peixes):
    limite = 50
    excesso = peso_peixes - limite
    multa = excesso * 4 
    return excesso, multa


peso_peixes = float(input("Informe o peso dos peixes (em Kg): "))


excesso, multa = calcular_multa(peso_peixes)


if excesso > 0:
    print(f"O peso dos peixes excede o limite em {excesso:.2f} Kg.")
    print(f"Portanto, o pescador deverá pagar uma multa de R$ {multa:.2f}.")
else:
    print("O peso dos peixes está dentro do limite estabelecido. Nenhuma multa é devida.")
