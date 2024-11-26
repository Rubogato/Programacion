#Las tres comillas permiten que el print pueda mostrar el texto en diferentes líneas
print("""
INSTRUCCIONS
1.La longitud del password té que tenir entre 6 i 8 caràcters
2.Forçar els següents valors segons la posició indicada:
    Posició 1 Un número major o igual que 1 i menor o igual que 5
    Posició 2 Una lletra minúscula
    Posició 3 Una lletra mayúscula
    Posició 4 Un dels següents símbols *, _, @
    Posició 5 Una lletra minúscula
    Posició 6 Un número major o igual que 6 i menor o igual que 9
    Posició 7 Un dels següents símbols &,/,#
    Posició 8 Un número menor o igual que 5
""")
password=input("Introduce una palabra clave: ")
lon=len(password)
#Pongo un condicional para que el programa solo se ejecute si la longitud es correcta
if lon>=6 and lon<=8:
    #Le doy el valor a las variables con el valor de cada caracter
    a=password[0]
    b=password[1]
    c=password[2]
    d=password[3]
    e=password[4]
    f=password[5]
    #le doy valor de 0 para evitar errores por la longitud
    g=0
    h=0
    #Solamente si la longitud es 7 o 8 les doy el valor que les corresponda
    if lon>=7:
        g=password[6]
        if lon==8:
            h=password[7]
    #Hago que estas variables tengan ya el texto de error
    e1="Error en el caràcter 1 "
    e2="Error en el caràcter 2 "
    e3="Error en el caràcter 3 "
    e4="Error en el caràcter 4 "
    e5="Error en el caràcter 5 "
    e6="Error en el caràcter 6 "
    e7="Error en el caràcter 7 "
    e8="Error en el caràcter 8 "
    #Compruebo si es un numero o letra para evitar algún posible error si se pone una letra
    if a.isnumeric():
        #Convierto el valor string en valor numerico
        var1=int(a)
        if var1>=1 and var1<=5:
            #Hago que la variable e1 no tenga valor
            e1=""
    if b.islower():
        e2=""
    if c.isupper():
        e3=""
    if d=="*" or d=="_" or d=="@":
        e4=""
    if e.islower():
        e5=""
    if f.isnumeric():
        var2=int(f)
        if var2>=6 and var2<=9:
            e6=""
    #Aquí tengo en cuenta la longitud para que no muestre error si la longitud es inferior.
    if g==0:
        e7=""
    else:
        if g=="&" or g=="/" or g=="#":
            e7=""
    
    if h==0:
        e8=""
    else:
        if h.isnumeric():
            var3=int(h)
            if var3<=5 and var3>=0:
                e8=""
    #Aqui sumo las variables de error. El objetivo es que todo esté en una sola línea
    #Si hay algún error en el Password, la variable correspondiente no se borrará
    #Si no hay errores no quedará nada
    P1=e1+e2+e3+e4+e5+e6+e7+e8
    #Solamente mostrará que el Password es correcto si P1 no tiene nada, de otra manera mostrará P1
    if P1=="":
        print("El format del PASSWORD és correcte")
    else:
        print(P1)
else:
    print("Error, el password té una longitud de",lon,"caràcters i no compleix els requisits")