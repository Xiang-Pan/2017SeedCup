import csv

print("hello world")

listFinal = []  # 用来保存输出的

with open('../../res/UploadTrain.csv', 'r', encoding="utf-8") as csvFile:
    read = csv.reader(csvFile)
    isFirst = True
    for item in read:
        listRow = []
        if isFirst:  # 去除第一行
            isFirst = False
            continue

        listRow.append(item[0])
        listRow.append(item[1])
        listFinal.append(listRow)

outFile = open('schedule.csv', 'w', newline='')  # 设置newline，否则两行之间会空一行
writer = csv.writer(outFile)
for i in range(len(listFinal)):
    writer.writerow(listFinal[i])
outFile.close()
