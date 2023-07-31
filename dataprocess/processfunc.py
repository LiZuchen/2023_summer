import copy
import math
from datetime import datetime
import numpy as np
from matplotlib import pyplot
from sklearn.preprocessing import MinMaxScaler

import CONTROL.Global
from dataprocess.hash import HashMap


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
    return data_new

def sub_time(date1,date2):
    '''
    :param date1: str
    :param date2: str
    :return: date2- date1 float
    '''
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
    '''
    :param a: str
    :param b: str
    :return: int
    '''
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

# date1 = "2022.05.11 13:30:00"
# date2 = "2022.05.10 12:00:00"
# def longtail_modify(data):
#     '''
#        :param data: list
#        :return: ndarray
#     '''
#     data = np.asarray(data)
#     datanew=[]
#     for datai in data:
#         if datai<=0.02:
#             datanew.append(0.2)
#         elif datai<=0.05 and datai>0.02:
#             datanew.append(0.4)
#         elif datai <= 0.1 and datai > 0.05:
#             datanew.append(0.6)
#         elif datai > 0.1:
#             datanew.append(0.8)
#     return np.asarray(datanew,'f').reshape(-1,1)
def longtail_modify_log(data):
    '''
        :param data: list
        :return: ndarray
    '''
    data = np.asarray(data )
    datanew=[]
    for datai in data:

        if (float)(datai)==-1:
            print("pass fail")
            datanew.append(math.log((float)(datai) +CONTROL.Global.LONGTAIL_INF_ALT, 2))
        else:
            try:
                datanew.append(math.log((float)(datai)+CONTROL.Global.LONGTAIL_ZERO_ADD,2))
            except (ValueError):
                print("data i error:",datai)
    return np.asarray(datanew,'f').reshape(-1,1)

def MinMaxScaler_use(column,number):
    data = [tmp[number] for tmp in column]
    timessubmit_std = MinMaxScaler_Single(data)
    modifycol(column, timessubmit_std, number)

def longtail_log(column,number):
    data = [tmp[number] for tmp in column]
    if CONTROL.Global.RAWFIGSHOW:
        i=range(len(data))
        pyplot.scatter(i,data)
        pyplot.title(CONTROL.Global.XLIST[number],fontproperties="STSong")
        pyplot.savefig(CONTROL.Global.RAW_FIGSAVE_PATH+CONTROL.Global.XLIST[number])
        pyplot.show()
    if CONTROL.Global.LONGTAILLOGDETAIL:
        print(len(data))
    timespass_std = longtail_modify_log(data)
    if CONTROL.Global.LONGTAILLOGDETAIL:
        print(len(column),len(timespass_std))
    modifycol(column, timespass_std, number)

def shorttail_modify_exp(data):
    '''
        :param data: list
        :return: ndarray
    '''
    data = np.asarray(data)
    datanew = []
    for datai in data:

        if (float)(datai) == -1:
            datanew.append(math.exp((float)(datai) / 10000000))
        else:
            try:
                datanew.append(math.exp((float)(datai)/10000000))
            except OverflowError:
                print("data i/10000000 error:", datai/10000000)

            # try:
            #     datanew.append(math.exp((float)(datai)))
            # except (ValueError):
            #     print("data i error:", datai)
    return np.asarray(datanew, 'f').reshape(-1, 1)
def shorttail_exp(column,number):
    data = [tmp[number] for tmp in column]
    if CONTROL.Global.RAWFIGSHOW:
        i=range(len(data))
        pyplot.scatter(i,data)
        pyplot.title(CONTROL.Global.XLIST[number],fontproperties="STSong")
        pyplot.savefig(CONTROL.Global.RAW_FIGSAVE_PATH+CONTROL.Global.XLIST[number])
        pyplot.show()
    if CONTROL.Global.LONGTAILLOGDETAIL:
        print(len(data))
    timespass_std = shorttail_modify_exp(data)
    if CONTROL.Global.SHORTTAILEXPDETAIL:
        print(len(column),len(timespass_std))
    modifycol(column, timespass_std, number)


