zoznam_prazdny = []
zoznam_cisel = [1,5,8,9,15]
zoznam_pismen = ['a','t','r']
zoznam_mix = ["slovo",14,'a','!', 55]

zoznam_cisel[0] = 99999
print(zoznam_cisel[4])
print(zoznam_pismen[2])
print(zoznam_mix[-1])

print("---------------")
print(zoznam_pismen)
print(zoznam_mix)
print(zoznam_cisel)


zoznam = list()
print(zoznam)
zoznam_range = list(range(3, 7))
print(zoznam_range)

#orezavanie
neorezany_zoznam = list(range(10))
print(neorezany_zoznam)

print(neorezany_zoznam[0:5])
print(neorezany_zoznam[2:8])
print(neorezany_zoznam[1:7:2])
print(neorezany_zoznam[2:9:3])


#velkost/ kolko prvkov obsahuje zoznam
x = [5,8,1,3,"slovo"]
print(len(x))

#prechadzanie zoznamu
zoznam_prvkov = ["jablko", "hruska", "banan"]
#1.
for prvok in zoznam_prvkov:
    print(prvok)

#2.
for index in range(len(zoznam_prvkov)):
    print(zoznam_prvkov[index])


#metody zoznam
mylist = [1,5,8,55,500]

#append/ prida na koniec listu novy prvok
mylist.append(99)
mylist.append(1)
mylist.append(0)
print(mylist)

#pop
hodnota = mylist.pop()
print(mylist)
print(hodnota)




#funkcie
#len
#min/max
mylist2 = [1,54,7,2,74,-10]
print("minimum", min(mylist2))
print("maximum", max(mylist2))
#suma / spocita prvky zoznamu
print("suma", sum(mylist2))

print(mylist2)
#otoci list naopak
print(sorted(mylist2))
