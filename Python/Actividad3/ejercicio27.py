#Mejora el programa anterior para controlar que el valor introducido es una letra y en 
#caso de introducir un número, aparezca un aviso por pantall
a=input("Introduce una letra: ")
if a.isalpha():
    if a.isupper()==True:
        print("La letra es mayúscula")
    else:
        print("La letra es minúscula")
elif a.isnumeric():
    print("El valor introducido es un número")
else:
    print("La letra es mayúscula ¿?")