def check_col(column):
    for i in column:
        if (i[5] == '0'):
            print("投入时间为0 ", i[0],"题目 ",i[1])
        if (i[6] == '0'):
            print("提交次数为0 ", i[0],"题目 ",i[1])
        if (i[7] == 0):
            print(i[0],"间隔为0 ","题目 ",i[1])
        if (i[8] == 0):
            print(i[0],"通过次数为0 ","题目 ",i[1],"提交次数为", i[6])
        if( i[9]== 0):
            print(i[0],"通过率为0","题目 ",i[1])
# def  col_FACtime(column):
#     for i in column:
#         if i[CONTROL.Global.COLLIST.index("首次AC时间")]<0:
#             i[CONTROL.Global.COLLIST.index("首次AC时间")]=CONTROL.Global.LONGTAIL_INF_ALT
#             print(i)
#     return column
def merge(column):
    #xnum
    if CONTROL.Global.PROCESS_DETAIL:
        print("学号+题目号码->学号 开始合并")
    adw=[3,4,5,6]
    anti_adw=[1,2]
    # column=col_FACtime(column)

    re=HashMap()
    #key:stdid;value:X
    numsofsubmit=HashMap()

    for i in column:
        if re.get(i[0])==None:
            re.put(i[0], [0, 0, 0, 0, 0, 0, 0])
            numsofsubmit.put(i[0],1)
        # print("before ",re.get(i[0]))
        times = numsofsubmit.get(i[0])
        for j in range(0,7):
            if j in adw:
                mergeadd_wei(re, i, j,times)
            elif j in anti_adw:
                mergeadd_anti_wei(re,i,j,times)
            else:
                mergeadd(re,i,j,times)
        numsofsubmit.put(i[0],times+1)
        # print("after ",re.get(i[0]))
    linked_list = numsofsubmit.headers

    for i in linked_list:
        for j in i.get_list():
            if j.get_val()<CONTROL.Global.LEASTSUBMIT:
                if CONTROL.Global.LESSTHANLEASTSUBMITSHOW:
                    print(j.get_key(), j.get_val())
                if CONTROL.Global.DELETELESSSUBMIT:
                    re.delete(j.get_key())

    if CONTROL.Global.PROCESS_DETAIL:
        print("学号+题目号码->学号 合并完成")
    return re
def mergeadd_wei(re,one,xnum,times):
    #one 为全部的信息
    colnum=xnum+5
    recordx=re.get(one[0])
    recordx[xnum]=(times)/(times+1)*recordx[xnum]+\
                  one[colnum]*one[2]/5/(times+1)

def mergeadd_anti_wei(re,one,xnum,times):
    colnum = xnum + 5
    recordx=re.get(one[0])
    recordx[xnum] = (times) / (times + 1) * recordx[xnum] + \
                    one[colnum] * (6-one[2])/5 / (times + 1)

def mergeadd(re,one,xnum,times):
    colnum = xnum + 5
    recordx=re.get(one[0])
    recordx[xnum] = (times) / (times + 1) * recordx[xnum] + \
                    one[colnum] / (times + 1)

def map_zero_check(MAP):
    linked_list = MAP.headers
    for i in linked_list:
        for j in i.get_list():
            # print(j.get_key(),j.get_val())
            for xi in j.get_val():
                if xi == 0:
                    print(j.get_key(), j.get_val())
                    break

def maptolist2(MAP):
    list=[]
    linked_list = MAP.headers
    for i in linked_list:
        for j in i.get_list():
            # print(type(j.get_key()),type(j.get_val()))
            std_std=copy.deepcopy(j.get_val())
            std_std.append(j.get_key())
            list.append(std_std)
    return list

def maptolist(MAP):
    list=[]
    linked_list = MAP.headers
    for i in linked_list:
        for j in i.get_list():
            # print(type(j.get_key()),type(j.get_val()))
            list.append(j.get_val())
    return list

