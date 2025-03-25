var_1=float(input("Introduce el primer número: "))
#He usado float, para poder introducir decimales
var_2=float(input("Introduce el segundo número: "))
var_total=var_1+var_2
#El comando round redondea el valor de la izquierda de la coma con el numero de decimales que se especifica a la derecha de la coma
var_divi=round(var_total/3,3)
#He usado el round para quitar el decimal con el valor más cercano posible al original
var_total=round(var_total)
print(f"El resultado de sumar",var_1,"y",var_2,"es:",var_total)
print(f"El resultado de dividir",var_total,"entre 3 es:",var_divi)
