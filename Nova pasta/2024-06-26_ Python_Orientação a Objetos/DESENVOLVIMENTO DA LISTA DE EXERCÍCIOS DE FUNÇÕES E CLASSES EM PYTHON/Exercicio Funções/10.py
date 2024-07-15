# 10

def media(num1, num2, num3, letra):
    if letra == "A":
        print(f"Media aritimetica: {(num1 + num2 + num3) / 3}")
    elif letra == "P":
        print(f"Media ponderada: {(5*num1 + 3*num2 + 2*num3) / (5+3+2)}")

media(5,3,2,"A")
media(5,3,2,"P")