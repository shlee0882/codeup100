from sys import stdin
a, b, c, d = list(map(int, stdin.readline().split()))

# byte value
e = round(round(((a * b * c * d) / 8)/1024,1)/1024,1)

print(str(e)+" MB")

