from sys import stdin

a,b,c,d = list(map(int, stdin.readline().split()))

for i in range(d-1):
    a *= b
    a += c

print(a)
