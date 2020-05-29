from sys import stdin

i = 0
a = []

while i < 10:
    a.append(list(map(int, stdin.readline().split())))
    i += 1

'''
a = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 1, 1, 1, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
[1, 0, 0, 0, 0, 1, 0, 1, 0, 1],
[1, 0, 0, 0, 0, 1, 2, 1, 0, 1],
[1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ]
'''

cu = []
cu.append([1,1])

s1 = 0

s = 1
e = 1

while s1 <= 0 :

    ar = cu.pop()
    x, y = ar[0], ar[1]

    if a[x][y] == 2:
        a[x][y] = 9
        break
    else:
        a[x][y] = 9

    if a[x][y+1] == 2:
        a[x][y+1] = 9
        break
    else:
        if a[x][y+1] == 0:
            a[x][y+1] = 9
            cu.append([x,y+1])
        elif a[x+1][y] == 0:
            a[x+1][y] = 9
            cu.append([x+1,y])
        elif a[x][y+1] == 2:
            a[x][y+1] = 9
            break
        elif a[x+1][y] == 2:
            a[x+1][y] = 9
            break
        else:
            s1 = 1
        
    
for i in a:
    print(*i)
