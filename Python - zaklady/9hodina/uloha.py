"""
prvy_riadok = ["█", " ", "█", " ", "█", " ", "█", " "]
druhy_riadok = [" ", "█", " ", "█", " ", "█", " ", "█"]

for i in range(4):
    for prvok in prvy_riadok:
        print(prvok, end= "")
    print(sep= "")
    for j in druhy_riadok:
        print(j, end= "")
    print("")
"""

sachovnica = [
    ["█", " ", "█", " ", "█", " ", "█", " "],
    [" ", "█", " ", "█", " ", "█", " ", "█"],
    ["█", " ", "█", " ", "█", " ", "█", " "],
    [" ", "█", " ", "█", " ", "█", " ", "█"]
]

for riadok in sachovnica:
    for policko in riadok:
        print(policko, end= "")
    print()