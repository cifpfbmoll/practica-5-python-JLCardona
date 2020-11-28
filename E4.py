from os import system
system("cls")
print ("Dame un número y calcularé su factorial : ")
cálculo = int (1)
num = int ( input ("Número : "))
for i in range(1, num + 1):
    cálculo = cálculo * i
print("El factorial de " , i ," es " , cálculo)
