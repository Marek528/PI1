class Person:
    def __init__(self, name):
        self.unava = 0
        self.name = name
        print(self)
    
    def __str__(self):
        return self.name + " ma unavu: " + str(self.unava)

    def run(self, kilometre):
        if self.unava + kilometre <= 20:
            self.unava += kilometre
            print(f"Ubehol {kilometre} km")
        else:
            print("Je prilis unaveny")
        print(self)
        
    def sleeping(self, hours):
        self.unava -= 10 * hours
        print(f"Spal {hours} hodin")

        if self.unava < 0:
            self.unava = 0
        print(self)

clovek = Person("Marek")
clovek.run(10)
clovek.run(10)
clovek.run(10)
clovek.sleeping(1)
clovek.run(10)