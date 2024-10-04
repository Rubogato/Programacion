var1=int(input("Introduce el primer valor: "))
var2=int(input("Introduce el segundo valor: "))
#"//" es el operador de la división entera, que devuelve el número entero de la división
#Es decir, hace que la división no sea exacta
divent=var1//var2
#% este es el operador de módulo, que te da el resto de la división
res=var1%var2
#** este es el operador de exponente o potencia. La variable a la izquierda es la base y el de la derecha el exponenete
multi=var1**var2
print("El resultado de la división entera es:",divent)
print("El resultado del módulo es:",multi)
print("El resultado de la potencia es:",res)
