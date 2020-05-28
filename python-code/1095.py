from sys import stdin
a = int(stdin.readline())
b = list(map(int, stdin.readline().split()))

arr = []

if a==len(b):
    for i in range(len(b)):
        arr.append(b[i])

if len(arr):
    arr.sort()
    print(arr[0])
