# Crie uma função que receba uma temperatura em graus Celsius e 
# retorne-a convertida em graus Fahrenheit.
# A fórmula de conversão é: F = C * (9.0/5.0) + 32.0,
# sendo F a temperatura em Fahrenheit e C a temperatura em Celsius.

def celsius_to_fahrenheit(celsius):
 
    fahrenheit = celsius * (9.0 / 5.0) + 32.0
    return fahrenheit


celsius_temp = 25
fahrenheit_temp = celsius_to_fahrenheit(celsius_temp)
print(f"{celsius_temp}°C é aproximadamente {fahrenheit_temp:.2f}°F.")
