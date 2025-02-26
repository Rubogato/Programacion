#72. A partir del ejercicio anterior, se da por hecho que las vocales con o sin acento son repetidas y 
#no deben almacenarse en la lista.
x="s"
lista=[]
a=0
e=0
i=0
o=0
u=0
vocales_a="aàáAÀÁ"
vocales_e="eéèÉÈE"
vocales_i="iíìÍÌI"
vocales_o="oòóOÒÓ"
vocales_u="uùúUÙÚ"
while x=="s":
    letra=input("Introduce una letra: ")
    while not letra.isalpha():
        letra=input("Introduce otra letra: ")
    var=lista.count(letra)
    if letra in vocales_a:
        if a==0:
            lista.append(letra)
            a=1
    elif letra in vocales_e:
        if e==0:
            lista.append(letra)
            e=1
    elif letra in vocales_i:
        if i==0:
            lista.append(letra)
            i=1
    elif letra in vocales_o:
        if o==0:
            lista.append(letra)
            o=1
    elif letra in vocales_u:
        if u==0:
            lista.append(letra)
            u=1
    elif var==0:
        lista.append(letra)
    x=input("Quieres repetir? s/n: ")
lista.sort() 
print(lista)