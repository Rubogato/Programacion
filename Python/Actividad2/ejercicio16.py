#Utiliza el método sqrt de la librería math para calcular la raíz cuadrada de un número. El 
#resultado de la raíz cuadrada divídelo entre 2 de manera que se obtenga siempre un 
#resultado entero. Haz que se muestre por pantalla los dos resultados de todo el proceso
#(raíz y división).
import math
valor1=int(input("Dame un valor: "))
rz=round(math.sqrt(valor1))
div=round(rz/2)
print("El resultado de la raíz es: ",rz)
print("EL resultado de la división es: ",div)
