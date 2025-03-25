concatenar=""
palabra=input()
lista=palabra.split()
for x in lista:
    concatenar=x+" "+concatenar
print(concatenar[:-1])