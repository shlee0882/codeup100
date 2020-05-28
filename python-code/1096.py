from sys import stdin
a = int(stdin.readline())
b = []
tmp = []

i = 0

c1 = 19
r1 = 19


c = [[0 for col in range(c1)] for row in range(r1)]

while i < a:
    b.append(list(map(int, stdin.readline().split())))
    i += 1

for j in b:
    first = j[0]-1
    second = j[1]-1
    c[first][second] = 1


for i in c:
    print(*i)
