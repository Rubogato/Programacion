#77. A partir de la lista del enunciado anterior, haz que el programa visualice por un lado las letras 
#y por otro los números permitiendo escoger orden ascendente o descendente. Como observarás 
#en la salida, el orden de las letras no es correcto, busca la manera de solucionarlo
lista=["a","b","D","x","r","X","3","h","w","2","i"]
num=[]
letra=[]
var=int(input("Introduce 1 para visualizar en orden ascendente o 2 descendente: "))
for x in lista:
    if x.isalpha():
        letra.append(x.lower())
    else:
        num.append(int(x))
if var==1:
    letra.sort()
    num.sort()
else:
    letra.sort(reverse=True)
    num.sort(reverse=True)
print(num)
print(letra)