def cal_firstsubmit(column):
    firstsubmit = HashMap()
    for i in column:
        if firstsubmit.get(i[1]) != None:
            if sub_time(i[3], firstsubmit.get(i[1])) > 0:
                if CONTROL.Global.FIRSTSUBMIT_DETAIL:
                    print("fi_sub change at ", i[1], " from ", firstsubmit.get(i[1]), " to ", i[3])
                firstsubmit.put(i[1], i[3])
        else:
            firstsubmit.put(i[1], i[3])
    return firstsubmit

def process(column):
    # LIST=CONTROL.Global.COLLIST
    LIST=CONTROL.Global.XLIST
    if CONTROL.Global.PROCESS_DETAIL and CONTROL.Global.hashlog.get("投入时间") == 1:
        print("开始预处理：长尾分布log:投入时间")
        longtail_log(column, LIST.index("投入时间"))
    if CONTROL.Global.PROCESS_DETAIL:
        print("开始预处理：标准化投入时间")
    MinMaxScaler_use(column, LIST.index("投入时间"))

    if CONTROL.Global.PROCESS_DETAIL and CONTROL.Global.hashlog.get("提交次数") == 1:
        print("开始预处理：长尾分布log：提交次数")
        longtail_log(column,LIST.index("提交次数"))
    if CONTROL.Global.PROCESS_DETAIL:
        print("开始预处理：标准化提交次数")
    MinMaxScaler_use(column, LIST.index("提交次数"))

    if CONTROL.Global.PROCESS_DETAIL and CONTROL.Global.hashlog.get("平均提交间隔") == 1:
        print("开始预处理：长尾分布log：平均提交间隔")
        longtail_log(column,LIST.index("平均提交间隔"))
    if CONTROL.Global.PROCESS_DETAIL:
        print("开始预处理：标准化平均提交间隔")
    MinMaxScaler_use(column,LIST.index("平均提交间隔"))

    if CONTROL.Global.PROCESS_DETAIL and CONTROL.Global.hashlog.get("通过次数") == 1:
        print("开始预处理：长尾分布log：通过次数")
        longtail_log(column,LIST.index("通过次数"))

    if CONTROL.Global.PROCESS_DETAIL:
        print("开始预处理：标准化通过次数")
    MinMaxScaler_use(column,LIST.index("通过次数"))

    if CONTROL.Global.PROCESS_DETAIL:
        print("开始预处理：标准化通过率")
    MinMaxScaler_use(column,LIST.index("通过率"))

    if CONTROL.Global.PROCESS_DETAIL and CONTROL.Global.hashlog.get("首次AC时间") == 1:
        print("开始预处理：长尾分布log：首次AC时间")
        longtail_log(column,LIST.index("首次AC时间"))

    if CONTROL.Global.PROCESS_DETAIL:
        print("开始预处理：标准化首次AC时间")
    MinMaxScaler_use(column,LIST.index("首次AC时间"))

    if CONTROL.Global.PROCESS_DETAIL and CONTROL.Global.hashlog.get("首次提交时间和最早提交者的时间差") == 1:
        print("开始预处理：长尾分布log：首次提交时间和最早提交者的时间差")
        longtail_log(column, LIST.index("首次提交时间和最早提交者的时间差"))

    if CONTROL.Global.PROCESS_DETAIL and CONTROL.Global.hashexp.get("首次提交时间和最早提交者的时间差") == 1:
        print("开始预处理：厚尾分布exp：首次提交时间和最早提交者的时间差")
        shorttail_exp(column, LIST.index("首次提交时间和最早提交者的时间差"))

    if CONTROL.Global.PROCESS_DETAIL:
        print("开始预处理：标准化首次提交时间和最早提交者的时间差")
    MinMaxScaler_use(column,LIST.index("首次提交时间和最早提交者的时间差"))

    return column