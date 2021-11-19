cisla = []

while(True):
    premenna = input("zadaj cislo: ")
    if premenna != "":
        premenna = int(premenna)
        cisla.append(premenna)
    else:
        break

zoradene_cisla = sorted(cisla)
print(zoradene_cisla)




