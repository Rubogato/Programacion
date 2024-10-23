#Cómo solucionarías con ayuda de métodos String el problema del ejercicio anterior para 
#no distinguir entre mayúsculas y minúsculas
frase="A quién madruga Dios ayuda."
b=input("Palabra que quiere encontrar: ")
a=frase.find(b)
if a>=1:
    print("La palabra está en la frase y está en el índice",a)
frase=frase.lower() 
a=frase.find(b)
if a>=1:
    print("La palabra está en la frase y está en el índice",a)
else:
    print("La palabra no está en la frase")