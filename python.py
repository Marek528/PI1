from random import randint

privlastky = ['maly', 'velky', 'pekny', 'skaredy', 'chudy', 'vesely', 'smutny', 'nudny', 'zaujimavy', 'tucny' ]
zoznam_mien = []

while True:
    meno = input('zadaj meno: ')
    priezvisko = input('zadaj priezvisko: ')
    mismas = meno + '' + privlastky[random.randint(0,9)] + '' + priezvisko
    zoznam_mien.append(mismas)
    print(zoznam_mien)