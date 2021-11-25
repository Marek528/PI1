"""
riadky= int(input('zadaj pocet riadkov: '))
stlpce = int(input('zadaj pocet stlpcov: '))

for i in range(0, stlpce):
    for j in range(0, riadky):
        print('*', end="")
    print()
"""

"""
string = "Informatika s Mišom"
print(string[5:8] + 'e' + string[5:8] + string[8:12])
"""

print('1 - scitanie')
print('2 - odcitanie')
print('3 - nasobenie')
print('4 - delenie')
print('5 - mocniny')
print('6 - odmocnovanie')

vyber = int(input('vyber si moznost od 1 - 5: '))
a = int(input('zadaj hodnotu a: '))
b = int(input('zadaj hodnotu b: '))

if vyber == 1:
    vysledok = a+b
    print('vysledok scitania je:', vysledok)
elif vyber == 2:
    vysledok = a-b
    print('vysledok odcitania je:', vysledok)
elif vyber == 3:
    vysledok = a*b
    print('vysledok nasobenia je:', vysledok)
elif vyber == 4:
    if b == 0:
        print('0 sa delit neda')
    else:
        print('vysledok delenia je:', a/b)
elif vyber == 5:
    vysledok = a**b
    print('vysledok mocniny je:', vysledok)
elif vyber == 6:
    vysledok = a ** 1/b
    print('vysledok umocnovania je:', vysledok)
else:
    print('prosim vyber cislo medzi 1 - 5')
