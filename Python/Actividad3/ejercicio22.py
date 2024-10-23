#Programa que al introducir una nota por teclado te diga si has aprobado o suspendido. 
#Si la nota es menos de un 5 es suspenso y si la nota es 5 o mayor estás aprobado.
nota=float(input("Introduce tu nota: "))
if nota>0 and nota<10:
    if nota>=5:
        print("Has sacado un",nota,"y has aprobado")
    else:
        print("Has sacado un",nota,"y has suspendido")
else:
    print("La nota que has introducido no está entre 0 y 10")