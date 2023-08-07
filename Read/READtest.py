import csv

import numpy as np
from matplotlib import pyplot

from CONTROL.Global import  FILEREAD_LINES_TEST
path = "C:\\Users\\11858\\Desktop\\暑期\\data\\test"
file="examscore1691319996408.csv"
test = []
def readtest():
    with open(path + "\\" + file, encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile)
        # column1=[row for row in reader if(row["题型"] == "编程题")]
        # print(len(column1))
        for col in reader:
            if col["学号"][0] != "t" \
            and col["学号"][0] != "y" \
            and col["学号"][0] != "s" \
            and col["学号"][0] != "Z" \
            and (float)(col["总分"])>=0: \
                test.append(
                    [col["学号"],  # 0
                     col["姓名"],  # 1
                     (float)(col["编程题总分"]),  # 2
                     (float)(col["总分"]),  # 3
                    ]
                )

    if (FILEREAD_LINES_TEST):
        print("读入" + file + "后，当前总共的考试人数: ", len(test))

    if 0:
        nptest=np.asarray([[(int)(tmp[0]),tmp[2]]for tmp in test])
        pyplot.scatter(nptest[:,0],nptest[:,1])
        pyplot.show()
    return test

