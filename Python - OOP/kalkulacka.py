class Calc:
    def sucet(self):
        return print("Sucet:", a + b)

    def rozdiel(self):
        return print("Rozdiel:", a - b)
    
    def sucin(self):
        return print("Sucin:", a * b)
    
    def podiel(self):
        return print("Podiel:", a / b)


kalkulacka = Calc()
a = int(input("zadaj 1. cislo: "))
b = int(input("zadaj 2. cislo: "))

kalkulacka.sucet()
kalkulacka.rozdiel()
kalkulacka.sucin()
kalkulacka.podiel()