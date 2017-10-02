import csv
import numpy as np

print("hello world")
# 脚本预处理得到的常数
lgAST = 364718.8
lgFG = 625204.8
lgFT = 1378642.5
LgPTS = 9.599483741893954
lgFGA = 7.9257835855217715
lgORB = 1.0323144230326975
lgTO = 1.3148358092259547
lgFTA = 1.6748677735363129
LgTRB = 4.077040311824487
# DRBP = 3.0480217771236817
lgFT_fault = 1.6748677735363129
lgPF = 1.9255915697006025

# 计算过程中的常数
factor = (2 / 3) - (0.5 * (lgAST / lgFG)) / (2 * (lgFG / lgFT))
VOP = LgPTS / (lgFGA - lgORB + lgTO + 0.44 * lgFTA)
DRBP = (LgTRB - lgORB) / LgTRB

listFinal = []  # 用来保存输出的

with open('../../res/teamDataAdvanced.csv', 'r', encoding="utf-8") as csvFile:
    read = csv.reader(csvFile)
    isFirst = True
    tmAST = 0
    tmFG = 0
    for item in read:

        listRow = []  # 保存单行数据
        if isFirst:  # 去除第一行
            isFirst = False
            continue
        if int(item[1]) == 0:  # 把球队两数据预载入
            tmAST = float(item[23])
            tmFG = float(item[24])
        # PER计算式
        uPER = 0
        MP = float(item[4])
        P3 = float(item[10])
        AST = float(item[17])
        FG = float(item[6])
        FT = float(item[12])
        TO = float(item[20])
        FGA = float(item[7])
        # FG = float(item[6])
        FTA = float(item[13])
        # FT = float(item[12])
        TRB = float(item[14])
        ORB = float(item[15])
        STL = float(item[18])
        BLK = float(item[19])
        PF = float(item[21])

        try:
            uPER = (P3 + 2 / 3 * AST + (2 - factor * tmAST / tmFG) * FG + FT * 0.5 * (
                1 + (1 - tmAST / tmFG)) + 2 / 3 * tmAST / tmFG - VOP * TO - VOP * DRBP * (
                        FGA - FG) - VOP * 0.44 * (0.44 + (0.56 * DRBP)) * (
                        FTA - FT) + VOP * (1 - DRBP) * (
                        TRB - ORB) + VOP * DRBP * ORB + VOP * STL + VOP * DRBP * BLK -
                    PF * (lgFT / lgPF) -
                    0.44 * (lgFTA / lgPF) * VOP) / MP
        except:
            uPER = 0
        # 数据受限无法获得aPER和PER值，只能获得未修正的PER
        listFinal.append([uPER])

outFile = open('PerWithSequence.csv', 'w', newline='')  # 设置newline，否则两行之间会空一行
writer = csv.writer(outFile)
for i in range(len(listFinal)):
    writer.writerow(listFinal[i])
outFile.close()
