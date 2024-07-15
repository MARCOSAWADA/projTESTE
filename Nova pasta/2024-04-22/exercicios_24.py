### 24. Crie um programa que calcule e mostre a área de um trapézio. Sabe-se que:
### A = (basemaior + basemenor) * altura / 2

basemaior = float(input("Digite o valor da base maior: "))
basemenor = float(input("Digite o valor da base menor: "))
h = float(input("Digite o valor da altura: "))

A = (basemaior + basemenor) * h / 2
print("A área do trapéxio é: ", A)