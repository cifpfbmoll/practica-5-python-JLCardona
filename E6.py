from os import system
system("cls")
print ("Dame la altura de un triángulo : ")
altura = int ( input ("Altura : "))
for i in range(altura):
    for j in range(i + 1):
        print ("*" , end = " ")
    print ()