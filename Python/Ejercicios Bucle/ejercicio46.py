#46. A partir del programa anterior, soluciona el error que se produce en el test anterior con la 
#palabra Abrigo utilizando únicamente una instrucción.
pal=input("Introduce una palabra: ")
voc=""
con=""
for x in range(0,len(pal)):
    let=pal[x].lower()
    if let=="a" or let=="e" or let=="i" or let=="o" or let=="u":
        voc=voc+let
    else:
        con=con+let
print("Las vocales de la palabra abrigo son:",voc)
print("Las consonantes de la palabra abrigo son:",con)