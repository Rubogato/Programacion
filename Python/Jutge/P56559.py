inter=[]
intervalo=input()
lista=intervalo.split()
min1=int(lista[0])
max1=int(lista[1])
min2=int(lista[2])
max2=int(lista[3])
if min1==min2 and max1==max2:
    print("=")
elif min1<=min2 and max1>=max2:
    print("2")
elif min2<=min1 and max2>=max1:
    print("1")
else:
    print("?")