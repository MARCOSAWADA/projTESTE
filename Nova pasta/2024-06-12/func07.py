def caulcular_salario(horas_trabalhadas, salario_por_hora):
    carga_horaria_base = 40 
    taxa_horas_extras = 1.5

    if horas_trabalhadas <= carga_horaria_base:
       salario = horas_trabalhadas * salario_por_horas
    else:
       horas_extras = horas_trabalhadas - carga_horaria_base
       salario_base =  carga_horaria_base * salario_por_horas
       salario_horas_extras = horas_extras * salario_por_horas * taxa_horas_extras 
       salario = salario_base + salario_horas_extras
       return salario

horas_trabalhadas = 45 
salario_por_horas = 20
salario_total= caulcular_salario(horas_trabalhadas,salario_por_horas)
print(f'o salario total para horas {horas_trabalhadas}, horas trabalhadas R$ {salario_total}')
    