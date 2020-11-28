from os import system
system("cls")
print ("Escala PAR - IMPAR")
num1 = int(input("1er número : "))
num2 = int(input("2o número MAYOR que el primero : "))
if num2 < num1 :
    print ("ERROR: El 2o número debe ser MAYOR que el 1o")
else:
    for i in range(num1,num2 +1):
        if i % 2 == 0:
            print ("El número ",i," es PAR")
        else:
            print ("El número ",i," es IMPAR")
