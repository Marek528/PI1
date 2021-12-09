hracie_pole = [
    [" ", 1,2,3],
    [1, " ", " ", " "],
    [2, " ", " ", " "],
    [3, " ", " ", " "],
]

krizik = "X"
kruzok = "O"

def usporiadanie(hracie_pole):
    for riadok in hracie_pole:
        for policko in riadok:
            print(policko, end= "")
        print()


while True:
    usporiadanie(hracie_pole)
    print('Na rade je hrac s krizikmi')
    poloha1 = int(input('zadaj poziciu 1: '))
    if poloha1 > 3:
        print('zadaj mensie cislo!')
    elif poloha1 == 0:
        print('zadaj väčšie cislo!')
    else:
        continue

    poloha2 = int(input('zadaj poziciu 2: '))
    if poloha2 > 3:
        print('zadaj mensie cislo!')
    elif poloha2 == 0:
        print('zadaj väčšie cislo!')
    else:
        continue
    vkladanie = hracie_pole[poloha1][poloha2] = 'X'
    

    usporiadanie(hracie_pole)
    print('Na rade je hrac s kruzkami')
    poloha1 = int(input('zadaj poziciu 1: '))
    if poloha1 > 3:
        print('zadaj mensie cislo!')
    elif poloha1 == 0:
        print('zadaj väčšie cislo!')
    else:
        continue

    poloha2 = int(input('zadaj poziciu 2: '))
    if poloha2 > 3:
        print('zadaj mensie cislo!')
    elif poloha2 == 0:
        print('zadaj väčšie cislo!')
    else:
        continue
    vkladanie = hracie_pole[poloha1][poloha2] = 'O'