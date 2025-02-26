#71. Haz un programa que permita al usuario introducir letras en una lista (cantidad indefinida), en 
#esta lista no deben almacenarse las letras que se han introducido repetidas.
x="s"
lista=[]
while x=="s":
    letra=input("Introduce una letra: ")
    while not letra.isaplha():
        letra=input("Introduce otra letra: ")
    var=lista.count(letra)
    if letra.isalpha() and var==0:
        lista.append(letra)
    x=input("Quieres repetir? s/n: ")
print(lista)