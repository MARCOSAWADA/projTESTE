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
    
    # def get_maior_lado(self):
    #     # Comparação manual dos lados para determinar o maior
    #     if self.ladoA >= self.ladoB and self.ladoA >= self.ladoC:
    #         return self.ladoA
    #     elif self.ladoB >= self.ladoA and self.ladoB >= self.ladoC:
    #         return self.ladoB
    #     else:
    #         return self.ladoC
    
# Função para obter um número inteiro positivo do usuário
def obter_numero_positivo(mensagem):
    while True:
        try:
            numero = int(input(mensagem))
            if numero > 0:
                return numero
            else:
                print("Por favor, digite um número inteiro positivo.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro positivo.")


print("Digite as medidas dos lados do triângulo:")
ladoA = obter_numero_positivo("Lado A: ")
ladoB = obter_numero_positivo("Lado B: ")
ladoC = obter_numero_positivo("Lado C: ")


triangulo1 = Triangulo(ladoA, ladoB, ladoC)


perimetro = triangulo1.calcular_perimetro()
print(f"O perímetro do triângulo é: {perimetro}")


maior_lado = triangulo1.get_maior_lado()
print(f"O maior lado do triângulo é: {maior_lado}")