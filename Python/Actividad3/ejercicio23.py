#Modifica el programa anterior para establecer si la nota es un excelente (8.5 a 10), un 
#notable (>=6.5 -<8.5), satisfactorio (<6.5 -5) o insuficiente (<5). Controla que la nota 
#introducida esté entre 0 y 10. Utilizar elif sin operadores lógicos.
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