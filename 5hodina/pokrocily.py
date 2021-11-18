cisla = []

while(True):
    premenna = input("zadaj cislo: ")
    if premenna != "":
        premenna = int(premenna)
        cisla.append(premenna)
    else:
        break

print(cisla)
velkost = len(cisla)
median = (velkost + 1) / 2



print(int(median))


