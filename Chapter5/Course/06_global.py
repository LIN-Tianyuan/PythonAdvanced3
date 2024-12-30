num = 100

def testA():
    print(num)

def testB():
    global num
    num = 200
    print(num)


testA()         # 100
testB()         # 200
# print(num)      # 100
print(num)      # 200
