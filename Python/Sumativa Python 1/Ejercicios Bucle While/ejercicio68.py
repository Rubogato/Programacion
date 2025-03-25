#66. Añade al ejercicio anterior la posibilidad de que el programa pregunte si deseas o no continuar 
#introduciendo passwords. Ej. “¿Deseas introducir otro password s/n?
cond="s"
while cond=="s":
    mayus=0
    minus=0
    simb=0
    ent=0
    password=input("Introduce una palabra clave: ")
    lon=len(password)
    if lon<=8 and lon>=6:
            for x in password:
                if x.isupper():
                    mayus=mayus+1
                if x.islower():
                    minus=minus+1
                if x.isnumeric():
                    x=int(x)
                    if x>=1 and x<=5:
                        ent=ent+1
                if x=="*" or x=="_" or x=="/" or x=="&" or x=="@" or x=="#":
                    simb=simb+1
            a=1-mayus
            b=2-minus
            c=2-simb
            d=1-ent
            if a<=0 and b<=0 and c<=0 and d<=0:
                print("password correcto")
            else:
                print("password incorrecto")
    else:
        print("password incorrecto")
    cond=input("¿Deseas introducir otro password s/n? ")