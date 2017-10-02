import csv


def findDetail(listReturn, name):
    with open('15-16Team_Per_Game_Stat.csv', 'r', encoding="utf-8") as DetailFile:
        readerIn = csv.reader(DetailFile)
        First = True
        for itemIn in readerIn:
            if First:
                First = False
                continue
            if int(name) == int(itemIn[1]):
                listReturn.append(int(itemIn[0]))
                for a in range(4, 25):
                    listReturn.append(float(itemIn[a]))
                break


listFinal = []
with open('schedule.csv', 'r', encoding="utf-8") as csvFile:
    read = csv.reader(csvFile)

    for item in read:
        listRow = [item[0], item[1]]

        # 获得比分的前后
        # scoreList = str(item[4]).split(':')
        # listRow.append(scoreList[0])

        # advancedScoreHome = int(scoreList[1]) * 1
        # listRow.append(advancedScoreHome)

        # 添加球队详细数据
        listDetailV = []
        listDetailH = []
        findDetail(listDetailV, int(item[0]))
        findDetail(listDetailH, int(item[1]))
        for j in range(len(listDetailV)):
            listRow.append(listDetailV[j])
        for k in range(len(listDetailH)):
            listRow.append(listDetailH[k])

        # # 获得客场历史战绩
        # history = str(item[2])
        # history = history.replace('负', '')
        # historyList = history.split("胜")
        # listRow.append(historyList[0])
        # listRow.append(historyList[1])
        #
        # # 获得主场历史战绩
        # history = str(item[3])
        # history = history.replace('负', '')
        # historyList = history.split("胜")
        # listRow.append(historyList[0])
        # listRow.append(historyList[1])

        # 存到listFinal中
        listFinal.append(listRow)

csvFile.close()

# 写入
TrainFile = open('ScheduleHover.csv', 'w', newline='')  # 设置newline，否则两行之间会空一行
writerTrain = csv.writer(TrainFile)
m = len(listFinal)
for i in range(m):
    writerTrain.writerow(listFinal[i])

TrainFile.close()
