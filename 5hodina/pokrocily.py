cisla = []

while(True):
    premenna = input("zadaj cislo: ")
    if premenna != "":
        premenna = int(premenna)
        cisla.append(premenna)
    else:
        break

zoradene_cisla = sorted(cisla)
dlzka_cisel = len(zoradene_cisla)
vypocet_medianu = int(dlzka_cisel / 2)
median = zoradene_cisla[vypocet_medianu]


for i in range(dlzka_cisel):
    x = cisla[i]
    rozdiel_od_medianu = x - median
    print(x, 'sa od medianu odlisuje o', rozdiel_od_medianu)



