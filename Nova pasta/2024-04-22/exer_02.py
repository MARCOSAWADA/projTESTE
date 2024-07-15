### 2.

temp = int(input("Qual é a temperatura neste exato momento: "))

if(temp > 28):
    print("Esta calor")
elif(temp <= 28 and temp >= 14):
    print("Está agradável")
else:
    print("Está frio")