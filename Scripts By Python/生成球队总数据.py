import csv

print("hello world")


def getBlankRowList():
    listRowNew = [1, -1, 82, 241.8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # 25
    return listRowNew


listFinal = []  # 用来保存输出的
'''
FG = 0
FGA = 0
FG010 = 0
P3 = 0
P3A = 0
P3010 = 0
P2 = 0
P2A = 0
P2010 = 0
FT = 0
FTA = 0
FT010 = 0
ORB = 0
DRB = 0
TRB = 0
AST = 0
STL = 0
BLK = 0
TOV = 0
PF = 0
PTS = 0
'''
with open('../../res/teamData.csv', 'r', encoding="utf-8") as csvFile:
    read = csv.reader(csvFile)
    isFirst = True
    listRow = []
    teamID = -1
    for item in read:

        if isFirst:  # 去除第一行
            isFirst = False
            continue

        if int(item[1]) == 0:
            # save firstly
            listFinal.append(listRow)
            listRow = getBlankRowList()

        if int(item[0]) == 208:
            break;

        listRow[1] = int(item[0])  # 队名
        listRow[4] = listRow[4] + float(item[6])  # 投球命中次数
        listRow[5] = listRow[5] + float(item[7])  # 投射次数
        try:
            listRow[6] = listRow[4] / listRow[5]  # 投球命中次数
        except ZeroDivisionError as e:
            listRow[6] = 0
        listRow[7] = listRow[7] + float(item[9])  # 三分球命中次数
        listRow[8] = listRow[8] + float(item[10])  # 三分球投射次数
        try:
            listRow[9] = listRow[7] / listRow[8]  # 三分球命中率
        except ZeroDivisionError as e:
            listRow[9] = 0
        listRow[10] = listRow[10] + listRow[5] - listRow[8]  # 二分球命中次数
        listRow[11] = listRow[11] + listRow[6] - listRow[9]  # 二分球投射次数
        try:
            listRow[12] = listRow[10] / listRow[11]  # 二分球命中率
        except ZeroDivisionError as e:
            listRow[12] = 0
        listRow[13] = listRow[13] + float(item[12])  # 罚球命中次数
        listRow[14] = listRow[14] + float(item[13])  # 罚球投射次数
        try:
            listRow[15] = listRow[13] / listRow[14]  # 罚球命中率
        except ZeroDivisionError as e:
            listRow[15] = 0
        listRow[16] = listRow[16] + float(item[15])  # 进攻篮板球
        listRow[17] = listRow[17] + float(item[16])  # 防守篮板球
        listRow[18] = listRow[18] + float(item[14])  # 篮板球总数
        listRow[19] = listRow[19] + float(item[17])  # 助攻
        listRow[20] = listRow[20] + float(item[18])  # 抢断
        listRow[21] = listRow[21] + float(item[19])  # 封盖
        listRow[22] = listRow[22] + float(item[20])  # 失误
        listRow[23] = listRow[23] + float(item[21])  # 个犯
        listRow[24] = listRow[24] + float(item[22])  # 得分

outFile = open('Team_Per_Game_Stat.csv', 'w', newline='')  # 设置newline，否则两行之间会空一行
writer = csv.writer(outFile)
for i in range(len(listFinal)):
    writer.writerow(listFinal[i])
outFile.close()
