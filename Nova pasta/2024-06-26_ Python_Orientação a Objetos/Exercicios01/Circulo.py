class Circulo:
    def __init__(self, raio):
        self.raio = raio
    
    def imprimir_raio(self):
        print(f"O raio do círculo é: {self.raio}")
    
    def calcular_area(self):
        area = 3.14159 * self.raio ** 2
        return area
    
    def calcular_circunferencia(self):
        circunferencia = 2 * 3.14159 * self.raio
        return circunferencia

# Criando um objeto circulo1 da classe Circulo com raio 5
circulo1 = Circulo(5)

# Exemplo de acesso aos métodos
circulo1.imprimir_raio()

area = circulo1.calcular_area()
print(f"A área do círculo é: {area:.2f}")

circunferencia = circulo1.calcular_circunferencia()
print(f"A circunferência do círculo é: {circunferencia:.2f}")
