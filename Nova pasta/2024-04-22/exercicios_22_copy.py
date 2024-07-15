### 22. Escreva um programa que leia um inteiro entre 1 e 7 e imprima o dia da semana correspondente a este número. 
### Isto é, domingo equivale a 1, segunda-feira se 2, e assim por diante.


numero = int(input("Digite um numero entre 1 e 7: "))


if numero == 1:
    print("domingo")
elif numero ==2:
    print("segunda-feira")
elif numero == 3:
    print("terça-feira")
elif numero == 4:
    print("quarta-feira")
elif numero == 5:
    print("quinta-feira")
elif numero == 6:
    print("sexta-feira")
elif numero == 7:
    print("sábado")
else:
    print("número inválido")
