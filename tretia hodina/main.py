"""
cislo = 1
while (cislo <= 10):
    print(cislo)
    cislo = cislo + 1
print("tento kod sa vykoná dalej")
"""

"""
start = 10
koniec = 0
while (start >= koniec):
    if start == 5:
        start -= 1
        continue
    print(start)
    start = start - 1

print("--------")

start = 10
koniec = 0
while (start >= koniec):
    if start == 5:
        break
    print(start)
    start = start - 1

print("-----------------")

start = int(input("zadaj odkial bude pocitat: "))
koncove = int(input("zadaj pokial bude pocitat: "))
while(start < koniec):
    if(start % 3 == 0):
        print(start, "je nasobok 3ky")
    start += 1

print("-----------------")

for premenna in range(10):
    print(premenna)
"""


samohlasky = "aáeéiíoóuúyý"
spoluhlasky = "dtnlchhgkďťňľcčžšdzdžjmbpvszsfr"
cislo = "0123456789"

slovo = input("Zadaj slovo: ")

pocet_znakov = 0
pocet_samohlasok = 0
pocet_spol = 0
pocet_cis = 0

for znak in slovo:
    if znak in samohlasky:
        pocet_samohlasok += 1

    elif znak in spoluhlasky:
        pocet_spol += 1

    elif znak in cislo:
        pocet_cis += 1

    else:
        pocet_znakov += 1

print("slovo obsahuje samohlasky", pocet_samohlasok)
print("slovo obsahuje spoluhlasky", pocet_spol)
print("slovo obsahuje cislo", pocet_cis)
print("slovo obsahuje ine znaky", pocet_znakov)