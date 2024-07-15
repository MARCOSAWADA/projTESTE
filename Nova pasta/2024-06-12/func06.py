def calcularTempo(tempo_minutos):
    
    valor_minimo = 9.00
    valor_adicional_por_hora = 1.50
    minutos_por_hora = 60
    
    if tempo_minutos < 15:
        return 0.00
    
    horas_completas = tempo_minutos // minutos_por_hora
    minutos_restantes = tempo_minutos % minutos_por_hora
    
 
    if horas_completas == 0:
        valor_total = valor_minimo
    else:
        valor_total = valor_minimo + (horas_completas * valor_adicional_por_hora)
       
        if minutos_restantes > 0:
            valor_total += valor_adicional_por_hora
    
    return round(valor_total, 2)

tempo_utilizado = 135 
valor_a_pagar = calcularTempo(tempo_utilizado)
print(f'Tempo utilizado: {tempo_utilizado} minutos')
print(f'Valor total a pagar: R$ {valor_a_pagar:.2f}')