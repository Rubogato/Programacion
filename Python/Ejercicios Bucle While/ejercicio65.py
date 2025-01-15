#65. Programa que pida continuamente números por teclado hasta que el usuario introduzca el valor 
#-99. Por pantalla debe aparecer cuál de todos los números introducidos es el mayo y cuál el menor
valor=int(input("Introduce un número: "))
mayor=0
menor=0
valor1=0
valor1=int(input("Introduce otro número: "))
if valor>valor1:
    mayor=valor
    menor=valor1
elif valor1>valor:
    mayor=valor1
    menor=valor
while not valor==-99:
    valor1=int(input("Introduce otro número: "))
    if valor1==-99:
        break
    if valor1>mayor:
        mayor=valor1
    if valor1<menor:
        menor=valor1
print(f"El mayor número introducido es {mayor} y el menor es {menor}")