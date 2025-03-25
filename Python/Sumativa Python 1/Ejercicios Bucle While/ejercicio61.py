#61. A partir del c—digo anterior, haz que el programa finalice si el valor de la tabla de multiplicar es
#superior o igual a 40
cont=0
var=int(input("Introduce un nœmero: "))
while cont<10:
    cont=cont+1
    mult=var*cont
    if mult>40:
        print("Fin del programa")
        break
    print(mult)