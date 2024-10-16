# Programa que calcula una ecuación de segundo grado. Controla que el valor de la raíz 
#cuadrada no de un valor negativo
import math
a=int(input("Introduce el primer valor: "))
b=int(input("Introduce el siguiente valor: "))
c=int(input("Introduce el último valor: "))
raíz=b**2-4*a*c
if raíz<0:
    print("No hay solución")
else:
    total1=(-b+math.sqrt(raíz))/2*a
    total2=(-b-math.sqrt(raíz))/2*a
    print("El primer resultado es:",total1)
    print("El segundo resultado resultado es:",total2)