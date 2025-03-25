var=input("Introduce los valores: ")
lista=var.split("-")
lista2=[]
lista3=[]
contador=0
lista4=[]
lista5=[]
for x in lista:
    if x.isalpha():
        lista3.append(x)
    else:
        if x.isnumeric():
            lista2.append(int(x))
        else:
            lista2.append(float(x))
print(f"""Valores numéricos antes de eliminar duplicados:
{lista2}""")
total=sum(lista2)
print("Suma total antes de eliminar duplicados:",total)
lista2.sort()
for y in lista2:
    contador=contador+1
    if not y==lista2[contador-2]:
        lista4.append(y)
print(f"""Valores numéricos después de eliminar duplicados:
{lista4}""")
total2=sum(lista4)
print("Suma total después de eliminar duplicados:",total2)
print(f"""Valores no numéricos antes de eliminar duplicados:
{lista3}""")
a=set(lista3)
for x in a:
    lista5.append(x.upper())
print("Valores no numéricos después de eliminar duplicados:",lista5)