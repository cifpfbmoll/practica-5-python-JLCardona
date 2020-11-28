from os import system
system("cls")
anchura = int ( input ("Dame la anchura del rectángulo : "))
altura = int(input("Dame la altura del rectángulo : "))

for i in range (anchura):
    print ("* ", end = "")
print ()

for i in range (altura - 2):
    print ("* ", end = "")
    for j in range(anchura - 2):
        print ("  ", end = "")
    print ("*")

for i in range(anchura):
    print ("* ", end = "")