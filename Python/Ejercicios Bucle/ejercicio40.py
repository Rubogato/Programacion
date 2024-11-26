#40. Crea un programa que cuente todos los números pares hasta el número 50
num=50
par=0
imp=0
for contador in range(1,50+1):
    div=contador%2
    if div==0:
        par=par+1
    else:
        imp=imp+1
print("El total de pares es:",par)
print("El total de impares es:",imp)