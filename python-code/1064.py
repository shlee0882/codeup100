a,b,c = input().split()
a = int(a)
b = int(b)
c = int(c)

# 5 15 10
d = a < b and a < c and a or b < a and b < c and b or c < a and c < b and c or a
print(d)
