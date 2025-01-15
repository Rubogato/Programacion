#66. Repite el ejercicio 63. En lugar de ‘tirar’ 100 veces un dado, modifica el programa para ver cómo 
#se comporta el dado en lanzamientos producidos durante aprox 3 segundos.
import random
import time
tiempo=0
a=0
b=0
c=0
d=0
e=0
f=0
x=time.time()
while tiempo<=3:
    tiempo=time.time()-x
    valor=random.randint(1,6)
    if valor==1:
        a=a+1
    elif valor==2:
        b=b+1
    elif valor==3:
        c=c+1
    elif valor==4:
        d=d+1
    elif valor==5:
        e=e+1
    else:
        f=f+1
print(f"""RESUMEN
Tiempo: {tiempo}
Uno: {a}
Dos:{b}
Tres: {c}
Cuatro: {d}
Cinco: {e}
Seis: {f}""")