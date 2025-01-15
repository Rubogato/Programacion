#58. Modifica el programa anterior para que tengas 3 intentos. Utiliza while
import random
cont=0
a=random.randint(1,5)
while cont<3:
    cont=cont+1
    b=input("Introduzca un número: ")
    while b.isnumeric()==False:
        b=input("El valor introducido no es un número, por favor reintroduzca el valor: ")
    b=int(b)
    if b==a:
        print("Número acertado")
        break
    else:
        print("Número no acertado")