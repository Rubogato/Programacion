var=int(input())
horas=var//3600
r=var%3600
minutos=r//60
s=r%60
print(horas,minutos,s)