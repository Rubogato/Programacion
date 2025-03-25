#56b.Opcional. Haz alguna o todas las mejoras en el programa anterior que a continuaciÃ³n se 
#indican:
cond="s"
pedidos=0
precio=0
print("""MENò
1. Bocadillo de calamares- 9 Û
2. Bocadillo de chistorra - 4.5 Û
3. Bikini de jamÃ³n - 2.5 Û

ACOMPAÃ‘AMIENTO
1. Patatas finas - 1.5 Û
2. Patatas gruesas - 1.75 Û
3. Patatas rÃºsticas - 2 Û

BEBIDAS
1. Coca cola - 2 Û"
2. Acuarius - 1.5 Û
3. Agua - 1 Û""")
while cond=="s":
    pedidos=pedidos+1
    if input("ÀQuiere pedir un bocadillo? s/n: ").lower()=="s":
        boc=int(input("Introduce el bocadillo: "))
    if input("ÀQuiere pedir un acompa–amiento? s/n: ").lower()=="s":
        aco=int(input("Introduce el acompa–amiento: "))
    if input("ÀQuiere pedir una bebida? s/n: ").lower()=="s":
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
    cond=input("ÀQuieres realizar otro pedido? s/n: ").lower()
    if not cond=="s" or cond=="n"
    print("Ha introducido un valor err—neo")
    int("ÀQuieres realizar otro pedido? s/n: ")
totaliva=round(precio+precio*10/100,2)
print("RESUMEN")
print("Nœmero de pedidos:",pedidos)
print("Total a pagar:",precio)
print("Total con IVA:",totaliva)
if precio>=20 and precio<=30:
    total=round(totaliva-totaliva*5/100,2)
    print("Precio total con descuento del 5%:",total)
if precio>30:
    total=round(totaliva-totaliva*15/100,2)
    print("Precio total con descuento del 15%:",total)