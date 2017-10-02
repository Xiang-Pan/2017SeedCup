import csv
import numpy as np

'''             
可以临时计算 ：/tmFG，球队助攻总数/球队命中总数 tmAST/tmFG，球队助攻数/球队命中数
'''

print("hello world")
lgAST = 364718.8
lgFG = 625204.8
lgFT = 1378642.5
LgPTS = 9.599483741893954
lgFGA = 7.9257835855217715
lgORB = 1.0323144230326975
lgTO = 1.3148358092259547
lgFTA = 1.6748677735363129
LgTRB = 4.077040311824487
DRBP = 3.0480217771236817
lgFT_fault = 1.6748677735363129
lgFTA = lgFT_fault
lgPF = 1.9255915697006025

# 本块功能为把球队两数据保存进listTeam
listTeam = []
with open('TeamData.csv', 'r', encoding="utf-8") as csvFile:
    read = csv.reader(csvFile)
    for item in read:
        listRow = [float(item[0]), float(item[1])]
        listTeam.append(listRow)

listFinal = []  # 用来保存输出的

with open('../../res/teamData.csv', 'r', encoding="utf-8") as csvFile:
    read = csv.reader(csvFile)
    isFirst = True
    # factor = (2 / 3) - (0.5 * (lgAST / lgFG)) / (2 * (lgFG / lgFT))
    index = 1
    for item in read:

        listRow = []  # 保存单行数据
        if isFirst:  # jump out from the first one
            isFirst = False
            continue

        for k in range(23):
            listRow.append(item[k])  # 把整行的原始数据存进去

        if int(item[1]) == 0:  # 如果是球队第一人，把球队助攻，球队得分存入该行
            if index != 208:
                listRow.append(listTeam[index][0])  # 24
                listRow.append(listTeam[index][1])  # 25
                index = index + 1  # 把球队数据往后移动，方便存入 listFinal

        listFinal.append(listRow)

            # factor = (2 / 3) - (0.5 * (lgAST / lgFG)) / (2 * (lgFG / lgFT))
            # uPER = float(1 / i[4])
            # item = 0
            # item = float(i[10]) + 2 / 3 * float(i[17]) + (2 - factor * tmAST / tmFG) * int(i[6])

outFile = open('teamDataAdvanced.csv', 'w', newline='')  # 设置newline，否则两行之间会空一行
writer = csv.writer(outFile)
for i in range(len(listFinal)):
    writer.writerow(listFinal[i])
outFile.close()
