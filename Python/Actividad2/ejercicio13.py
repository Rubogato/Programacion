#Realiza un programa que, a partir introducir el lado de un cubo, presente por pantalla el 
#área y para calcular el volumen utiliza el operador de exponente.
lado=int(input("Dime cuánto mide un lado del cubo: "))
area=lado**2*6
volumen=lado**3
print("El área del cubo es: ",area)
print("El volumen del cubo es: ",volumen)
