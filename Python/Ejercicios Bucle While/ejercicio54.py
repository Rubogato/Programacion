#54. Modifica el programa anterior y haz que se repita el ciclo automáticamente hasta que el total 
#de todas las sumas sea superior a 50, será entonces cuando el programa finalice. No hará falta 
#preguntar si deseas repetir la operación. En cada operación aparece por pantalla la suma de la 
#operación y su acumulado. Para aquellos de vosotros que os fijáis en los detalles, controlar que el 
#mensaje del acumulado es singular o plural.. . Con While
total=0
rep=0
while total<50:
    rep=rep+1
    var=int(input("Introduce un número: "))
    var1=int(input("Introduce otro número: "))
    suma=var+var1
    print("El resultado de la suma es:",suma)
    total=total+suma
    print("El total acumulado es",total,"y llevas",rep,"operaciones relacionadas")
else:
    print("Mensaje: 'Fin del programa'")