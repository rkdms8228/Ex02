# List
testList = [1, 2, 'python']  # testList =[]  # testList=list()

print(testList[0], testList[1], testList[2])
print(testList[-1], testList[-2])

testList = testList[1:3]
print(testList[1:3])
print(testList * 2)
print(testList + [3, 4, 5])
print(len(testList))

print(2 in testList)

print("===================================")

# 리스트 삭제하는 법
# del(testList[0])
print(testList)

print("===================================")

# 리스트 수정하는 법
testList[0] = "일"
print(testList)

aList = ['apple', 'banana', 10, 20]
aList[2] = aList[2] + 90
print(aList)

print("===================================")

bList = [1, 12, 123, 1234]
bList[0:2] = [10, 20]
print(bList)

bList[0:2] = [10]
print(bList)

bList[1:2] = [20]
print(bList)

bList[2:3] = [30]
print(bList)

print("===================================")

cList = [1, 12, 123, 1234]
cList[1:2] = []
print(cList)

cList[0:2] = []
print(cList)

print("===================================")

dList = [1, 12, 123, 1234]
# dList[1:2] = "a"      # 변경
dList[1:1] = "a"        # 같은 숫자면 변경
print(dList)

dList[5:] = [12345]
print(dList)

dList[:0] = [12, -1, 0]
print(dList)

print("===================================")

a = [1, 12, 123, "hello", 3.14, 1000]
print(a)

# 추가
a.append(5)
print(a)

a.insert(3, 1000)
print(a)

a.extend([6, 7, 8])
print(a)

# 제거
a.remove(1000)
print(a)

a.pop(2)
print(a)

a.pop()
# del(a[4])

print("===================================")

b = [1, 123, 1000, 12, 1000]
print(b)

# b[5:] = [1,2,3]
# b.insert(5, [1,2,3])
# print(b[5][1])

# 카운트
print(len(b))
print(b.count(1000))

# 뒤집기
b.reverse()
print(b)

# 정렬
b.sort()
print(b)

# index
print(b.index(1000))  # 여러 개일 때는 첫 번째