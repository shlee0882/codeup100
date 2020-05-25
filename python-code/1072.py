a = int(input())
b = input().split()

if len(b) == a:
    for i in b:
        print(i)
else:
    print('재입력')
