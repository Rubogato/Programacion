#Cines Paradiso celebran su décimo aniversario y por ser un día especial realizan 
#importantes descuentos. A los adultos se les aplicará un 10% de descuento y a los menores 
#de 18 años un 50%. Si la entrada cuesta 12 euros, calcula el total a pagar introduciendo por 
#teclado el número de menores y el número de adultos que asisten al cine.
ad=int(input("Dime el numero de adultos: "))
me=int(input("Dime el numero de menores: "))
prad=round(ad*12/10*9,2)
prme=round(me*12/2,2)
print("El precio total del cine para",me,"menor/es es: ",prme)
print("EL precio total del cine para",ad,"adulto/s es: ",prad)
       
