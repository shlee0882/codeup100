a = int(input())

for i in range(1, a+1):
    if i%3 == 0:
        if i%33 == 0:
            print('XX', end=' ')
        else:
            print('X', end=' ')
    else:
        print(i, end=' ')
