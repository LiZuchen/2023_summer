import csv
import os

import numpy as np
from matplotlib import pyplot

import CONTROL.Global
from CONTROL.Global import FILEREAD_LINES_TEST
from dataprocess.hash import HashMap

path = "C:\\Users\\11858\\Desktop\\暑期\\data\\查重"
file = "作业7.csv"
dirs = os.listdir(path)
if CONTROL.Global.FILEREAD_NAMES_SHOW:
    for i in dirs:
        print(i)
namelist = []
idlist = []
copytimes = HashMap()


def readcopy():
    for file in dirs:
        with open(path + "\\" + file, encoding='utf-8-sig') as csvfile:
            reader = csv.DictReader(csvfile)
            for col in reader:
                # if col["学号/姓名"][0] != "t" \
                # and col["学号/姓名"][0] != "y" \
                # and col["学号/姓名"][0] != "s" \
                # and col["学号/姓名"][0] != "Z":
                tmp = list(col["学号/姓名"].split())
                if tmp != []:
                    for i in tmp:
                        tmp1 = list(i.split('/'))
                        if tmp1[1][0] != 't' and tmp1[1][0] != 's':
                            idlist.append(int(tmp1[1]))

        # if 0:
        #     nptest=np.asarray([[(int)(tmp[0]),tmp[2]]for tmp in test])
        #     pyplot.scatter(nptest[:,0],nptest[:,1])
        #     pyplot.show()
    print(idlist)
    for i in idlist:
        if copytimes.get(i) == None:
            copytimes.put(i, 1)
        else:
            copytimes.put(i, copytimes.get(i) + 1)

    return copytimes
