lado=int(input("Dime cuánto midel el segundo lado: "))
bame=int(input("Dime cuánto mide la base menor: "))
bama=int(input("Dime cúanto mide la base mayor: "))
alt=int(input("Dime la altura del trapecio: "))
peri=bame+bama+(lado*2)
area=((bama+bame)/2)*alt
print("El perímetro es: ",peri)
print("El área es: ", area)
