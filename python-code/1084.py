from sys import stdin
a, b, c = list(map(int, stdin.readline().split()))

d = 0

for i in range(a):
    for j in range(b):
        for k in range(c):
            d+=1
            print(i,j,k)
            
print(d)
