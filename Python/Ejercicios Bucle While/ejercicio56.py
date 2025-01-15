#56. Realiza un programa que gestione un establecimiento de venta de bocadillos. Un pedido se 
#compone de: bocadillo, acompañamiento y bebida. Un cliente puede pedir más de un pedido. El 
#dependiente a partir del menú (ver imagen), se encarga de introducir los datos. El menú solo se 
#visualiza una vez al ejecutar el programa. El programa debe preguntar al dependiente tras la 
#realización de un pedido, si quiere gestionar otro.
cond="s"
pedidos=0
precio=0
print("""MENÚ
1. Bocadillo de calamares- 9 €"
2. Bocadillo de chistorra - 4.5 €
3. Bikini de jamón - 2.5 €"

ACOMPAÑAMIENTO
1. Patatas finas - 1.5 €
2. Patatas gruesas - 1.75 €
3. Patatas rústicas - 2 €

BEBIDAS
1. Coca cola - 2 €"
2. Acuarius - 1.5 €
3. Agua - 1 €""")
while cond=="s":
    pedidos=pedidos+1
    boc=int(input("Introduce el bocadillo: "))
    aco=int(input("Introduce el acompañamiento: "))
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
    cond=input("¿Quieres realizar otro pedido? s/n: ")
totaliva=round(precio+precio*10/100,2)
print("RESUMEN")
print("Número de pedidos:",pedidos)
print("Total a pagar:",precio)
print("Total con IVA:",totaliva)
if precio>=20 and precio<=30:
    total=round(totaliva-totaliva*5/100,2)
    print("Precio total con descuento del 5%:",total)
if precio>30:
    total=round(totaliva-totaliva*15/100,2)
    print("Precio total con descuento del 15%:",total)
