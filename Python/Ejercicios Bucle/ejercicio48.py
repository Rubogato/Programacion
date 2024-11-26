#48. Realiza un programa que introduzcas por teclado una palabra ‘secreta’, consigue la longitud de 
#esa palabra para que sea ese el criterio que establezca el rango del bucle de manera que el usuario
#tenga x oportunidades para ver si letra introducida está en esa palabra
palabra=input("Introduce la palabra secreta: ")
for x in palabra:
    let=input("Introduce una letra: ")
    a=palabra.count(let)
    if a>=1:
        print("La letra existe")
    else:
        print("La letra no existe")