#45. Realiza un programa que permita introducir una palabra por teclado y puedas recorrer el string
#distinguiendo vocales y las consonantes:
pal=input("Introduce una palabra: ")
voc=""
con=""
for x in range(0,len(pal)):
    let=pal[x]
    if let=="a" or let=="e" or let=="i" or let=="o" or let=="u":
        voc=voc+let
    else:
        con=con+let
print("Las vocales de la palabra abrigo son:",voc)
print("Las consonantes de la palabra abrigo son:",con)