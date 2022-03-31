class Car:
    def __init__(self, SPZ, color):
        self.SPZ = SPZ
        self.color = color
    
    def zaparkuj(self, garage):
        garage.cars_in_garage.append("{0} {1}".format(self.SPZ, self.color))

    def vyparkuj(self, garage):
        pass

class Garage:

    cars_in_garage = []

    def vypis_aut(self):
        if self.cars_in_garage == []:
            print("Garaz je prazdna")
        else:
            print("V garazi su auta: {}".format(', '.join(self.cars_in_garage)))

garaz = Garage()
bmw = Car("123ABC", "modre")
bmw.zaparkuj(garage)
audi = Car("987DPI", color)
audi.zaparkuj(garage)
renault = Car("456LAM", "zlta")
renault.zaparkuj(garage)
