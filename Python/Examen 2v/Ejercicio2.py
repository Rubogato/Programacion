texto=input("Introduce una frase: ")
lista=texto.split()
print(f"""Lista de palabras:
{lista}""")
palabra=input("Introduce la palabra buscada: ")
veces=lista.count(palabra)
frase=(",").join(lista)
print(f"La palabra {palabra} aparece {veces} veces")
print(frase)