from sys import stdin

a,b,c = list(map(int, stdin.readline().split()))
day = 1

while day%a != 0 or day%b != 0 or day%c != 0 :
    day += 1

print(day)
