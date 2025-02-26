#83. Modifica el código del ejercicio anterior para que el programa permita repetir x partidas (hasta 
#que el usuario lo decida). Tienes que controlar una puntuación de cada partida de la siguiente 
#manera, si la palabra la aciertas a la primera son 8 puntos, si la aciertas a la segunda 7 puntos y así 
#sucesivamente.
#Una vez el usuario desea finalizar el programa tiene que sumar todas tus puntuaciones obtenidas. 
#Si el total supera la media de la puntuación posible de todas las partidas, se puede decir que la 
#suerte le acompaña, de lo contrario mejor no Se dediques a los juegos de azar . PISTA.. ¿existe 
#algún método que permita sumar el contenido de una lista?
import random
lista=["casa","barco","gato","perro","madera","agua","puente","pantalón"]
cond="s"
puntuacion=[]
print("Estas son las palabras que pueden ser escogidas:",lista)
while cond=="s":
    rwg=random.choice(lista)
    a=0
    p=0
    while a==0:
        palabra=input("Introduce una palabra: ")
        p=p+1
        if palabra==rwg:
            a=1
            print("ACERTASTE")
        else:
            print("SIGUE JUGANDO")
    puntos=9-p
    puntuacion.append(puntos)
    cond=input("Quieres repetir la partida? s/n: ")
total=sum(puntuacion)
media=len(puntuacion)*4
print(f"""PUNTUACIÓN {puntuacion}
Tu puntuación ha sido de {total}
La media las partidas realizadas es: {media}""")
if total>media:
    print("Tienes buena suerte")
else:
    print("Dedícate al parchís")