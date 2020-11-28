from os import system
system("cls")
numero = int (input ("Dame un número y te diré todos sus divisores : "))
for i in range (numero + 1):
    if ((i!=0) and (numero % i==0)):
        print(i , end = " ")