y=0
while y==0:
    num=input()
    lista=num.split()
    x=int(lista[0])
    y=int(lista[1])
div=x//y
res=x%y
print(div,res)