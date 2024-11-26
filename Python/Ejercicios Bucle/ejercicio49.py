#49. A partir del programa anterior, modifica el código para que al introducir la letra por teclado te 
#indique en qué posición de la palabra se encuentra la letra.
palabra=input("Introduce la palabra secreta: ")
for x in palabra:
    let=input("Introduce una letra: ")
    a=palabra.count(let)
    if a>=1:
        b=0
        for z in palabra:
            if let==z:
                print("la letra se encuentra en la posición",b+1)
            b=b+1
    else:
        print("La letra no existe")