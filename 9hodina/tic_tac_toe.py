hracie_pole = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]

hrac = True #ked je "True" znamena X, inak O
pocet = 0

def vypisHraciehoPola(hracie_pole):
    for riadok in hracie_pole:
        for policko in riadok:
            print(f"{policko} ", end= "")
        print()

def koniec(zadanie_cisla):
    if zadanie_cisla == "koniec":
        return True
    else:
        return False

def kontrolaVstupu(zadanie_cisla):
    if not kontrolaCisla(zadanie_cisla):
        return False
    zadanie_cisla = int(zadanie_cisla)
    if not hranice(zadanie_cisla):
        return False
    return True

def kontrolaCisla(zadanie_cisla):
    if not zadanie_cisla.isnumeric():
        print('Toto nie je cislo')
        return False
    else:
        return True

def hranice(zadanie_cisla):
    if zadanie_cisla > 9 or zadanie_cisla < 1:
        print('Toto cislo je mimo rozsahu')
        return False
    else:
        return True

def kontrolaHraciehoPola(poloha, hracie_pole):
    riadok = poloha[0]
    stlpec = poloha[1]
    if hracie_pole[riadok][stlpec] != "-":
        print('Tato pozicia je uz zabrana')
        return True
    else:
        return False

def suradnice(zadanie_cisla):
    riadok = int(zadanie_cisla / 3)
    stlpec = zadanie_cisla
    if stlpec > 2:
        stlpec = int(stlpec % 3)
    return (riadok, stlpec)

def pridajDoPola(poloha, hracie_pole, aktivny_hrac):
    riadok = poloha[0]
    stlpec = poloha[1]
    hracie_pole[riadok][stlpec] = aktivny_hrac

def aktualny_hrac(hrac):
    if hrac:
        return 'X'
    else:
        return 'O'

def kontrolaVyhry(hrac, hracie_pole):
    if kontrolaRiadkov(hrac, hracie_pole):
        return True
    if kontrolaStlpcov(hrac, hracie_pole):
        return True
    if kontrolaDiagonalne(hrac, hracie_pole):
        return True
    return False

def kontrolaRiadkov(hrac, hracie_pole):
    for riadok in hracie_pole:
        cely_riadok = True
        for policko in riadok:
            if policko != hrac:
                cely_riadok = False
                break
        if cely_riadok:
            return True
    return False

def kontrolaStlpcov(hrac, hracie_pole):
    for stlpec in range(3):
        cely_stlpec = True
        for riadok in range(3):
            if hracie_pole[riadok][stlpec] != hrac:
                cely_stlpec = False
                break
        if cely_stlpec:
            return True
    return False

def kontrolaDiagonalne(hrac, hracie_pole):
    if hracie_pole[0][0] == hrac and hracie_pole[1][1] == hrac and hracie_pole[2][2] == hrac:
        return True
    elif hracie_pole[0][2] == hrac and hracie_pole[1][1] == hrac and hracie_pole[2][0] == hrac:
        return True
    else:
        return False

while pocet < 9:
    aktivny_hrac = aktualny_hrac(hrac)
    vypisHraciehoPola(hracie_pole)
    zadanie_cisla = input('zadaj poziciu od 1 po 9 alebo \"koniec\" pre ukoncenie: ')
    if koniec(zadanie_cisla):
        break
    if not kontrolaVstupu(zadanie_cisla):
        print('Prosim skuste znova')
        continue
    zadanie_cisla = int(zadanie_cisla) - 1
    poloha = suradnice(zadanie_cisla)
    if kontrolaHraciehoPola(poloha, hracie_pole):
        print('Skus este raz')
        continue
    pridajDoPola(poloha, hracie_pole, aktivny_hrac)
    if kontrolaVyhry(aktivny_hrac, hracie_pole):
        print(f"{aktivny_hrac.upper()} won!")
        vypisHraciehoPola(hracie_pole)
        break

    pocet += 1
    if pocet == 9:
        print('Remiza!')
        vypisHraciehoPola(hracie_pole)
    hrac = not hrac