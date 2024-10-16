#Realiza un programa que, introduciendo en los valores de lado, base menor, base mayor 
#y altura de un trapecio isósceles, nos devuelva por pantalla en el área y el perímetro.
lado=int(input("Dime cuánto miden los lados: "))
bame=int(input("Dime cuánto mide la base menor: "))
bama=int(input("Dime cúanto mide la base mayor: "))
alt=int(input("Dime la altura del trapecio: "))
peri=bame+bama+(lado*2)
area=((bama+bame)/2)*alt
print("El perímetro es: ",peri)
print("El área es: ", area)
