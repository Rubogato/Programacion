print("""
INSTRUCCIONES
1.La longitud del PASSWORD tiene que tener más de 8 caracteres
2. EL PASSWORD tiene que cumplir con las siguientes condiciones:
    1. Al menos 3 números
    2. Al menos 2 letras minúsculas
    3. Al menos 2 letras minúsculas
    3. Al menos 1 símbolo de los siguientes: -; _; *; /; %; &; @
""")
for cont in range(3):
    mayus=0
    minus=0
    simb=0
    num=0
    errores=""
    password=input("Introduce una palabra clave: ")
    lon=len(password)
    if lon>=8:
        for x in password:
            if x.isupper():
                mayus=mayus+1
            if x.islower():
                minus=minus+1
            if x.isnumeric():
                num=num+1
            if x=="-" or x=="_" or x=="*" or x=="/" or x=="%" or x=="&" or x=="@":
                simb=simb+1
        a=-mayus+2
        b=-minus+2
        c=-num+3
        d=-simb+1
        if a<=0 and b<=0 and c<=0 and d<=0:
            print("El formato PASSWORD es correcto")
        else:
            if a>0:
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
                errores=errores+(f"Falta {d} símbolo, ")
            print(errores[0:len(errores)-2])
    else:
        print("El password es demasiado corto")