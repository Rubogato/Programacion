#Las tres comillas permiten que el print pueda mostrar el texto en diferentes l�neas
print("""
INSTRUCCIONS
1.La longitud del password t� que tenir entre 6 i 8 car�cters
2.For�ar els seg�ents valors segons la posici� indicada:
    Posici� 1 Un n�mero major o igual que 1 i menor o igual que 5
    Posici� 2 Una lletra min�scula
    Posici� 3 Una lletra may�scula
    Posici� 4 Un dels seg�ents s�mbols *, _, @
    Posici� 5 Una lletra min�scula
    Posici� 6 Un n�mero major o igual que 6 i menor o igual que 9
    Posici� 7 Un dels seg�ents s�mbols &,/,#
    Posici� 8 Un n�mero menor o igual que 5
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
    e1="Error en el car�cter 1 "
    e2="Error en el car�cter 2 "
    e3="Error en el car�cter 3 "
    e4="Error en el car�cter 4 "
    e5="Error en el car�cter 5 "
    e6="Error en el car�cter 6 "
    e7="Error en el car�cter 7 "
    e8="Error en el car�cter 8 "
    #Compruebo si es un numero o letra para evitar alg�n posible error si se pone una letra
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
    #Aqu� tengo en cuenta la longitud para que no muestre error si la longitud es inferior.
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
    #Aqui sumo las variables de error. El objetivo es que todo est� en una sola l�nea
    #Si hay alg�n error en el Password, la variable correspondiente no se borrar�
    #Si no hay errores no quedar� nada
    P1=e1+e2+e3+e4+e5+e6+e7+e8
    #Solamente mostrar� que el Password es correcto si P1 no tiene nada, de otra manera mostrar� P1
    if P1=="":
        print("El format del PASSWORD �s correcte")
    else:
        print(P1)
else:
    print("Error, el password t� una longitud de",lon,"car�cters i no compleix els requisits")