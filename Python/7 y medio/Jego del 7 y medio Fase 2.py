import random
c=input("Quieres jugar? s/n")
depo=100
while c=="s" or c=="ss":
    num=[1,2,3,4,5,6,7,10,11,12]
    lista=[]
    cond="s"
    acu=0
    while cond=="s":
        var=0
        while var==0:
            cartas=random.choice(num)
            lista.append(cartas)
            if cartas==1:
                uno=lista.count(1)
                if uno<=4:
                    var=1
            elif cartas==2:
                dos=lista.count(2)
                if dos<=4:
                    var=1
            elif cartas==3:
                tres=lista.count(3)
                if tres<=4:
                    var=1
            elif cartas==4:
                cuatro=lista.count(4)
                if cuatro<=4:
                    var=1
            elif cartas==5:
                cinco=lista.count(5)
                if cinco<=4:
                    var=1
            elif cartas==6:
                seis=lista.count(6)
                if seis<=4:
                    var=1
            elif cartas==7:
                siete=lista.count(7)
                if siete<=4:
                    var=1
            elif cartas==10:
                diez=lista.count(10)
                if diez<=4:
                    var=1
            elif cartas==11:
                once=lista.count(11)
                if once<=4:
                    var=1
            else:
                doce=lista.count(12)
                if doce<=4:
                    var=1
        valor=cartas
        if cartas==10 or cartas==11 or cartas==12:
            valor=0.5
        acu=acu+valor
        print("Tu carta es:",cartas)
        print("acumulas:",acu)
        if acu>7.5:
            print("Has perdido la partida!")
            depo=depo-10
            break
        if acu==7.5:
            print("Enhorabuena, has ganado la partida")
            depo=depo+10
            break
        cond=input("Quieres otra carta? s/n: ")
        cond=cond.lower()
    if not cond=="s" or cond=="ss":
        if acu>=6 and acu<=7:
            print("Has sido un poco conservador")
            depo=depo+5
        if acu<6:
            print("Quizás tendrías que arriesgar un poco ¿no?")
            depo=depo-5
    print("Tu depósito es de:",depo)
    if depo>0:
        c=input("Quieres repetir la partida? s/n: ")
    else:
        print("Estás arruinado!")
        c=""