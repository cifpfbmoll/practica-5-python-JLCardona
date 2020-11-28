from os import system
system("cls")
print ("Escala SUMA")
n1 = int(input("1er número : "))
n2 = int(input("2o número MAYOR que el primero : "))
list = []
suma = 0
if n2 <= n1 :
    print ("ERROR: El 2o número debe ser MAYOR que el 1o")
else:
    for i in range(n1,n2 +1):
        list = [i]
        suma = suma + i
    print ("Esta es la suma : ",suma)