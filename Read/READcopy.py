import csv

import numpy as np
from matplotlib import pyplot

from CONTROL.Global import  FILEREAD_LINES_TEST
from dataprocess.hash import HashMap

path = "C:\\Users\\11858\\Desktop\\暑期\\data\\查重"
file="作业7.csv"
namelist = []
idlist=[]
copytimes=HashMap()
def readcopy():
    with open(path + "\\" + file, encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile)
        # column1=[row for row in reader if(row["题型"] == "编程题")]
        # print(len(column1))
        for col in reader:
            # if col["学号/姓名"][0] != "t" \
            # and col["学号/姓名"][0] != "y" \
            # and col["学号/姓名"][0] != "s" \
            # and col["学号/姓名"][0] != "Z":


                tmp=list(col["学号/姓名"].split())
                if tmp!=[]:

                    for i in tmp:
                        tmp1=list(i.split('/'))

                        idlist.append(int(tmp1[1]))

    # if (FILEREAD_LINES_TEST):
    #     print("读入" + file + "后，当前总共的考试人数: ", len(test))

    if 0:
        nptest=np.asarray([[(int)(tmp[0]),tmp[2]]for tmp in test])
        pyplot.scatter(nptest[:,0],nptest[:,1])
        pyplot.show()
    print(idlist)

    for i in idlist:
        if copytimes.get(i)==None:
            copytimes.put(i,1)
        else:
            copytimes.put(i,copytimes.get(i)+1)

    return copytimes


