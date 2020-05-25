x = int(input())

a = bin(x)
b = int(a, 2)

c = bin(~x)

d = int(c, 2)
print(d)

