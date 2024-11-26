# 44. Realiza un programa que recorra todos los números comprendidos de 0 a 100 realizando saltos 
#de 3 en 3. El resultado debe aparecer por pantalla en una línea con los números separados por ‘,’
a=0
b=""
for x in range(0,100+1,3):
    a=str(x)
    if x<99:
        b=b+a+","
    else:
        b=b+a
print (b)