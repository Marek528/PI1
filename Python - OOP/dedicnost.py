class Zvieratko:
    def __init__(self, name):
        self.name = name
    
    def eat(self, jedlo):
        print(f"{self.name}: {jedlo} mi chutí!")

# Inherit - dedenie
# Dedim od Zvieratka jeho metody
class Macka(Zvieratko):    
    def do_sound(self):
        print(f"{self.name}: Mňau!")

    def eat(self, jedlo):
        super().eat('Sunka')
        print(f"{self.name}: {jedlo} vyplula!")

class Pes(Zvieratko):
    def do_sound(self):
        print(f"{self.name}: Haf!")

macka = Macka('Micka')
pes = Pes('Falko')

macka.eat('Šunka')
#macka.zamnaukaj()

pes.eat('Granule')
#pes.zastekaj()

# POLYMORFIZMUS
zvieratka = [Macka('Naginy'), Pes('Azor')]

for zvieratko in zvieratka:
    zvieratko.eat('Granulka')
    zvieratko.do_sound()
# Generalizacia
