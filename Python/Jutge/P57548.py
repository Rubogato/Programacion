num=input()
total=0
lista=num.split()
if len(lista)==1:
    num2=input()
    total=int(num)+int(num2)
    print(total)
else:
    for x in lista:
        var=int(x)
        total=total+var
    print(total)