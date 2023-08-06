import numpy as np
import csv
import CONTROL.Global
from dataprocess import processfunc
from dataprocess.processfunc import sub_time, averagetime, actimes, acrate, MinMaxScaler_Single, modifycol, \
    longtail_modify_log, longtail_log, MinMaxScaler_use, check_col, merge, maptolist, map_zero_check, cal_firstsubmit, \
    maptolist2
# filename="C:\\Users\\11858\\Desktop\\暑期\\data\\pure\\assigndata1518_2.csv"
import os

from models.My_Kmeans import my_kmeans

path = "C:\\Users\\11858\\Desktop\\暑期\\data\\pure"
dirs = os.listdir(path)

# 输出所有文件和文件夹
# for file in dirs:
#    print( file)
column=[]
filenamelist=[]
# for filename in filenamelist:
for file in dirs:
    with open(path+"\\"+file,encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        # column1=[row for row in reader if(row["题型"] == "编程题")]
        # print(len(column1))
        for col in reader:
            if col["题型"] == "编程题" \
                    and col["提交次数"] != "-1" \
                    and col["提交次数"] != "0" \
                    and col["难度"]!='0' \
                    and (float)(col["首次AC时间"])>=0\
                    and col["学号"][0]!="t" \
                    and col["学号"][0]!="y" \
                    and col["学号"][0]!= "s":\

                column.append(
                [col["学号"],#0
                col["题目ID"],#1
                 (int)(col["难度"]),#2
                col["首次提交时间"],#3
                col["最后提交时间"],#4
                sub_time(col["首次提交时间"],col["最后提交时间"]),  #提交时间差 5
                (int)(col["提交次数"]),  #提交次数6
                averagetime(sub_time(col["首次提交时间"], col["最后提交时间"]),col["提交次数"]),  #平均提交间隔7
                actimes(col["有效优化次数"], col["是否通过"]),  #通过次数8
                acrate(actimes(col["有效优化次数"], col["是否通过"]),submittimes=col["提交次数"]),#9
                 (float)(col["首次AC时间"])#10
                 #11首次提交与首次提交同学的时间差-->相对积极性
                ]
                )
    # column = [[col["学号"],
    #            col["题目ID"],
    #            col["难度"],
    #            col["首次提交时间"],
    #            col["最后提交时间"],
    #            sub_time(col["首次提交时间"],col["最后提交时间"]),  #提交时间差
    #            col["提交次数"],  #提交次数
    #            averagetime(sub_time(col["首次提交时间"], col["最后提交时间"]),col["提交次数"]),  #平均提交间隔
    #            actimes(col["有效优化次数"], col["是否通过"]),  #通过次数
    #            acrate(actimes(col["有效优化次数"], col["是否通过"]),submittimes=col["提交次数"])
    #            ]for col in reader if((col["题型"]=="编程题")&(col["提交次数"]!="-1"))]  #  同列的数据
    if(CONTROL.Global.FILEREAD_LINES):
        print("读入"+file+"后，当前总共的编程题提交记录数: ",len(column))


if CONTROL.Global.CHECKFORCOL:
    check_col(column)

firstsubmit=cal_firstsubmit(column)
#加入#11列
for i in column:
    i.append(sub_time(firstsubmit.get(i[1]),i[3]))
    #i[11]

if CONTROL.Global.PROCESS_DETAIL:
    print("cs数据读取完成，特征项构造完成")
    if CONTROL.Global.COLTYPE:
        for i in range(len(column[0])):
            print(i, CONTROL.Global.COLLIST[i], (type)(column[0][i]))
    print()
#引入sklkearn中的归一化模块
#归一化
#1）获取数据
Xmap=merge(column)
col=maptolist2(Xmap)

col=processfunc.process(col)

# column=processfunc.process(column)
#
# Xmap=merge(column)
final=col
if CONTROL.Global.MAPZEROSHOW:
    map_zero_check(Xmap)
if CONTROL.Global.FINAL_NUMS_OF_STD:
    print("总计有效人数:",len(final))

# X=np.asarray([tmp[5:] for tmp in column],'f')
#tmp[7]:std id
for i in final:
    try:
        i[7]=int(i[7])
    except ValueError:
        print(i[7])
X=np.asarray([tmp for tmp in final],'f')

my_kmeans(X)