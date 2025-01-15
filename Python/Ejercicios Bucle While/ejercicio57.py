#57. Realiza un programa que permita adivinar un número comprendido entre 1 y 5. El programa 
#debe controlar si el usuario introduce un número no comprendido entre 1 y 5
import random
a=random.randint(1,5)
b=input("Introduzca un número: ")
while b.isnumeric()==False:
    b=input("El valor introducido no es un número, por favor reintroduzca el valor: ")
b=int(b)
if b==a:
    print("Número acertado")
else:
    print("Número no acertado")