var=input("Introduce una secuencia de números: ")
lista=var.split("-")
total=0
lista3=[]
lista2=[]
for x in lista:
    total=total+int(x)
    lista2.append(int(x))
media=round(total/len(lista),4)
for y in lista2:
    if y>media:
        lista3.append(int(y))
print("Máximo:",max(lista2))
print("Mínimo:",min(lista2))
print("Promedio:",media)
print("Nueva lista:",lista3)