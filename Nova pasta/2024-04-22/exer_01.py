### 1. Considere a=0, b=2 e c=1.
### O que será impresso pelos comandos abaixo?
### (Primeiro ajuste corretamente a indentação).

a= int(input("o valor do A é: "))
b= int(input("o valor do B é: "))
c= int(input("o valor do C é: "))

if( a > 0):
    if(b > 0):
        print("Tudo ok para decolagem!")
    else:
        print("tanque principal vazio; voando com combustivel reserva!")
else:
    if(c > 0):
        print("Foguete não tem piloto, mas há outros foguetes disponíveis!")   
