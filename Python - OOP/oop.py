"""
#Trieda Macka
class Cat:
    # knostruktor -> vykona sa vzdy ked vytvaram instanciu triedy
    def __init__(self, meno, vek):
        print("Vytvaram objekt macky")
        self.name = meno
        self.vek = vek

    def __str__(self):
        print("Meno macky je :", self.name)
        print("vek macky je: ", str(self.vek))
        return "  "

    def zamnaukaj(self):
        print(self.name + " mňau")
    
    def zjedz(self, jedlo):
        print(self.name + " zjedla/zjedlo " + jedlo)

# vytvorenie instancie objektu macku
cat = Cat("Mica", 4)
#cat.meno = "Cica"

# volanie metody
cat.zamnaukaj()
cat.zjedz("rybu")

cat2 = Cat("Murko", 5)
#cat2.meno = "Murko"
cat2.zamnaukaj()

print(cat2)
"""

class Auto:
    def __init__(self, znacka, rok, farba, pocet_miest, jeNastartovane):
        self.znacka = znacka
        self.rok = rok
        self.farba = farba
        self.pocet_miest = pocet_miest
        self.jeNastartovane = False

    def __str__(self):
        print("Znacka auta je: ",self.znacka)
        print("Rok vyroby je: ",self.rok)
        print("Farba auta je: ",self.farba)
        print("Pocet miest v aute je:", self.pocet_miest)
        return " "

    def zapniMotor(self, state):
        self.zapniMotor = state

    def chodDoPredu(self):
        print(self.znacka + " ide do predu")

    def zatrub(self):
        print(self.znacka + " TUTUU!")
    
auto = Auto("BMW", 2017, "modra", 5, True)
auto.zatrub()
auto.chodDoPredu()
auto.zapniMotor(True)
print(auto)
auto.zapniMotor(False)
print(auto)