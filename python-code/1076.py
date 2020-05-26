a = input();

a = ord(a)

arr = []

i = 97
while i <= int(a):
    alphabet = chr(i)
    arr.append(alphabet)
    i += 1

for i in arr:
    print(i, end=" ")    
