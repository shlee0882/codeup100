from sys import stdin

a,b,c = list(map(int, stdin.readline().split()))

for i in range(c-1):
    a += b

print(a)
