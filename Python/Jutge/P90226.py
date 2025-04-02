word=input()
lista=word.split()
x=lista[0]
y=lista[1]
if x>y:
    print(f"{x} > {y}")
elif x<y:
    print(f"{x} < {y}")
else:
    print(f"{x} = {y}")