"""
zoznam = [10,0,-1]
for prvok in zoznam:
    print(prvok)
"""

zelenina = ["mrkva", "brokolica","melon", "kapusta"]
ovocie = ["jablko", "malina", "hruska", "banan"]

while(True):
    slovo = input("zadaj slovo: ")
    if slovo in zelenina:
        print("zadal si zeleninu")
    elif slovo in ovocie:
        print("zadal si ovocie")
    else:
        print("toto slovo nepoznam")

    otazka = input("prajes si zadat dalsie slovo? ano/nie")
    if otazka == "nie":
        break
