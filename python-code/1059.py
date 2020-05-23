x = int(input())
x2 = '00'
x2 += format(x, 'b')

print(x2)

convert = "0b"

for i in list(x2):
    if i=='0':
        convert += '1'
    elif i=='1':
        convert += '0'

convert2 = int(convert, 2)
print(convert2)
    

