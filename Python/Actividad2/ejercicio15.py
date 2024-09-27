import math
rad=int(input("Dame el valor del radio: "))
alt=int(input("Dame el valor de la altura: "))
pi=math.pi
area=round(2*pi*rad*(rad+alt),2)
volumen=round(pi*rad**2*alt,2)
print("El area del cilindro es: ",area)
print("El volumen del cilindro es: ",volumen)
