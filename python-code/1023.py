# 1023 : [기초-입출력] 실수 1개 입력받아 부분별로 출력하기(설명) 
x = float(input())
split_num = str(x).split('.')
print(split_num[0])
print(split_num[1])