pocet_suborov = int(input('zadaj pocet suborov: '))
list = []

with open ('./basnicka.txt', encoding='UTF-8') as subor:
    for riadok in subor:
        list += riadok.split()

dlzka_basne = len(list)
x = 0
for i in range(pocet_suborov):
    if i >= dlzka_basne:
        x = i - dlzka_basne
    open('%s.txt' % i,'w', encoding='UTF-8').write(list[x])
