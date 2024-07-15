class Triangulo:
    def __init__(self, ladoA, ladoB, ladoC):
        self.ladoA = ladoA
        self.ladoB = ladoB
        self.ladoC = ladoC
    
    def calcular_perimetro(self):
        perimetro = self.ladoA + self.ladoB + self.ladoC
        return perimetro
    
    def get_maior_lado(self):
        maior_lado = max(self.ladoA, self.ladoB, self.ladoC)
        return maior_lado


print("Digite as medidas dos lados do triângulo:")
ladoA = int(input("lado a: "))
ladoB = int(input("lado b: "))
ladoC = int(input("lado c: "))


triangulo1 = Triangulo(ladoA, ladoB, ladoC)


perimetro = triangulo1.calcular_perimetro()
print(f"O perímetro do triângulo é: {perimetro}")


maior_lado = triangulo1.get_maior_lado()
print(f"O maior lado do triângulo é: {maior_lado}")