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

from dataprocess.processfunc import sub_time, averagetime, actimes, acrate, MinMaxScaler_Single, modifycol, \
    longtail_modify_log, longtail_modify

filename="C:\\Users\\11858\\Desktop\\暑期\\data\\assigndata1582_1.csv"
with open(filename,encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    # column1=[row for row in reader if(row["题型"] == "编程题")]
    # print(len(column1))
    column = [[col["学号"],
               col["题目ID"],
               col["难度"],
               col["首次提交时间"],
               col["最后提交时间"],
               sub_time(col["首次提交时间"],col["最后提交时间"]),  #提交时间差
               col["提交次数"],  #提交次数
               averagetime(sub_time(col["首次提交时间"], col["最后提交时间"]),col["提交次数"]),  #平均提交间隔
               actimes(col["有效优化次数"], col["是否通过"]),  #通过次数
               acrate(actimes(col["有效优化次数"], col["是否通过"]),submittimes=col["提交次数"])
               ]for col in reader if((col["题型"]=="编程题")&(col["提交次数"]!="-1"))]  #  同列的数据
print("len提交的编程题: ",len(column))
for tmp in column:
    if(tmp[6]=='0'):
        print(tmp[0],tmp[1],"zero times submit")
# print(column)
#引入sklkearn中的归一化模块
#归一化
#1）获取数据
data=[tmp[5] for tmp in column]
timespend_std=MinMaxScaler_Single(data)
modifycol(column,timespend_std,5)


data=[tmp[6] for tmp in column]
timessubmit_std=MinMaxScaler_Single(data)
modifycol(column,timessubmit_std,6)

data=[tmp[6] for tmp in column]
timespass_std=longtail_modify_log(data)
modifycol(column,timespass_std,6)

data=[tmp[8] for tmp in column]
timespass_std=MinMaxScaler_Single(data)
modifycol(column,timespass_std,8)

#调整分布：
data=[tmp[8] for tmp in column]
timespass_std=longtail_modify(data)
modifycol(column,timespass_std,8)


X=np.asarray([tmp[5:] for tmp in column],'f')

i=0
for x in X:
    print("通过rate: ",x[4])
    if x[4]==0:
        i+=1
print(i)
model = KMeans(n_clusters=3)
# 模型拟合
model.fit(X)
# 为每个示例分配一个集群
yhat = model.predict(X)
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