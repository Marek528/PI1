from statistics import median


while(True):
    premenna = input("zadaj cislo: ")
    if premenna != "":
        premenna = int(premenna)

    else:
        break

print('median zadanych cisel je: ', median())

