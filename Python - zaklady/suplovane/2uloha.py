import random
skupinaA = []
skupinaB = []
skupinaC = []

while True:
    skupina = random.randrange(0,3)
    meno = input('zadaj meno: ')
    if meno == 'koniec':
        break
    if skupina == 0:
        skupinaA.append(meno)
    elif skupina == 1:
        skupinaB.append(meno)
    elif skupina == 2:
        skupinaC.append(meno)

    print('skupina A: ', skupinaA)
    print('skupina B: ', skupinaB)
    print('skupina C: ', skupinaC)