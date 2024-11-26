# 43. Realiza un programa que recorra con un for una palabra introducida por teclado y se imprima 
#por pantalla cada letra
var=input("Introduce una palabra: ")
a=-1
for x in var:
    a+=1
    print(f"En la posición {a} está la",x)
    