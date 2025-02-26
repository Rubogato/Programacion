#84. A partir de la lista definida en el ejercicio 81, haz que se visualice por pantalla una de las 
#palabras, pero con todas sus letras desordenadas. El usuario tendrá que recolocar y acertar la 
#palabra secreta. El usuario tendrá 3 oportunidades para adivinar la palabra
import random
a=0
palabra=""
lista=["casa","barco","gato","perro","madera","agua","puente","pantalón"]
rwg=random.choice(lista)
lista2=[]
for x in rwg:
    lista2.append(x)
random.shuffle(lista2)
print(lista2)
while a<3 and not palabra==rwg:
    palabra=input("Introduce una palabra: ")
    a=a+1
    if palabra==rwg:
        print("Acertaste")
    else:
        print("no has acertado")
else:
    if not a<3:
        print("no has acertado ninguno de los intentos")