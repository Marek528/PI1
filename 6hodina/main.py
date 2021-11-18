"""
domy = [4, 2, 0, 5, 0, 1, 5, 4]

i = 0

for i in domy:
    neobyvane_domy = domy.count(0)
    max_pocet = domy.count(max(domy))
    

print('pocet obyvatelov je', sum(domy))
print('neobyvanych domov je', neobyvane_domy)
print('maximalny pocet obyvatelov v dome je', max(domy))
print('pocet maximalnych domov je', max_pocet)
"""


domy = [1,5,0,8,9,2,4,5,3,7,4,1,2,5,0]

i = 0

for i in domy:
    neobyvane_domy = domy.count(0)
    max_pocet = domy.count(max(domy))
    

print('pocet obyvatelov je', sum(domy))
print('neobyvanych domov je', neobyvane_domy)
print('maximalny pocet obyvatelov v dome je', max(domy))
print('pocet maximalnych domov je', max_pocet)
