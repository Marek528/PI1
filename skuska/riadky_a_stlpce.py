riadky= int(input('zadaj pocet riadkov: '))
stlpce = int(input('zadaj pocet stlpcov: '))

for i in range(0, stlpce):
    for j in range(0, riadky):
        print('*', end="")
    print()
