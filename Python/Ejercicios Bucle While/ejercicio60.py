#60. Diseña un programa que al introducir un número, realice su tabla de multiplicar del 1 al 10. 
#Utiliza únicamente el while
cont=0
var=int(input("Introduce un número: "))
while cont<10:
    cont=cont+1
    mult=var*cont
    print(mult)