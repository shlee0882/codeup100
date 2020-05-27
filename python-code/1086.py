from sys import stdin
a, b, c  = list(map(int, stdin.readline().split()))

# byte value
d = round(round(((a * b * c) / 8)/1024,2)/1024,2)

print('%.2f' % d + " MB")
