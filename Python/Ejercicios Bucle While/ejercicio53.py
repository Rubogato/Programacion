#53. A partir del código anterior, haz que aparezca al finalizar el programa por pantalla el total las 
#sumas y el número de repeticiones. Con While
cond="s"
suptotal=0
rep=0
while cond=="s":
    rep=rep+1
    var=int(input("Introduce un número: "))
    var1=int(input("Introduce otro número: "))
    total=var+var1
    print("El resultado de la suma es:",total)
    suptotal=suptotal+total
    cond=input("Deseas repetir la operación s/n: ")
else:
    print("Mensaje: 'Resumen:'")
    print("La suma total es:",suptotal,"y el número de repeticiones es:",rep)