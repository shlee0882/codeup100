# in 1234567 

a = input()
list1 = list(a)


for idx, val in enumerate(list1):
    while idx < len(list1)-1:
        val = val + '0'
        idx +=1
    print("["+val+"]")
