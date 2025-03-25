import random
b=1
while b==1:
    pregunta=input("Banca: Quieres jugar al 7 y medio? (s/n) ")
    if pregunta=="s" or pregunta=="n":
        b=0
if pregunta=="s":
    y="s"
    ñ=0
    var=0
    valor=0
    dinero=100
    banca=100
    nombre=input("Banca: Cómo quiere que le llame? ")
    lista=[]
    print(f"""-------------------------------
    AL EMPEZAR:
    TÚ TIENES: {dinero} $
    LA BANCA TIENE: {banca} $
-------------------------------
    """)
    while y=="s":
        cantidad="n"
        while cantidad=="n":
            apuesta=input("¿Cuánto quieres apostar? ")
            if apuesta.isnumeric():
                apuesta=int(apuesta)
                if apuesta==0:
                    print("Banca: Esto no es un juego de niños, apuesta algo.")
                elif apuesta<=dinero:
                    cantidad="s"
                elif apuesta>dinero:
                    if var==0:
                        var=var+1
                        print("Banca: ¿Estás ciego?, no tienes suficiente dinero.")
                    elif var==1:
                        var=var+1
                        print("Banca: Parece que también estás sordo, ¿verdad?")
                    elif var==2:
                        var=var+1
                        print("Banca: Así ademas de ser sordo-ciego, eres insistente, ¿eh?")
                    elif var==3:
                        var=var+1
                        print("Banca: Si no apuestas algo que puedas pagar, entonces vete.")
                    elif var==4:
                        print("Narrador: Te acaban de echar del casino a patadas.")
                        y="n"
                        ñ=1
                        break
            else:
                if valor==0:
                    valor=valor+1
                    print("Banca: Perdone,¿qué acaba de decir?")
                elif valor==1:
                    valor=valor+1
                    print("Banca: Pare de balbucear y dígame cuánto quieres apostar.")
                elif valor==2:
                    valor=valor+1
                    valor1=input("Banca: ¿Estás bien, necesita ver a un médico? (s/n): ")
                    if valor1=="s":
                        print("Narrador: La banca ha llamado a una ambulancia y te llevaron al hospital.")
                        ñ=1
                        y="n"
                        break
        if ñ==1:
            break
        num=[1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,10,10,10,10,11,11,11,11,12,12,12,12]
        lista=[]
        a="s"
        cond="s"
        maq=0
        acu=0
        while cond=="s":
            cartas=random.choice(num)
            num.remove(cartas)
            lista.append(cartas)
            valor=cartas
            if cartas==10 or cartas==11 or cartas==12:
                valor=0.5
            acu=6
            print("Tu carta es:",cartas)
            print("acumulas:",acu)
            m=1
            if acu<=7.5:
                while m==1:
                    cond=input(f"""BANCA: Quieres otra carta? {nombre} (s/n):""")
                    if cond=="s" or cond=="n":
                        m=0
            elif acu>7.5:
                print("Te has pasado de 7.5 y te plantas")
                cond=""
        print("-------------------------------")
        while a=="s":
            cartas=random.choice(num)
            num.remove(cartas)
            lista.append(cartas)
            pun=cartas
            if cartas==10 or cartas==11 or cartas==12:
                pun=0.5
            maq=maq+pun
            print("La banca coje un:",cartas)
            print("La banca acumula:",maq)
            if maq==7.5 or maq>7.5:
                print("La banca se ha plantado")
                x=input("")
                a="n"
            elif acu==7.5:
                print("La banca coge otra carta")
                x=input("")
                a="s"
            elif acu<8:
                if apuesta>=(banca*0.75) or apuesta==banca:
                    if maq<acu or maq<5.5:
                        print("La banca coge otra carta")
                        x=input("")
                        a="s"
                    elif maq==acu or maq>=6:
                        print("La banca se ha plantado")
                        x=input("")
                        a="n"
                elif apuesta>=(banca*0.25) and apuesta<(banca*0.75):
                    if maq==acu or maq<acu or maq<5.5:
                        print("La banca coge otra carta")
                        x=input("")
                        a="s"
                    elif maq>acu and maq>6:
                        print("La banca se ha plantado")
                        x=input("")
                        a="n"
                elif apuesta<(banca*0.25):
                    if maq==7:
                        print("La banca se ha plantado")
                        x=input("")
                        a="n"
                    elif maq<6.5 or maq<acu or maq==acu:
                        print("La banca coge otra carta")
                        x=input("")
                        a="s"
                    elif maq>acu:
                        print("La banca se ha plantado")
                        x=input("")
                        a="n"
            else:
                if maq<6:
                    print("La banca coge otra carta")
                    x=input("")
                    a="s"
                else:
                    print("La banca se ha plantado")
                    x=input("")
                    a="n"
        if maq<7.5 and acu<7.5:
            if maq==acu:
                print("La banca acumuló:",maq)
                print("EMPATE")
            elif maq>acu:
                dinero=dinero-apuesta
                banca=banca+apuesta
                print("La banca acumuló:",maq)
                print(f"BANCA: Has perdido, {nombre}")
            else:
                dinero=dinero+apuesta
                banca=banca-apuesta
                print("La banca acumuló:",maq)
                print(f"BANCA: Ganaste, {nombre}")
        elif maq==7.5 and acu==7.5:
            print("La banca acumuló:",maq)
            print("EMPATE")
        elif maq>7.5 and acu>7.5:
            print("La banca acumuló:",maq)
            print("BANCA: Tanto tú como yo perdimos...")
        elif maq>7.5 or acu==7.5:
            dinero=dinero+apuesta
            banca=banca-apuesta
            print("La banca acumuló:",maq)
            print(f"BANCA: Ganaste, {nombre}")
        elif acu>7.5 or maq==7.5:
            dinero=dinero-apuesta
            banca=banca+apuesta
            print("La banca acumuló:",maq)
            print(f"BANCA: Has perdido, {nombre}")
        if dinero<=0 or banca<=0:
            y=""
        else:
            print(f"""-------------------------------
   RESUMEN DE LA SITUACION
   TÚ TIENES: {dinero} $
   LA BANCA TIENE: {banca} $
-------------------------------
        """)
            n=1
            while n==1:
                y=input(f"Quieres seguir apostando? {nombre} (s/n): ")
                if y=="s" or y=="n":
                    n=0
    else:
        if y=="n":
            print("Te has retirado y tienes",dinero,"$")
        elif banca<=0:
            print(f"La banca decide retirarse y tienes {dinero} $")
        elif dinero<=0:
            print("Te has arruinado")
else:
    print("Banca: Entonces,¡vete de aquí!")