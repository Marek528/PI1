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

for i in range(dlzka_cisel):
    




