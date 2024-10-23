#Corrige los 4 errores o añade el código que necesites para que el siguiente programa se 
#ejecute correctamente

var_numero="6734"
var_suma=0
var_longitud=len(var_numero)


a=int(var_numero[0])
b=int(var_numero[1])
c=int(var_numero[2])
d=int(var_numero[3])
var_suma=a+b+c+d

a=var_suma%2
if a==0:
    print (f"el valor de {var_suma} es impar")