list1 = ['a', 'b', 'c']

for i in range(pocet_suborov):
    open('%s.txt' % i, 'w', encoding='UTF-8').write(list[i])