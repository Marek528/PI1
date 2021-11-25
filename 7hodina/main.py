pocet_suborov = int(input('zadaj pocet suborov: '))

list = []

with open ('./7hodina/basnicka.txt', encoding='utf-8') as subor:
    for riadok in subor:
        list += riadok.split()

for i in range(1):
    with open ('./7hodina/text.txt', mode='w', encoding='utf-8') as subor1:
        print(list[0], file=subor1)

