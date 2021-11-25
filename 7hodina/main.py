pocet_suborov = int(input('zadaj pocet suborov: '))

list = []

with open ('./basnicka.txt', encoding='utf-8') as subor:
    for riadok in subor:
        list += riadok.split()

for i in range(pocet_suborov):
    open('%s.txt' % i, 'w').write(list[i])

