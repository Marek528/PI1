pocet_suborov = int(input('zadaj pocet suborov: '))
list = []

with open('./7hodina/basnicka.txt', encoding='UTF-8') as subor:
    for riadok in subor:
        list += riadok.split()

dlzka_basne = len(list)
x = 0
for i in range(pocet_suborov):
    if i >= dlzka_basne:
        x = i - dlzka_basne
    open('./7hodina/%s.txt' % i, 'w', encoding='UTF-8').write(list[x])
    x += 1 
