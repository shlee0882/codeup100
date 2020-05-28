from sys import stdin

c, r = list(map(int, stdin.readline().split()))
s = [[0 for col in range(r)] for row in range(c)]
b = int(stdin.readline())
c = []
#c = [[2, 0, 1, 1],[3, 1, 2, 3], [4, 1, 2, 5]]

i,x,y = 0, 0, 0
while i < b:
    c.append(list(map(int, stdin.readline().split())))
    i += 1

for i in c:
    x = i[2]-1
    y = i[3]-1
    s[x][y] = 1


    if i[0] > 1:
        for k in range(0,i[0]):
            # right direction
            if i[1] == 0:
                s[x][y+k] = 1
            elif i[1] == 1:
                s[x+k][y] = 1
         
for i in s:
    print(*i)
