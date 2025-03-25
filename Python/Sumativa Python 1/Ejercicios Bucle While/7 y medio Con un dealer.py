import random
y="s"
nombre=input("Banca: Cómo quiere que le llame? ")
while y=="s":
    cond="s"
    maq=0
    acu=0
    a="s"
    while cond=="s":
        var=0
        while var==0:
            cartas=random.randint(1,12)
            if not cartas==8 and not cartas==9:
                var=1
        valor=cartas
        if cartas==10 or cartas==11 or cartas==12:
            valor=0.5
        acu=acu+valor
        print("Tu carta es:",cartas)
        print("acumulas:",acu)
        if acu<7.5:
            cond=input(f"BANCA: Quieres otra carta? {nombre} ")
        elif acu>7.5:
            print("Te has pasado de 7.5 y te plantas")
            break
        else:
            print("Tienes un 7.5 y te plantas")
            break
    while a=="s":
        b=0
        while b==0:
            c=random.randint(1,12)
            if not c==8 and not c==9:
                b=1
        pun=c
        if c==10 or c==11 or c==12:
            pun=0.5
        maq=maq+pun
        print("La banca coge un:",c)
        print("La banca acumuló:",maq)
        if maq<=5:
            print("La banca coge otra carta")
            x=input("")
            a="s"
        if maq>5 and maq<=6:
            p=random.randint(1,2)
            if p==1:
                print("La banca se ha plantado")
                x=input("")
                a="n"
            else:
                print("La banca coge otra carta")
                x=input("")
                a="s"
        if maq>6:
            print("La banca se ha plantado")
            x=input("")
            a="n"
    if maq<7.5 and acu<7.5:
        if maq==acu:
            print("La banca acumuló:",maq)
            print("EMPATE")
        elif maq>acu:
            print("La banca acumuló:",maq)
            print(f"BANCA: Has perdido, {nombre}")
        else:
            print("La banca acumuló:",maq)
            print(f"BANCA: Ganaste, {nombre}")
    elif maq==7.5 and acu==7.5:
        print("La banca acumuló:",maq)
        print("EMPATE")
    elif maq>7.5 and acu>7.5:
        print("La banca acumuló:",maq)
        print("BANCA: Tanto tú como yo perdimos...")
    elif maq>7.5 or acu==7.5:
        print("La banca acumuló:",maq)
        print(f"BANCA: Ganaste, {nombre}")
    elif acu>7.5 or maq==7.5:
        print("La banca acumuló:",maq)
        print(f"BANCA: Has perdido, {nombre}")
    y=input(f"Quieres repetir la partida? {nombre} ")