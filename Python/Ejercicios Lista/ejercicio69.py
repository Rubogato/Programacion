#69. Realiza un programa que permita introducir una cantidad exacta de números, cada número se 
#irá almacenando en una lista. El programa debe finalizar presentando por pantalla los números 
#ordenados de menor a mayor.
lista=[]
contador=int(input("Introduce el número de repeticiones: "))
for x in range(0,contador):
    num=int(input("Introduce un número: "))
    lista.append(num)
lista.sort()
print(lista)