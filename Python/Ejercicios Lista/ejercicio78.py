#78. A partir de la lista definida en el ejercicio 75, haz que el programa pregunte qué valor se desea 
#eliminar de la lista, siendo únicamente los números los valores permitidos para suprimir
lista=["a","b","D","x","r","X","3","h","w","2","i"]
x="s"
while x=="s":
    var=input("Introduce el valor que desea eliminar: ")
    if var.isnumeric():
        if var in lista:
            lista.remove(var)
            print(lista)
        else:
            print("El valor no está en la lista")
    else:
        print("Introduce un valor numérico")
    x=input("Desea introducir otro valor? s/n: ")