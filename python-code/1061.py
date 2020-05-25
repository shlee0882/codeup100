a,b = input().split()
a = int(a)
b = int(b)

a = bin(a)
a1 = int(a, 2)

b = bin(b)
b1 = int(b, 2)

c = bin(a1 | b1)


d = int(c,2)
print(d)
