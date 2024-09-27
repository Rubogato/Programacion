import math
dia=int(input("Dime el diámetro del círculo: "))
rad=dia/2
pi=math.pi
area=round(pi*(rad**2),1)
peri=round(2*pi*rad,1)

print("El perímetro del círculo es: ",peri)
print("El área del círculo es. ",area)
