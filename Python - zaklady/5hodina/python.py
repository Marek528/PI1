def scitaj(a , b):
    vysledok = a+b
    return vysledok

vysledok = scitaj(scitaj(5,6),scitaj(12,1))
print(vysledok)