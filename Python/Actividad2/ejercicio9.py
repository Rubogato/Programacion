#programa que pida los segundos y muestre por pantalla y en la misma frase los minutos 
#y las horas
valor1=int(input("Dime los segundos: "))
minutos=round(valor1/60,1)
horas=round(valor1/3600,2)
print("el numero de minutos es:",minutos,"y en horas es:",horas)
