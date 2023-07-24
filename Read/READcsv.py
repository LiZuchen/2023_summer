import math
from datetime import datetime
import numpy as np
import csv
from numpy import unique
from numpy import where
from sklearn import metrics
from sklearn.datasets import make_classification
from sklearn.cluster import KMeans
from matplotlib import pyplot
from sklearn.preprocessing import MinMaxScaler
from sklearn_extra.cluster import KMedoids

import CONTROL.Global
from dataprocess.hash import HashMap
from dataprocess.processfunc import sub_time, averagetime, actimes, acrate, MinMaxScaler_Single, modifycol, \
    longtail_modify_log, longtail_log, MinMaxScaler_use, check_col, merge, maptolist, map_zero_check, cal_firstsubmit
# filename="C:\\Users\\11858\\Desktop\\暑期\\data\\pure\\assigndata1518_2.csv"
import os
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
                    and col["学号"][0]!="t" :\


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
for i in range(len(column[0])):
    if CONTROL.Global.COLTYPE:
        print(i,CONTROL.Global.COLLIST[i],(type)(column[0][i]))

if CONTROL.Global.CHECKFORCOL:
    check_col(column)

firstsubmit=cal_firstsubmit(column)
#加入#11列
for i in column:
    i.append(sub_time(firstsubmit.get(i[1]),i[3]))
    #i[11]


#引入sklkearn中的归一化模块
#归一化
#1）获取数据
if CONTROL.Global.PROCESS_DETAIL:
    print("开始预处理：长尾分布log:投入时间")
longtail_log(column,5)
if CONTROL.Global.PROCESS_DETAIL:
    print("开始预处理：标准化投入时间")
MinMaxScaler_use(column,5)

if CONTROL.Global.PROCESS_DETAIL:
    print("开始预处理：长尾分布log：提交次数")
longtail_log(column,6)
if CONTROL.Global.PROCESS_DETAIL:
    print("开始预处理：标准化提交次数")
MinMaxScaler_use(column,6)

if CONTROL.Global.PROCESS_DETAIL:
    print("开始预处理：标准化平均间隔时间")
MinMaxScaler_use(column,7)

if CONTROL.Global.PROCESS_DETAIL:
    print("开始预处理：长尾分布log：通过次数")
longtail_log(column,8)
if CONTROL.Global.PROCESS_DETAIL:
    print("开始预处理：标准化通过次数")
MinMaxScaler_use(column,8)

if CONTROL.Global.PROCESS_DETAIL:
    print("开始预处理：长尾分布log：首次AC时间")
longtail_log(column,10)
if CONTROL.Global.PROCESS_DETAIL:
    print("开始预处理：标准化首次AC时间")
MinMaxScaler_use(column,10)

if CONTROL.Global.PROCESS_DETAIL:
    print("开始预处理：标准化首次提交与最早差")
MinMaxScaler_use(column,11)

Xmap=merge(column)
final=maptolist(Xmap)
if CONTROL.Global.MAPZEROSHOW:
    map_zero_check(Xmap)
if CONTROL.Global.FINALNUMSOFSTD:
    print("总计有效人数:",len(final))

# X=np.asarray([tmp[5:] for tmp in column],'f')
X=np.asarray([tmp[:] for tmp in final],'f')

#    kmeans
if CONTROL.Global.PROCESS_DETAIL:
    print("K-means begin")
model = KMeans(n_clusters=CONTROL.Global.KMEANSCLUSTER)
# 模型拟合
model.fit(X)
# 为每个示例分配一个集群
yhat = model.predict(X)
if CONTROL.Global.SCOREON:
    print(metrics.calinski_harabasz_score(X, yhat))
# 检索唯一群集
clusters = unique(yhat)
# 为每个群集的样本创建散点图
for cluster in clusters:
# 获取此群集的示例的行索引
    row_ix = where(yhat == cluster)
# 创建这些样本的散布
    pyplot.scatter(X[row_ix, 1],X[row_ix, 4])
# 绘制散点图
pyplot.text(.99, .01, ('kmeans_score: %.2f' % metrics.calinski_harabasz_score(X, yhat)),
            transform=pyplot.gca().transAxes, size=10,
            horizontalalignment='right')


# my_x_ticks=np.arange(-2, 1, 0.1)
# my_y_ticks=(0, 1, 0.01)
# pyplot.xticks(my_x_ticks)
# pyplot.yticks(my_y_ticks)
pyplot.show()