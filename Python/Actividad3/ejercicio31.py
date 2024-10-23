#Asigna a una variable de texto la siguiente frase: A quién madruga Dios ayuda. 
#Comprueba si existen las siguientes palabras mostrando por pantalla la posición de su 
#índice
frase="A quién madruga Dios ayuda."
a=frase.find(input("Palabra que quiere encontrar: "))
if a>=1:
    print("La palabra está en la frase y está en el índice",a)
else:
    print("La palabra no está en la frase")