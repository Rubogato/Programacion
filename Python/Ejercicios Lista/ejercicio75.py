#75. Crea una lista con el siguiente nombre lista1 y su contenido: a,b,D,x,r,X,3,h,w,2,i. Presenta por 
#pantalla los siguientes resultados:
#a. Cantidad total de valores
#b. Cantidad de números
#c. Cantidad de letras
#d. Cantidad de mayúsculas
#e. Suma de los valores numérico
lista=["a","b","D","x","r","X","3","h","w","2","i"]
mayus=0
minus=0
letra=0
num=0
lista2=[]
for x in lista:
    if x.isalpha():
        letra=letra+1
        if x.isupper():
            mayus=mayus+1
        else:
            minus=minus+1
    else:
        num=num+1
        lista2.append(int(x))
var=sum(lista2)
lon=len(lista)
print(f""" Hay una cantidad de {lon} de valores de los cuales son:
{letra} letras, {mayus} mayúsculas.
{minus} minúsculas y {num} números
y la suma de los números es {var}""")