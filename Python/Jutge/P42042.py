letra=input()
if letra.isupper():
    print("uppercase")
elif letra.islower():
    print("lowercase")
a=letra.lower()
if a in ("aeiou"):
    print("vowel")
else:
    print("consonant")