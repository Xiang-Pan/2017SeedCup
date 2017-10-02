import csv

print("hello world")

listFinal = []  # 用来保存输出的

with open('TRAIN.csv', 'r', encoding="utf-8") as csvFile:
    read = csv.reader(csvFile)
    # isFirst = True
    teamID = -1
    for item in read:
        listRow = []
        # if isFirst:  # 去除第一行
        #     isFirst = False
        #     continue
        if float(item[2]) > float(item[3]):
            listRow.append(item[0])  # 主队胜利
            listRow.append(item[1])
            listRow.append('V')
        else:
            listRow.append(item[1])  # 客队胜利
            listRow.append(item[0])
            listRow.append('H')
        listFinal.append(listRow)

outFile = open('result.csv', 'w', newline='')  # 设置newline，否则两行之间会空一行
writer = csv.writer(outFile)
for i in range(len(listFinal)):
    writer.writerow(listFinal[i])
outFile.close()
