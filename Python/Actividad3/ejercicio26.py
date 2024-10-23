# Realiza un programa que, al introducir una letra por teclado, aparezca por pantalla si 
#está o no en mayúscula. Utiliza dos IF’s que establezcan True o False a la condición
a=input("Introduce una letra: ")
if a.isalpha():
    if a.isupper()==True:
        print("La letra es mayúscula")
    else:
        print("La letra es minúscula")
else:
    print("La letra es mayúscula ¿?")