#80. Utilizando listas, crea un programa que te permita determinar si un número es decimal o no.
numero=input("Introduce un número: ")
lista=[]
lista=numero.split(".")
contador=0
for x in lista:
    if x.isnumeric():
        contador=contador+1
if contador==2:
    print("Es un número con decimales")
else:
    print("No es un número con decimales")