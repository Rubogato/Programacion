#59. Diseña un programa que “piense” un numero aleatorio entre 0 y 1000 para que nos pida que 
#intentemos adivinarlo. En cada intento, el programa nos dirá si el numero introducido es mayor o 
#menor del correcto. No utilices break para salir del bucle. Cuando se acierte el número debe 
#mostrarse por pantalla un mensaje y el número de intentos.
import random
b=0
tries=0
a=random.randint(1,1000)
while not a==b:
    tries=tries+1
    b=input("Introduce un valor comprendido entre 1 y 1000: ")
    while b.isnumeric()==False:
        b=input("El valor introducido no es un número, por favor reintroduzca el valor: ")
    b=int(b)
    if b<a:
        print("El número que has introducido es menor")
    elif b>a:
        print("El número que has introducido es mayor")
print("Acertaste, has realizado",tries,"intentos")