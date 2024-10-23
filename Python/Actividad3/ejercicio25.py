#Repite el programa número 23 pero en esta ocasión utilizando operadores lógicos.
nota=float(input("Introduce tu nota: "))
if nota>0 and nota<10:
    if nota<5:
        print("Has sacado un",nota,"y tienes un insuficiente")
    elif nota>5 and nota<6.5:
        print("Has sacado un",nota,"y tienes un suficiente")
    elif nota>=6.5 and nota<8.5:
        print("Has sacado un",nota,"y tienes un notable")
    else:
        print("Has sacado un",nota,"y tienes un excelente")
else:
    print("La nota que has introducido no está entre 0 y 10")