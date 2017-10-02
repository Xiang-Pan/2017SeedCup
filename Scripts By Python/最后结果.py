import csv

print("hello world")

listFinal = []  # 用来保存输出的

with open('../../res/16-17Result.csv', 'r', encoding="utf-8") as csvFile:
    read = csv.reader(csvFile)
    isFirst = True
    for item in read:
        if isFirst:  # 去除第一行
            isFirst = False
            continue
        listFinal.append(item[0])

listTest = []
with open('TEST.csv', 'r', encoding="utf-8") as csvFile:
    read = csv.reader(csvFile)
    # isFirst = True
    for item in read:
        # if isFirst:  # 去除第一行
        #     isFirst = False
        #     continue
        if float(item[2]) > float(item[3]):  # 存入胜队，再与前面的列表进行比较
            listTest.append(item[0])
        else:

            listTest.append(item[1])

right = 0
for i in range(len(listFinal)):
    if int(listTest[i]) == int(listFinal[i]):
        right = right + 1

print(right)  # 输出正确的个数
