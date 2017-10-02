import csv

print("hello world")


ScoreHomeUP = 0.02  # 可以做线性递增调参

listFinal = []

with open('../../res/matchDataTrain.csv', 'r', encoding="utf-8") as csvFile:
    read = csv.reader(csvFile)
    isFirst = True
    for item in read:
        if isFirst:  # jump out from the first one
            isFirst = False
            continue;

        listRow = [item[0], item[1]]

        # 获得比分的前后
        scoreList = str(item[4]).split(':')
        listRow.append(scoreList[0])

        advancedScoreHome = int(scoreList[1]) * (1-ScoreHomeUP)
        listRow.append(advancedScoreHome)

        # 获得客场历史战绩
        history = str(item[2])
        history = history.replace('负', '')
        historyList = history.split("胜")
        listRow.append(historyList[0])
        listRow.append(historyList[1])

        # 获得主场历史战绩
        history = str(item[3])
        history = history.replace('负', '')
        historyList = history.split("胜")
        listRow.append(historyList[0])
        listRow.append(historyList[1])

        # 存到listFinal中
        listFinal.append(listRow)

csvFile.close()

# 写入
TestFile = open('TEST.csv', 'w', newline='')  # 设置newline，否则两行之间会空一行
writerTest = csv.writer(TestFile)
TrainFile = open('TRAIN.csv', 'w', newline='')  # 设置newline，否则两行之间会空一行
writerTrain = csv.writer(TrainFile)
m = len(listFinal)
for i in range(m):
    if i > 5600:
        writerTest.writerow(listFinal[i])
    else:
        writerTrain.writerow(listFinal[i])

TestFile.close()
TrainFile.close()
input("Enter the any press to exit")