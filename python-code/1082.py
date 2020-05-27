a = int(input(),16)
b = hex(a)[2:].upper()


for i in range(1,16):
    c = hex(i)[2:].upper()
    d = hex(a*i)[2:].upper()
    print(str(b)+"*"+str(c)+"="+str(d))
