num=input()
total=0
lista=num.split()
valor=""
if len(lista)==2:
    for x in lista:
        var=int(x)
        total=total+var
    while valor.isnumeric()==False:
        valor=input()
    else:
        valor1=int(valor)
    total=total+valor1
else:
    for x in lista:
        var=int(x)
        total=total+var
print(total)
