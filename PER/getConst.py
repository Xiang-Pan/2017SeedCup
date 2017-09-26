import csv
import string

'''
常数提前输出 ：lgAST联盟助攻数 lgFG联盟命中数 lgFT联盟出手数。         LgPTS，联盟平均得分；lgFGA，联盟平均出手；lgORB，联盟平均前板；lgTO，联盟平均失误；lgFTA，联盟平均罚球数；
                             LgTRB，联盟平均总板；DRBP，联盟平均防守篮板；lgFT_fault/lgPF，联盟平均罚分/联盟平均犯规；lgFTA/lgPF，，联盟平均罚球数/联盟平均犯规；
                             
可以临时计算 ：/tmFG，球队助攻总数/球队命中总数 tmAST/tmFG，球队助攻数/球队命中数

'''

print("hello world")


try:
    f = open('../../res/test.csv', 'r')
except FileNotFoundError as e:
    print("failed")

with open('../res/teamData.csv', 'r', encoding="utf-8") as csvFile:
    read = csv.reader(csvFile)
    isFirst = True

    # 需要提前计算的常量如下
    lgAST = 0  # 联盟助攻数
    lgFG = 0  # 联盟命中数
    lgFT = 0  # 联盟出手数
    LgPTS = 0  # 联盟平均得分
    lgFGA = 0  # 联盟平均出手
    lgTO = 0  # 联盟平均失误
    lgFTA = 0  # 联盟平均罚球数 lgFT_fault = lgFTA
    lgORB = 0  # 联盟平均前板
    LgTRB = 0  # 联盟平均总板
    DRBP = 0  # 联盟平均防守篮板
    lgFT_fault = 0  # 联盟平均罚分
    lgPF = 0  # 联盟平均犯规
    BigTimes = 0  # 所有人出场次数（用来做分母）

    for i in read:

        if isFirst:  # jump out from the first one
            isFirst = False
            continue;

        times = int(i[2])
        # print(i)
        lgAST = lgAST + float(i[17]) * times
        lgFG = lgFG + float(i[6]) * times
        lgFT = lgFT + float(i[7]) * times
        LgPTS = LgPTS + float(i[22]) * times
        lgFGA = lgFGA + float(i[7]) * times
        lgTO = lgTO + float(i[20]) * times
        lgFTA = lgFTA + float(i[12]) * times
        lgORB = lgORB + float(i[15]) * times
        DRBP = DRBP + float(i[16]) * times
        lgPF = lgPF + float(i[21]) * times
        LgTRB = LgTRB + float(i[14]) * times
        BigTimes = BigTimes + times

    LgPTS = LgPTS / BigTimes
    lgFGA = lgFGA / BigTimes
    lgTO = lgTO / BigTimes
    lgFTA = lgFTA / BigTimes
    lgORB = lgORB / BigTimes
    LgTRB = LgTRB / BigTimes
    DRBP = DRBP / BigTimes
    lgPF = lgPF / BigTimes
    print(
        "lgAST联盟助攻数" + str(lgAST) + "\nlgFG联盟命中数" + str(lgFG) + "\nlgFT联盟出手数" + str(lgFT) + "\nLgPTS，联盟平均得分" + str(LgPTS) + "\nlgFGA，联盟平均出手" + str(lgFGA) + "\nlgORB，联盟平均前板" + str(lgORB) + "\nlgTO，联盟平均失误" + str(lgTO) + "\nlgFTA，联盟平均罚球数" + str(lgFTA) + "\nLgTRB，联盟平均总板" + str(LgTRB) + "\nDRBP，联盟平均防守篮板" + str(DRBP) + "\nlgFT_fault/lgFTA，联盟平均罚分（平均罚球数）" + str(lgFTA) + "\n联盟平均犯规" + str(lgPF))
