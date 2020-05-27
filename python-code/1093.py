from sys import stdin
a = int(stdin.readline())
b = list(map(int,stdin.readline().split()))

c = 24
arr = []

if a == len(b):    
    for i in range(1,c):
        arr.append(b.count(i))
else:
    print("재입력")

for i in arr:
    print(i, end = ' ')

