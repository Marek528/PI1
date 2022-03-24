class Calc:
    def sucet(self):
        return a + b

    def rozdiel(self):
        return a - b
    
    def sucin(self):
        return a * b
    
    def podiel(self):
        return a / b


kalkulacka = Calc()
a = int(input("zadaj 1. cislo: "))
b = int(input("zadaj 2. cislo: "))

kalkulacka.sucet()
kalkulacka.rozdiel()
kalkulacka.sucin()
kalkulacka.podiel()