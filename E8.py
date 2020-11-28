from os import system
system("cls")
anchura = int ( input ("Dame la anchura del triángulo : "))

for i in list (range (1 , anchura) ) + list ( range (anchura , 0 , -1)):
    for j in range (i):
        print ("* ", end = "")
    print ()