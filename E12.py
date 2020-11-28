from os import system
system("cls")
numero = int (input ("Dame un número y te diré si es primo o no : "))
esPrimo = True
for i in range (numero):
    if ((i!=0) and (i!=1) and (numero % i==0)):
        esPrimo = False
if (esPrimo):
    print ("El ",numero," SÍ es un número primo :)")
else:
    print ("El ",numero," NO es un número primo :(")