
#pretypovanie
#cislo
#vek = int(input("Zadaj svoj vek: "))
#print(vek + 10)

#pretypovanie
#desatine cislo
#polomerKruhu = float(input("zadaj polomer kruhu: "))#
#obvodKruhu = 2*3.14*polomerKruhu
#print("Obvdo kruhu je", obvodKruhu)

"""uloha 1
a = int(input("Zadaj cislo a: "))
b = int(input("Zadaj cislo b: "))
print("scitanie: ", a+b)
print("odcitanie: ", a-b)
print("nasobenie: ", a*b)
if b == 0:
    print("nulou sa delit neda")
else:
    print("delenie: ", a / b)
#print("delenie: ", a/b)
koniec ulohy"""

#+-, *, %, **, /                - aritmeticke operatory
#==, !=, <, >, <=, >=           - logicke operatory
#vysledok = 1 != 2
#print(vysledok)

"""vek = int(input("zadaj svoj vek "))
if vek >= 18:
    print("vstup dalej, mas dost rokov")
    print("vitaj medzi nami")
else:
    print("vstup zakazany, si moc mlady!")

print("tento kod sa vykona vzdy")"""


"""a = 10
b = 20
z = a
a = b
b = z
print("a = ", a)
print("b = ", b)"""



"""day = 5
hour = 10

if day == 1:
    print("pondelok")
elif day == 2:
    print("utorok")
elif day == 3:
    print("streda")
elif day == 4:
    print("stvrtok")
elif day == 5:
    print("piatok")
    if hour < 12:
        print("je doobeda")
    else:
        print("je poobede")
elif day == 6:
    print("sobota")
elif day == 7:
    print("nedela")"""

username = input ("zadaj prihlasovacie meno: ")
password = input ("zadaj prihlasovacie heslo: ")
vek = input("zadaj svoj vek: ")

if username == "root" and password == "password" and vek == "18":
    print("uspesne si sa prihlasil!")
else:
    print("zle meno alebo heslo alebo vek")