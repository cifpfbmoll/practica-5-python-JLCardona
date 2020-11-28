from os import system
system("cls")
altura = int (input ("Dame la altura del triángulo : "))

for i in range (1, altura+1):
    for j in range (altura - i):
        print (" ", end = "")
    for j in range (1, 2 * i):
        print ("*", end = "")
    print ()