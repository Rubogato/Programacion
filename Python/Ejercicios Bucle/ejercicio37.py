#37. Programa que pregunte cuantas notas quiero introducir y para cada nota diga si estoy aprobado 
#o suspendido.
rep=int(input("Introduce el número de notas que deseas introducir "))
for contador in range(0,rep+1):
    nota=int(input("Introduce la nota: "))
    if nota<5:
        print("Asignatura suspendida")
    else:
        print("Asignatura aprobada")