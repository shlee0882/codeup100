# 1019 : [기초-입출력] 연월일 입력받아 그대로 출력하기 해결
x, y, z = input().split(".")
x = int(x)
y = int(y)
z = int(z)
print('%04d' % x, '%02d' % y, '%02d' % z, sep='.')
