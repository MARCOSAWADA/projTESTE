# 2
def data():
    meses = ["nada", "janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]

    day = input('Digite o dia: ')
    mes = int(input('Digite o mes: '))
    ano = input('Digite o ano: ')

    print(f"{day} de {meses[mes]} de {ano}")

data()