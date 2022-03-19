
cisla = [4,5,6,7]
print(cisla[0])

pole = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(pole[1][1])
pole[0].append(99)
print("--------------------")
for riadok in pole:
    print(riadok)
    for prvok in riadok:
        print(prvok)

print("----------------------")


def vypisKinosalu(kinosalu):
    for riadok in kinosala:
        print(riadok)


#start programu
kinosala = []

for i in range(5):
    temp = []
    for i in range(10):
        temp2 = []
        for i in range(4):
            temp2.append(0)
        temp.append(temp2)
    kinosala.append(temp)

print(kinosala)

vypisKinosalu(kinosala)    
kinosala[0][5] = 1
kinosala[2][4] = 1
kinosala[1][3] = 1
vypisKinosalu(kinosala)


