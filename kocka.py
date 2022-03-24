import random

hrany = int(input("zadaj pocet hran: "))

class Cube:
    def __init__(self, hrany):
        self.hrany = hrany

    def hodKockou(self):
        return random.randint(1, self.hrany)

print("Kocka s", hrany, "hranami")
kocka = Cube(hrany)
for i in range(10):
    print(kocka.hodKockou(), end= ' ')