otazkaSiStastny = input("Si stastny? ")
otazkaSiBohaty = input("Si bohaty? ")

if(otazkaSiStastny == "ano"):
    if(otazkaSiBohaty == "ano"):
        print("gratulujem")
    else:
        print("skus viac setrit")
else:
    if otazkaSiBohaty == "ano":
        print("skus sa viac usmievat")
    else:
        print("sorry je mi to luto")
