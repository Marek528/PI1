"""
for riadok in range(1,5):
    for stlpec in range(1, riadok):
        print(stlpec)

1
2
3
4

1-2 = 1
1-3 = 1 2
1-4 = 1 2 3

1
1
2
1
2
3
"""

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
zoradene = sorted(arr)
premenna = max(zoradene)
for i in zoradene:
    if i == premenna:
        continue
    print(i)
    break
