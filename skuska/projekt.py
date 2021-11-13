import random

cislo = input("zadaj cislo: ")

if cislo.isdigit():
    cislo = int(cislo)
    
    if cislo <= 0:
        print("prosim zadaj cislo väčšie ako 0.")
        quit()
else:
    print("prosim zadaj cislo.")
    quit()

nahodne_cislo = random.randint(0, cislo)
pocet_tipov = 0

while True:
    pocet_tipov += 1
    tip = input("tipni si cislo: ")
    if tip.isdigit():
        tip = int(tip)
    else:
        print("prosim zadaj cislo.")
        continue

    if tip == nahodne_cislo:
        print("tipol si si spravne!")
        break
    elif tip > nahodne_cislo:
        print("Bol si nad cislom")
    else:
        print("Bol si pod cislom")


if pocet_tipov == 1:
    print("dal si to na", pocet_tipov, "tip.")
elif pocet_tipov == 2 or 3 or 4:
    print("dal si to na", pocet_tipov, "tipy.")
else:
    print("dal si to na", pocet_tipov, "tipov.")



