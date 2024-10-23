#Realiza un programa que controle si la longitud de una frase introducida por teclado es
#igual, menor o mayor de 11 caracteres. Utiliza elif
frase=input("Introduce una frase: ")
long=len(frase)
if long==11:
    print("La frase tiene 11 caracteres.")
elif long>11:
    print("La frase tiene 11 o más caracteres.")
else:
    print("La frase tiene menos de 11 caracteres.")