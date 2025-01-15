#55. Última vez que reutilizamos el mismo código.. lo prometo . A partir del programa anterior 
#haz que sea todo exactamente igual pero teniendo en cuenta que el programa se repita siempre y 
#cuando la suma acumulada sea superior a 50 o la suma acumulada sea par. Con While
total=0
rep=0
var=0
while total<50 or var==0:
    rep=rep+1
    var=int(input("Introduce un número: "))
    var1=int(input("Introduce otro número: "))
    suma=var+var1
    print("El resultado de la suma es:",suma)
    total=total+suma
    print("El total acumulado es",total,"y llevas",rep,"operaciones relacionadas")
    var=total%2
else:
    print("Mensaje: 'Fin del programa'")