dividendo= float(input("Escribe el dividendo: "))
cuociente= int(input("Escribe otro numero: "))
Total= dividendo//cuociente
resto= dividendo%cuociente
print("El cociente es: ", Total)
print("El resto es: ", resto)
round(resto,0)
if resto==0:
    print("El dividendo es par")
else:
    print("El dividendo es impar")

