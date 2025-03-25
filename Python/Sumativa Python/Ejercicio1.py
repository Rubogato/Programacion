#He añadido floats para que pueda poner decimales, porque input solo deja introducir texto
var_1=float(input("Introduce el primer número: "))#No se pueden poner espacios en las variables
#Faltaban las comillas
var_2=float(input("Introduce el segundo número: "))
#No se puede poner espacios en las variables y faltan "_"en las variables
var_total=var_1+var_2
#Falta la coma cuando en el print cuando pasa de texto a variable
#El total no está designado, hay que poner var_total
#No hay que poner una coma con el "f"
#Para poner variables hay que cambiar de texto a variable
print(f"El resultado de sumar",var_1,"y",var_2,"es:",var_total)
