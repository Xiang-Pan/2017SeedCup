import csv

print("hello world")

listFinal = []  # 用来保存主场球队
with open('../../res/UploadTrain.csv', 'r', encoding="utf-8") as csvFile:  # 提交版模板
    read = csv.reader(csvFile)
    isFirst = True
    for item in read:
        listRow = []
        if isFirst:  # 去除第一行
            isFirst = False
            continue
        listFinal.append(int(item[1]))

listOut = []
indexForFinal = 0
with open('../../res/Result.csv', 'r', encoding="utf-8") as csvFile:
    read = csv.reader(csvFile)
    isFirst = True
    for item in read:
        listRow = []
        if isFirst:  # 去除第一行
            isFirst = False
            continue
        if int(item[0]) != listFinal[indexForFinal]:  # 该置信度非主场球队
            listOut.append(1 - float(item[2]))
        else:
            listOut.append(float(item[2]))
        indexForFinal = indexForFinal + 1

outFile = open('upload/predictPro.csv', 'w', newline='')  # 设置newline，否则两行之间会空一行
writer = csv.writer(outFile)
for i in range(len(listOut)):
    writer.writerow([listOut[i]])  # 这里的写入类型应该是列表
outFile.close()
