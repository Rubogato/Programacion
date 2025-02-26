
num=[]
let=[]
total=0
var=input("Introduce una serie de números con un guion en medio: ")
lista=var.split("-")
for x in lista:
    if x.isnumeric():
        num.append(int(x))
    else:
        let.append(x)
print(sum(num))