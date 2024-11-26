#47. Realiza un programa donde el usuario introduzca por teclado 2 intervalos, por pantalla se debe 
#mostrar el rango de números teniendo en cuenta que se a<b la secuencia será incremental y si a>b 
#la secuencia en descenso. Respeta el formato de salida
var=0
var2=""
var3=""
ter1=int(input("Introduce el primer intervalo: "))
ter2=int(input("Introduce el segundo intervalo: "))
if ter1<ter2:
    a=ter2
    b=ter1
else:
    a=ter1
    b=ter2
for x in range(b,a+1):
    var=str(x)
    var2=var2+var+"-"
if ter1>ter2:
    for y in range(1,len(var2)+1):
        var3=var3+var2[-y]
if ter1<ter2:
    print(var2[0:len(var2)-1])
else:
    print(var3[1:len(var2)+1])