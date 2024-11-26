#36. Programa que sume los n primeros n√∫meros naturales. n Lo introduce el usuario.
rep=int(input("Introduce el valor de 'n': "))
var1=0
for contador in range(0,rep+1):
    var1=var1+contador
print("La suma total de números naturales es:",var1)