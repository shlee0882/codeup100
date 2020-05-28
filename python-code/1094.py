from sys import stdin
a = int(stdin.readline())
b = list(map(int,stdin.readline().split()))

arr = []

if a == len(b):    
    for i in range(len(b)):
        arr.append(b[i])
else:
    print("재입력")

for i in range(1,len(arr)+1):
    print(arr[len(arr)-i], end=' ')
