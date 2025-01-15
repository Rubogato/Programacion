#63. Realiza un programa que permita tirar 100 veces un dado y nos presente por pantalla el número
#de veces que se repite cada número.
import random
cont=1
a=0
b=0
c=0
d=0
e=0
f=0
while cont<=100:
    cont+=1
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
print("Uno:",a)
print("Dos:",b)
print("Tres:",c)
print("Quatro:",d)
print("Cinco:",e)
print("Seis:",f)