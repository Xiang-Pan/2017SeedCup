import csv

print("hello world")

listFinal = []  # 用来保存输出的

with open('../../res/teamData.csv', 'r', encoding="utf-8") as csvFile:
    read = csv.reader(csvFile)
    isFirst = True
    tmAST = 0
    tmFG = 0
    for item in read:

        listRow = []  # 保存单行数据
        if isFirst:  # jump out from the first one
            isFirst = False
            continue

        if int(item[1]) == 0:  # 如果是球队一号
            listRow = [tmAST, tmFG]
            listFinal.append(listRow)
            tmAST = 0
            tmFG = 0

        tmAST = tmAST + float(item[17])
        tmFG = tmFG + float(item[6])

outFile = open('TeamData2.csv', 'w', newline='')  # 设置newline，否则两行之间会空一行
writer = csv.writer(outFile)
for i in range(len(listFinal)):
    writer.writerow(listFinal[i])
outFile.close()
