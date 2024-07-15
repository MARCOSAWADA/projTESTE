# 10 - Classe Carro: Crie uma classe que modele um Livro. Esta classe deve possuir os seguintes atributos:
# Modelo, Marca, Cor, Ano, Valor, Nível (default 0) , Consumo
# A classe deve ter o seguintes métodos:
# abastecer(); - deve incrementar no nível do tanque de combustível.
# andar(); - recebe a distancia em km que o veículo andou
# verificar_nível(); - o deve criar uma forma de calcular quantos litros de comb. foram gasto por km
# calcular_imposto()  -  deve considerar o IPVA do carro em 2,5% do valor.

class Carro:
    def __init__(self,modelo,marca,cor,ano,valor,nivel=5):
        self.modelo = modelo
        self.marca = marca
        self.cor = cor
        self.ano = ano
        self.valor = valor
        self.nivel = nivel
    
    def calcular_imposto(self):
        imposto = (self.valor * 3) / 100
        return imposto

    def abastecer(self,qtde_litros):
        self.nivel = self.nivel + qtde_litros

    def andar(self,km):
        consumo = km / 10.8
        self.nivel = self.nivel - consumo

    def verificar_nivel(self):
        return self.nivel


car1 = Carro("Jetta","Volks","Prata",2022,180000)
print(car1.calcular_imposto())
print("NIVEL DE GASOLINA ",car1.nivel," litros")
car1.abastecer(45)
print("NIVEL DE GASOLINA ",car1.nivel," litros")
car1.andar(250)
tanque = car1.verificar_nivel()
print(f"{tanque:.2f}")