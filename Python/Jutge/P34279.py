num=input()
lista=num.split()
var=int(lista[0])*3600+int(lista[1])*60+int(lista[2])+1
horas=var//3600
r=var%3600
minutos=r//60
s=r%60
if horas<10:
    hh="0"+str(horas)
elif horas>=24:
    hh="0"+str(horas-24)
else:
    hh=str(horas)
if minutos<10:
    mm="0"+str(minutos)
else:
    mm=str(minutos)
if s<10:
    ss="0"+str(s)
else:
    ss=str(s)
print(f"{hh}:{mm}:{ss}")