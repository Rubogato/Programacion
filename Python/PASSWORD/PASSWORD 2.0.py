#Printeo las intrucciones
print("""
INSTRUCCIONES
1.La longitud del PASSWORD tiene que tener más de 8 caracteres
2. EL PASSWORD tiene que cumplir con las siguientes condiciones:
    1. Al menos 3 números
    2. Al menos 2 letras minúsculas
    3. Al menos 2 letras minúsculas
    3. Al menos 1 símbolo de los siguientes: -; _; *; /; %; &; @
""")
#El bucle con las veces que se hará el programa
for cont in range(3):
    #Inicializo las variables y hacer que existan
    mayus=0
    minus=0
    simb=0
    num=0
    errores=""
    password=input("Introduce una palabra clave: ")
    lon=len(password)
#Hice que la longitud fuera mayor o igual a 8 para que fuera más simple de programar y que fuera más realista
#(las contraseñas suelen tener un tamaño mínimo y no máximo). Además de que una longitud de 8 és bastante segura.
    if lon>=8:
        #Hago un bucle donde se recorra la contraseña
        for x in password:
            #Condicionales donde si la letra es una de las siguientes se sume uno a la variable correspondiente
            if x.isupper():
                mayus=mayus+1
            if x.islower():
                minus=minus+1
            if x.isnumeric():
                num=num+1
            if x=="-" or x=="_" or x=="*" or x=="/" or x=="%" or x=="&" or x=="@":
                simb=simb+1
        #Fuera del bucle le resto al número mínimo de mayúsculas, minuscules, numeros o símbolos
        #el número de veces que hayan salido
        a=2-mayus
        b=2-minus
        c=3-num
        d=1-simb
        #Si el valor es menor o igual a cero significa las condiciones del password se han cumplido
        if a<=0 and b<=0 and c<=0 and d<=0:
            print("El formato PASSWORD es correcto")
        else:
            #Si falta alguna cosa, aquí se mira qué falta y se encadenan los errores
            if a>0:
                #Pongo otro condicional por si falta una sola letra y que esté bien escrito
                if a==1:
                    errores=errores+(f"Falta {a} mayúscula, ")
                else:
                    errores=errores+(f"Faltan {a} mayúsculas, ")
            if b>0:
                if b==1:
                    errores=errores+(f"Falta {b} minúscula, ")
                else:
                    errores=errores+(f"Faltan {b} minúsculas, ")
            if c>0:
                if c==1:
                    errores=errores+(f"Falta {c} número, ")
                else:
                    errores=errores+(f"Faltan {c} números, ")
            if d==1:
                #El valor d o símbolos no necesita una variación en plural
                errores=errores+(f"Falta {d} símbolo, ")
            #Por último printea la cadena de errores menos los últimos dos caracteres para que no salga la coma final
            print(errores[0:len(errores)-2])
    else:
        print("El password es demasiado corto")