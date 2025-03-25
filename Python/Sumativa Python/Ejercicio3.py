#he importado los ficheros math, para poder usar los operadores math
import math
#En la siguiente parte he usado el comando int, para convertir el valor de input en numero entero, pero también se puede usar float
lado=int(input("Introduce el valor de un lado: "))
#El comando math.sqrt hace la raíz cuadrada del número dentro del paréntesis
#El comando round redondea el valor a la izquierda de la coma con el número de decimales que se especifica a la derecha de la coma
area=round(math.sqrt(3)/4*lado**2,2)
#"**" este es el operador de exponente o potencia
print(area)
