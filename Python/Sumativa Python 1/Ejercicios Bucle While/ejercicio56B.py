#56b.Opcional. Haz alguna o todas las mejoras en el programa anterior que a continuación se 
#indican:
cond="s"
pedidos=0
precio=0
print("""MEN�
1. Bocadillo de calamares- 9 �
2. Bocadillo de chistorra - 4.5 �
3. Bikini de jamón - 2.5 �

ACOMPAÑAMIENTO
1. Patatas finas - 1.5 �
2. Patatas gruesas - 1.75 �
3. Patatas rústicas - 2 �

BEBIDAS
1. Coca cola - 2 �"
2. Acuarius - 1.5 �
3. Agua - 1 �""")
while cond=="s":
    pedidos=pedidos+1
    if input("�Quiere pedir un bocadillo? s/n: ").lower()=="s":
        boc=int(input("Introduce el bocadillo: "))
    if input("�Quiere pedir un acompa�amiento? s/n: ").lower()=="s":
        aco=int(input("Introduce el acompa�amiento: "))
    if input("�Quiere pedir una bebida? s/n: ").lower()=="s":
        beb=int(input("Introduce la bebida: "))
    if boc==1:
        precio=precio+9
    elif boc==2:
        precio=precio+4.5
    else:
        precio=precio+2.5
    if aco==1:
        precio=precio+1.5
    elif aco==2:
        precio=precio+1.75
    else:
        precio=precio+2
    if beb==1:
        precio=precio+2
    elif beb==2:
        precio=precio+1.5
    else:
        precio=precio+1
    cond=input("�Quieres realizar otro pedido? s/n: ").lower()
    if not cond=="s" or cond=="n"
    print("Ha introducido un valor err�neo")
    int("�Quieres realizar otro pedido? s/n: ")
totaliva=round(precio+precio*10/100,2)
print("RESUMEN")
print("N�mero de pedidos:",pedidos)
print("Total a pagar:",precio)
print("Total con IVA:",totaliva)
if precio>=20 and precio<=30:
    total=round(totaliva-totaliva*5/100,2)
    print("Precio total con descuento del 5%:",total)
if precio>30:
    total=round(totaliva-totaliva*15/100,2)
    print("Precio total con descuento del 15%:",total)