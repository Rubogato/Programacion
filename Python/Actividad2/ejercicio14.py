#Realiza un programa que a partir de introducir el diámetro de un círculo calcule el área 
#y perímetro. Importa la librería match y utiliza el valor PI para hacer el cálculo. Redondea el 
#resultado a un decimal
import math
dia=int(input("Dime el diámetro del círculo: "))
rad=dia/2
pi=math.pi
area=round(pi*(rad**2),1)
peri=round(2*pi*rad,1)

print("El perímetro del círculo es: ",peri)
print("El área del círculo es. ",area)
