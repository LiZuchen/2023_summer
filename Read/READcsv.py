import numpy as np
import csv
import CONTROL.Global
from Read.READcopy import readcopy
from dataprocess import processfunc
from dataprocess.hash import HashMap
from dataprocess.processfunc import sub_time, averagetime, actimes, acrate, MinMaxScaler_Single, modifycol, \
    longtail_modify_log, longtail_log, MinMaxScaler_use, check_col, merge, maptolist, map_zero_check, cal_firstsubmit, \
    maptolist2, stdid_to_int
import os
from models.My_Kmeans import my_kmeans

path = "C:\\Users\\11858\\Desktop\\暑期\\data\\pure"
dirs = os.listdir(path)
column = []
filenamelist = []
# 输出所有文件和文件夹
if CONTROL.Global.FILEREAD_NAMES_SHOW:
    for file in dirs:
        print(file)

for file in dirs:
    with open(path + "\\" + file, encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for col in reader:
            if col["题型"] == "编程题" \
                    and col["提交次数"] != "-1" \
                    and col["提交次数"] != "0" \
                    and col["难度"] != '0' \
                    and (float)(col["首次AC时间"]) >= 0 \
                    and col["学号"][0] != "t" \
                    and col["学号"][0] != "y" \
                    and col["学号"][0] != "s": \
                    column.append(
                        [col["学号"],  # 0
                         col["题目ID"],  # 1
                         (int)(col["难度"]),  # 2
                         col["首次提交时间"],  # 3
                         col["最后提交时间"],  # 4
                         sub_time(col["首次提交时间"], col["最后提交时间"]),  # 提交时间差 5
                         (int)(col["提交次数"]),  # 提交次数6
                         averagetime(sub_time(col["首次提交时间"], col["最后提交时间"]), col["提交次数"]),  # 平均提交间隔7
                         actimes(col["有效优化次数"], col["是否通过"]),  # 通过次数8
                         acrate(actimes(col["有效优化次数"], col["是否通过"]), submittimes=col["提交次数"]),  # 9
                         (float)(col["首次AC时间"])  # 10
                         # 11首次提交与首次提交同学的时间差-->相对积极性
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
    if (CONTROL.Global.FILEREAD_LINES):
        print("读入" + file + "后，当前总共的编程题提交记录数: ", len(column))

if CONTROL.Global.CHECKFORCOL:
    check_col(column)

firstsubmit = cal_firstsubmit(column)
# 加入#11列
for i in column:
    i.append(sub_time(firstsubmit.get(i[1]), i[3]))
    # i[11]


if CONTROL.Global.PROCESS_DETAIL:
    print("csv数据读取完成，特征项构造完成")
    if CONTROL.Global.COLTYPE:
        for i in range(len(column[0])):
            print(i, CONTROL.Global.COLLIST[i], (type)(column[0][i]))
    print()

#MERGE TO X[7]
Xmap = merge(column)
col = maptolist2(Xmap)
#MERGE END

copy=readcopy()
for i in col:
    if copy.get(int(i[8])) == None:
        i[7]=0
    else:
        i[7]=copy.get(int(i[8]))
        if CONTROL.Global.COPYTIMESSHOW:
            print(i[8],i[7])
# Now i  in col is X

col = processfunc.process(col)

# check = HashMap()
# for i in col:
#     if check.get(i[7]) != None:
#         print("chongfu")
#     else:
#         check.put(i[7], i[:6])
# column=processfunc.process(column)
#
# Xmap=merge(column)
final = col

if CONTROL.Global.MAPZEROSHOW:
    map_zero_check(Xmap)
if CONTROL.Global.FINAL_NUMS_OF_STD:
    print("总计有效人数:", len(final))

# X=np.asarray([tmp[5:] for tmp in column],'f')
# 'f' can cause bug

stdid_to_int(final)
# ！！！！！

X = np.asarray([tmp for tmp in final])

my_kmeans(X,copy)

