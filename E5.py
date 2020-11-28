from os import system
system("cls")
print ("Dame las medidas de un rectángulo y mira la mágia : ")
altura = int ( input ("Altura : "))
anchura = int ( input ("Anchura : "))
for i in range(altura):
    for j in range(anchura):
        print ("*" , end = " ")
    print()