#38. A partir del programa anterior, establece los rangos para que el usuario no pueda introducir 
#notas inferiores a 0 y superiores a 10
rep=int(input("Introduce el número de notas que deseas introducir: "))
for contador in range(0,rep+1):
    nota=int(input("Introduce la nota: "))
    if nota>=0 and nota<=10:
        if nota<5:
            print("Asignatura suspendida")
        else:
            print("Asignatura aprobada")
    else:
        print("Has introducido una nota equivocada")