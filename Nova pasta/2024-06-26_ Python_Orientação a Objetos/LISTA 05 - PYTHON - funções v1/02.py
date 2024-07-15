#  Faça uma função que receba a data atual (dia, mês, ano) e exiba-a na tela
#  no formato textual por extenso. 
# Exemplo: Data:01/01/2000, imprimir: 1 de Janeiro de 2000.

def data_por_extenso(dia, mes, ano):


    nomes_meses = [
        "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
        "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
    ]
    

    print(f"{dia} de {nomes_meses[mes - 1]} de {ano}")

data_por_extenso(1, 1, 2000)
