import random

pridavne_mena = ["velky", "automatizovany", "hubeny", "modry", "najlepsi"]
podstatne_mena = ["programator", "manazer", "hroch", "jednorozec"]
prislovky = ["s oblibou", "malo", "vela", "rychlo"]
slovesa = ["spal", "upratoval", "derivoval", "varil"]
prislovky_miesta = ["v lese", "u babky", "na stole", "pod stolom"]

class Generator:
    def generovanieViet(self):
        vyber_podst_mien = random.choice(podstatne_mena)
        vyber_prid_mien = random.choice(pridavne_mena)
        vyber_prislovky = random.choice(prislovky)
        vyber_slovesa = random.choice(slovesa)
        vyber = random.choice(prislovky_miesta)
        return print(f"{vyber_prid_mien} {vyber_podst_mien} {vyber_prislovky} {vyber_slovesa} {vyber}")
    
vety = Generator()
for i in range(10):
    vety.generovanieViet()