### 5. Faça um Programa que verifique se uma letra digitada é "F" ou "M". 
### Conforme a letra escreva: 
### F - Feminino, M – Masculino ou Sexo Inválido.

# Leitura da letra
letra = input("Digite 'F' para feminino ou 'M' para masculino: ")

# Verificação e impressão do gênero
if letra == 'F' or letra == 'f':
    print("F - Feminino")
elif letra == 'M' or letra == 'm':
    print("M - Masculino")
else:
    print("Sexo Inválido")