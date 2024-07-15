# Faça uma função que receba 3 números inteiros como parâmetro, 
# representando horas, minutos e segundos, e os converta em segundos.

def converter_para_segundos(horas, minutos, segundos):

    total_segundos = (horas * 3600) + (minutos * 60) + segundos
    return total_segundos


horas = 2
minutos = 30
segundos = 45
total_segundos = converter_para_segundos(horas, minutos, segundos)
print(f"{horas} horas, {minutos} minutos e {segundos} segundos equivalem a {total_segundos} segundos.")
