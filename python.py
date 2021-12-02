import random
from random import randint

privlastky = ['maly', 'velky', 'pekny', 'skaredy', 'chudy', 'vesely', 'smutny', 'nudny', 'zaujimavy', 'tucny' ]
zoznam_mien = []

while True:
    meno = input('zadaj meno: ')
    priezvisko = input('zadaj priezvisko: ')
    mismas = meno + ' ' + privlastky[random.randint(0,9)] + ' ' + priezvisko
    zoznam_mien.append(mismas)
    
    for i in range(0, len(zoznam_mien)):
        print(str(i+1)+ ".\t" + zoznam_mien[i])
