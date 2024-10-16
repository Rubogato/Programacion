#A partir del ejercicio anterior, forzar que el usuario solo pueda introducir por teclados 
#números entre 0 y 10
var1=int(input("Dame un valor: "))
var2=int(input("Dame otro valor: "))
if var1<10 and var2<10 and var1>0 and var2>0:
    if var1>var2:
        print("El número",var1,"es mayor al número",var2)
    elif var1<var2:
        print("El número",var2,"es mayor al número",var1)
    else:
        print("Los dos números son iguales")
else:
    print("Uno o los dos números están fuera de los límites establecidos")