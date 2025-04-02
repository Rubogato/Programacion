year=input()
lista=[]
for x in year:
    lista.append(x)
var1=int(lista[0]+lista[1])
var2=int(lista[2]+lista[3])
if not var2==0:
    if var2%4==0:
        print("YES")
    else:
        print("NO")
else:
    if var1%4==0:
        print("YES")
    else:
        print("NO")