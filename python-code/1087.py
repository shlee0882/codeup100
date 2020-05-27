from sys import stdin
a = int(stdin.readline())
j = 0

for i in range(1,a+1):
    if j < a:
        j += i
    else:
        break
print(j)
