a = int(input("Zadaj hodnotu a = "))
b = int(input("Zadaj hodnotu b = "))

scitanie = a + b
odcitanie = a - b
nasobenie = a * b


print("scitanie = ", scitanie)
if scitanie == 0:
    print("vysledok scitavania je nezaporne cele cislo")
else:
    if scitanie > 0:
        print("vysledok scitavania je kladne cislo")
    else:
        print("vysledok scitavania je zaporne cislo")


print("odcitanie = ", odcitanie)
if odcitanie == 0:
    print("vysledok odcitavania je nezaporne cele cislo")
else:
    if odcitanie > 0:
        print("vysledok odcitavnia je kladne cislo")
    else:
        print("vysledok odcitavania je zaporne cislo")


print("nasobenie =", nasobenie)
if nasobenie == 0:
    print("vysledok nasobenia je nezaporne cele cislo")
else:
    if nasobenie > 0:
        print("vysledok nasobenia je kladne cislo")
    else:
        print("vysledok nasobenia je zaporne cislo")


if b == 0:
    print("Nulou sa delit neda!!")
else:
    print("delenie = ", a / b)
    if a / b == 0:
        print("vysledok delenia je nezaporne cele cislo")
    else:
        if a / b > 0:
            print("vysledok delenia je kladne cislo")
        else:
            print("vysledok delenia je zaporne cislo")
