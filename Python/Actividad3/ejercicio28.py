# Mejora el programa anterior para controlar también la introducción de símbolos. Utiliza 
#elif.
a=input("Introduce una letra: ")
if a.isalpha():
    if a.isupper()==True:
        print("La letra es mayúscula")
    else:
        print("La letra es minúscula")
elif a.isnumeric():
    print("El valor introducido es un número")
else:
    print("El valor introducido es un símbolo")