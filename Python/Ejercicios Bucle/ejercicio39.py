#39. Programa que pida n números y que, tras introducir el último número, debe aparecer por 
#pantalla el número total de positivos, negativos y número de 0.
neg=0
pos=0
cer=0
n=int(input("Introduce la cantidad de números que deseas introducir: "))
for contador in range(0,n+1):
    var1=int(input("Introduce un número: "))
    if var1<0:
        neg=neg+1
    elif var1>0:
        pos=pos+1
    else:
        cer=cer+1
print("La cantidad de números positivos es:",pos)
print("La cantidad de números negativos es:",neg)
print("La cantidad de ceros es:",cer)