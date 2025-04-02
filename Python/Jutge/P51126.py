inter=[]
intervalo=input()
lista=intervalo.split()
min1=int(lista[0])
max1=int(lista[1])
min2=int(lista[2])
max2=int(lista[3])
if max1<min2 or min1>max2:
    print("[]")
else:
    if min1>=min2:
        inter.append(min1)
    elif min2>=min1:
        inter.append(min2)
    if max1>=max2:
        inter.append(max2)
    elif max2>=max1:
        inter.append(max1)
    a=inter[0]
    b=inter[1]
    print(f"[{a},{b}]")