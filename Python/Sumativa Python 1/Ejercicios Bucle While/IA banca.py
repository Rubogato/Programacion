
if maq==7.5 or maq>7.5:
    print("La banca se ha plantado")
    x=input("")
    a="n"
elif acu==7.5:
    print("La banca coge otra carta")
    x=input("")
    a="s"
elif acu<8:
    elif apuesta>=(banca*0.75) or apuesta==banca:
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