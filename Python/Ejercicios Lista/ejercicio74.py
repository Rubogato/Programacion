#74. A partir del programa anterior, haz que se visualicen tanto las palabras que se repiten o no de 
#entre las 2 listas.
lista1=["casa","mesa","sal","sol","agua"]
lista2=["casa","luz","tres","tren","sol","pan"]
rep=[]
norep=[]
for x in lista2:
    if lista1.count(x)==1:
        rep.append(x)
    else:
        norep.append(x)
for  in lista1:
    if lista1.count(x)==1:
        rep.append(x)
    else:
        norep.append(x)
print("Palabras repetidas",rep)
print("Palabras no repetidas",norep)