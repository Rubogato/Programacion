kg=float(input("Dime cuántos kilogramos pesas: "))
alt=float(input("Dime cuánto mides en metros: "))
IMC=round(kg/(alt**2),2)
if IMC >= 25:
    print("Si pesas",kg,"y mides",alt,",tu IMC es: ",IMC,"y tienes sobrepeso")
else:
    print("Si pesas",kg,"y mides",alt,",tu IMC es: ",IMC)
