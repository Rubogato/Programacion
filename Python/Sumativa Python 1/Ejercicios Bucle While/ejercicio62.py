#62. Realiza un programa que pida dos números por teclado y presente por pantalla qué números 
#hay pares e impares en ese rango. Utiliza for. Contempla si primer valor es superior al segundo.
par=""
impar=""
a=int(input("Introduce un valor: "))
b=int(input("Introduce otro valor: "))
if a>b:
    mayor=a
    menor=b
else:
    mayor=b
    menor=a
for var in range(menor,mayor):
    x=var%2
    num=str(var)+"-"
    if x==0:
        par=par+num
    else:
        impar=impar+num
print("Los números pares son: ",par[0:len(par)-1])
print("Los números impares son: ",impar[0:len(impar)-1])