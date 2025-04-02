import math
var=float(input())
a=math.floor(var)
b=math.ceil(var)
c=round(var)
if (var-c)==0.5:
    d=b
    print(a,b,d)
else:
    print(a,b,c)