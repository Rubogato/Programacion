#85. Te piden realizar un programa en que gestionen la media y la mediana de varias de tres 
#asignaturas de legua: catalán, inglés y castellano. Una vez introducidos varios registros el 
#programa debe mostrar la media y mediana los todos los alumnos introducidos
cond="s"
ingles=[]
caste=[]
cata=[]
a=0
while cond=="s":
    input("Introduce estudiante: ")
    i=float(input("Nota inglés: "))
    cas=float(input("Nota castellano: "))
    cat=float(input("Nota catalán: "))
    ingles.append(i)
    caste.append(cas)
    cata.append(cat)
    a=a+1
    cond=input("Deseas introducir otro alumno s/n: ")
mi=round(sum(ingles)/a)
mc=round(sum(caste)/a)
mca=round(sum(cata)/a)
ingles.sort()
caste.sort()
cata.sort()
if a%2==1:
    b=int((a/2)+0.5-1)
    mei=ingles[b]
    mec=caste[b]
    meca=cata[b]
else:
    b=int((a/2))
    c=int((a/2)-2)
    mei=round((ingles[b]+ingles[c])/2,2)
    mec=round((caste[b]+caste[c])/2,2)
    meca=round((cata[b]+caste[c])/2,2)
print(f"""Inglés: {ingles}
Castellano: {caste}
Catalán: {cata}

La media en inglés es: {mi}
La media en castellano es: {mc}
La media en catalán es: {mca}
La mediana en inglés es: {mei}
La mediana en castellano es: {mec}
La mediana en catalán es: {meca}""")