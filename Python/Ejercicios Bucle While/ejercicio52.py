#52. Realiza un programa que sume dos números enteros por teclado y presente el resultado por 
#pantalla. El programa preguntará si deseas o no repetir la operación. Con While
cond="s"
while cond=="s":
    var=int(input("Introduce un número: "))
    var1=int(input("Introduce otro número: "))
    total=var+var1
    print("El resultado de la suma es:",total)
    cond=input("Deseas repetir la operación s/n: ")
else:
    print("Programa finalizado")