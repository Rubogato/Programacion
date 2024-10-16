#Calcula el índice de masa corporal IMC de una persona, introduciendo por teclado el 
#peso (en kg) y dividiendo por la estatura (en metros y elevado al cuadrado). Si el resultado 
#es igual o superior a 25, debe aparecer un mensaje informando de sobrepeso
kg=float(input("Dime cuántos kilogramos pesas: "))
alt=float(input("Dime cuánto mides en metros: "))
IMC=round(kg/(alt**2),2)
if IMC >= 25:
    print("Si pesas",kg,"y mides",alt,",tu IMC es: ",IMC,"y tienes sobrepeso")
else:
    print("Si pesas",kg,"y mides",alt,",tu IMC es: ",IMC)
