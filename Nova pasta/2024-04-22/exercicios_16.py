### 16. Crie um programa que leia 2 notas de um aluno, 
### verifique se as notas são válidas e exiba na tela a média destas notas. 
### Uma nota valida deve ser, obrigatoriamente, um valor entre 0.0 e 10.0, 
### onde caso a nota não possua um valor válido, este fato deve será informado ao usuário e o programa termina

# Leia as duas notas do aluno
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

# Verifique se as notas são válidas
if 0.0 <= nota1 <= 10.0 and 0.0 <= nota2 <= 10.0:
    # Calcule a média das notas
    media = (nota1 + nota2) / 2
    # Exiba a média na tela
    print("A média das notas é:", media)
else:
    # Caso alguma nota não seja válida, informe o usuário e termine o programa
    print("Nota inválida. As notas devem estar entre 0.0 e 10.0.")
