#64. Programa que pida continuamente números por teclado hasta que el usuario introduzca el valor 
#-99. Será entonces cuando por pantalla aparecerán las siguientes estadísticas:
#a) total de pares
#b) total de impares
#c) total de números positivos
#d) total de números negativos
#e) total de ceros
#f) total de la suma de todos los números introducidos
neg=0
pos=0
cero=0
par=0
imp=0
total=0
valor=int(input("Introduce un número: "))
while not valor==-99:
    a=valor%2
    if a==0:
        par=par+1
    else:
        imp=imp+1
    if valor<0:
        neg=neg+1
    elif valor>0:
        pos=pos+1
    else:
        cero=cero+1
    total=total+valor
    valor=int(input("Introduce otro número: "))
print(f"""RESUMEN
      El número de pares es: {par}
      El número de impares es: {imp}
      El número de positivos es: {pos}
      El número de negativos es: {neg}
      El número de ceros es: {cero}
      El total es {total}""")