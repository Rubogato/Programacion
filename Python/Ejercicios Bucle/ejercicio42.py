#42. Imprima el siguiente patrón con el ciclo for.
a="*"
b=""
c=0
d=0
for x in range(8+1):
    if c<5:
        c+=1
        b=b+a
        print(b)
    else:
        d+=1
        b=b[0:5-d]
        print(b)
        