import math
from datetime import datetime
import numpy as np
from sklearn.preprocessing import MinMaxScaler

#fafafa
def MinMaxScaler_Single(data):
    '''
    :param data: list[]
    :return: ndarray
    '''
    data=np.asarray(data)
    # #2)实例化一个转换器类
    transfer=MinMaxScaler(feature_range=(0,1))   #rang范围可改变
    # #3)调用transform转换
    data_new=transfer.fit_transform(data.reshape(-1,1))
    print(type(data_new) )
    return data_new
def sub_time2(date1,date2):
    date1 = datetime.strptime(date1, "%Y.%m.%d %H:%M:%S")
    date2 = datetime.strptime(date2, "%Y.%m.%d %H:%M:%S")
    print(" date1:", date1, "\n" ,"date2:", date2)
    print(" 2个日期的类型分别是:\n", type(date1), type(date2))
    print("时间差/s :",(date2-date1).total_seconds())
    return 0
def sub_time(date1,date2):
    # print("时间差/s :",(date2-date1).total_seconds())
    date1 = datetime.strptime(date1, "%Y-%m-%d %H:%M:%S")
    date2 = datetime.strptime(date2, "%Y-%m-%d %H:%M:%S")
    # print(" date1:", date1, "\n", "date2:", date2)
    # print("时间差/s :", (date2 - date1).total_seconds())
    return (date2-date1).total_seconds()
def averagetime(seconds,times):
    if times=="1" :
        return 0
    else:
        return seconds / ((int)(times) - 1)
def actimes(a, b):
    if(int(b)==1):
        return (int)(a)+(int)(b)
    else:
        return 0
def addcol(column,newcol):
    k = 0
    for lines in column:
        lines.append(newcol[k][0])
        k+=1
def modifycol(column,newcol,index):
    '''
    :param column: [[]]
    :param newcol: ndarray[[]]
    :param index: int
    :return:
    '''
    k = 0
    for lines in column:
        # print("change ",lines[index]," to ",newcol[k][0])
        lines[index]=newcol[k][0]
        k+=1

def acrate(actimes,submittimes):
    if (submittimes == "-1"):
        return 0
    else:
        return actimes/((int)(submittimes));

date1 = "2022.05.11 13:30:00"
date2 = "2022.05.10 12:00:00"
def longtail_modify(data):
    '''
       :param data: list
       :return: ndarray
    '''
    data = np.asarray(data)
    datanew=[]
    for datai in data:
        if datai<=0.02:
            datanew.append(0.2)
        elif datai<=0.05 and datai>0.02:
            datanew.append(0.4)
        elif datai <= 0.1 and datai > 0.05:
            datanew.append(0.6)
        elif datai > 0.1:
            datanew.append(0.8)
    return np.asarray(datanew,'f').reshape(-1,1)
def longtail_modify_log(data):
    '''
        :param data: list
        :return: ndarray
    '''
    data = np.asarray(data )
    datanew=[]
    for datai in data:
        if(datai==0):
            print("6zero",datai)
        datanew.append(math.log((float)(datai+0.1),2))
    return np.asarray(datanew,'f').reshape(-1,1)