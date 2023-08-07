import warnings

import numpy as np
from matplotlib import pyplot
from numpy import unique, where
from sklearn import metrics
from sklearn.cluster import KMeans

import CONTROL
from CONTROL.Global import FIGTITLESHOW
from Read.READtest import readtest
from dataprocess.hash import HashMap


def draw(X, yhat, clusters, x_num, y_num, listnum):
    # 为每个群集的样本创建散点图
    rgb = CONTROL.Global.COLORLIST_RGB
    #rgb 为 蓝 红 橙 绿
    k = 0
    for cluster in clusters:
        # 获取此群集的示例的行索引
        row_ix = where(yhat == cluster)
        # 创建这些样本的散布
        pyplot.scatter(X[row_ix, x_num], X[row_ix, y_num], c=rgb[listnum.index(row_ix[0].size)])

        k += 1

    # 绘制散点图
    pyplot.text(.99, .01, ('kmeans_score: %.2f' % metrics.calinski_harabasz_score(X[:, :7], yhat)),
                transform=pyplot.gca().transAxes, size=10,
                horizontalalignment='right')
    name = "N= " + (str)(CONTROL.Global.KMEANSCLUSTER) + " " + CONTROL.Global.COLLIST[y_num + 5] + "-" + \
           CONTROL.Global.COLLIST[x_num + 5]
    xname = CONTROL.Global.COLLIST[x_num + 5]
    yname = CONTROL.Global.COLLIST[y_num + 5]
    pyplot.title(name, fontproperties="STSong", fontsize=16)
    pyplot.xlabel(xname, fontproperties="STSong", fontsize=16)
    pyplot.ylabel(yname, fontproperties="STSong", fontsize=16)
    # my_x_ticks=np.arange(-2, 1, 0.1)
    # my_y_ticks=(0, 1, 0.01)
    # pyplot.xticks(my_x_ticks)
    # pyplot.yticks(my_y_ticks)

    if FIGTITLESHOW:
        print(CONTROL.Global.FIGSAVE_PATH + yname + "-" + xname + ".png")
    pyplot.savefig(CONTROL.Global.FIGSAVE_PATH + yname + "-" + xname + ".png")
    pyplot.show()


def my_kmeans(X=None):
    ways = "K-means"
    hashcolors = HashMap()
    #    kmeans
    if CONTROL.Global.PROCESS_DETAIL:
        print("K-means begin")

    with warnings.catch_warnings():
        warnings.filterwarnings("ignore", category=FutureWarning, module="sklearn", lineno=1412)
        model = KMeans(n_clusters=CONTROL.Global.KMEANSCLUSTER)
        model.fit(X[:, :8])
    # 模型拟合

    # 为每个示例分配一个集群
    yhat = model.predict(X[:, :8])
    if CONTROL.Global.SCOREON:
        print(ways, metrics.calinski_harabasz_score(X[:, :7], yhat))
    # 检索唯一群集
    clusters = unique(yhat)
    if CONTROL.Global.PROCESS_DETAIL:
        print("K-means end,draw begin")

    # calulate
    stdlist = []
    listnum = []
    for cluster in clusters:
        # 获取此群集的示例的行索引
        row_ix = where(yhat == cluster)
        listnum.append(row_ix[0].size)
    listnum.sort()
    print("首次排序后的大小",listnum)
    #颜色应为 蓝 红 橙 绿
    print("颜色应为   蓝 红 橙 绿")
    k = 0

    for cluster in clusters:
        # 获取此群集的示例的行索引
        row_ix = where(yhat == cluster)
        # 创建这些样本的散布


        for j in row_ix[0]:
            if hashcolors.get(X[j, 7])!=None:
                print("重复在",j,X[j, 7],"之前在",hashcolors.get(X[j, 7]))
            else:
                hashcolors.put(X[j, 7],j)
                # print("放入",j,X[j, 7])

        ele = X[row_ix, 7].tolist()[0]

        stdlist.append(ele)
        k += 1
    #stdlist按乱序装入各个学生
    #listnum 指定各人数对应的颜色
    resultshow(stdlist, listnum)

    #draw
    for i in range(7):
        for j in range(i + 1, 7):
            draw(X, yhat, clusters, i, j, listnum)


def resultshow(stdlist, listnum):
    stdnum = 0
    k = 0
    hashcolor = HashMap()
    # hashcolor.put('red',[])
    # hashcolor.put('blue', [])
    # hashcolor.put('green', [])
    # hashcolor.put('orange', [])
    t = 0
    for i in stdlist:
        if CONTROL.Global.STDID_SHOW:
            print("颜色为: ", CONTROL.Global.COLORLIST_NAME[listnum.index(len(i))], " 如下：")
        for j in i:
            # (hashcolor.get(CONTROL.Global.COLORLIST_NAME[listnum.index(i.size)])).append(j)

            k = j
            key = (int)(k)
            key = (str)(key)
            hashcolor.put(key, CONTROL.Global.COLORLIST_NAME[listnum.index(len(i))])
            # print('add', key, CONTROL.Global.COLORLIST_NAME[listnum.index(len(i))], t)
            t += 1
            if CONTROL.Global.STDID_SHOW:
                print(k)

        if CONTROL.Global.STDNUM_SHOW:
            print("颜色为: ", CONTROL.Global.COLORLIST_NAME[listnum.index(len(i))], " ", len(i), "人")
            stdnum += len(i)
        k += 1
    if CONTROL.Global.STDNUM_SHOW:
        print("总计 ", stdnum, " 人")

    if CONTROL.Global.COMPARE_ON:
        c = 0
        test = readtest()
        for i in test:
            if hashcolor.get(i[0]) == None:
                c+=1
                print(i)
                i.append(None)
            else:
                i.append(hashcolor.get(i[0]))
        print("未找到人数",c)


    if 1:
        for tmp in test:
            if tmp[4]!=None:
                tmp[4]=CONTROL.Global.COLORLIST_NAME.index(tmp[4])
            else:
                tmp[4]=-1
            if((int)(tmp[0])>70000000):
                tmp[0]=(int)(tmp[0])-50000000
        nptest=np.asarray([[(int)(tmp[0]),tmp[2],tmp[4]]for tmp in test])

        row_ixs=[]
        for i in range(4):
            row_ix=where(nptest[:,2]==i)
            row_ixs.append(row_ix[0].size)
            pyplot.scatter(nptest[row_ix,1],nptest[row_ix,0],c=CONTROL.Global.COLORLIST_RGB[i])
        pyplot.show()
        ri=[]
        rinum=[0,0,0,0,0]
        for i in nptest[:,1]:
            ri.append(int(i//10))
            rinum[int(i//10)]=rinum[int(i//10)]+1
        # pyplot.bar(ri,nptest[:,1], alpha=1, width=1, color='r', edgecolor='r')
        pyplot.bar(range(0,5), rinum, alpha=1, width=1, color='r')
        pyplot.show()

        qj=5
        #blue
        first = [0,0,0,0]
        #red
        second = [0,0,0,0]
        #orange
        third = [0,0,0,0]
        #green
        fourth =[0,0,0,0]
        all=[first ,second ,third ,fourth]
        labels = {0, 1, 2, 3}

        for i in range(4):
            row_ix=where(nptest[:,2]==i)
            for j in nptest[row_ix, 1][0]:
                try:
                    all[listnum.index(len(row_ix[0]))][(int(j // 10))]+=1
                except IndexError:
                    print(i)
                    print(j)
        rgb=CONTROL.Global.COLORLIST_RGB

        #first 为蓝色各分段人数
        first_num=row_ixs[0]
        second_num=row_ixs[1]
        third_num=row_ixs[2]
        fourth_num=row_ixs[3]
        labels={0,1,2,3}

        x = np.arange(len(labels))  # x轴刻度标签位置
        width = 0.2  # 柱子的宽度
        # 计算每个柱子在x轴上的位置，保证x轴刻度标签居中
        pyplot.bar(x - 1.5 * width, first , width, label='1',color=rgb[0])
        pyplot.bar(x - 0.5 * width, second, width, label='2',color=rgb[1])
        pyplot.bar(x + 0.5 * width, third, width, label='3',color=rgb[2])
        pyplot.bar(x + 1.5 * width, fourth, width, label='4',color=rgb[3])
        pyplot.ylabel('人数',fontproperties="STSong", fontsize=16)
        pyplot.title('人数-成绩表',fontproperties="STSong", fontsize=16)
        pyplot.xticks(x, labels=labels)
        pyplot.legend()

        pyplot.show()
        print(first_num)
        print(first)
        print(second_num)
        print(second)
        print(third_num)
        print(third)
        print(fourth_num)
        print(fourth)
        cal(first,second,third,fourth)
def cal(a,b,c,d,e=None):
    word0 = []
    word1 = []
    word2 = []
    word3 = []
    word4=[]
    word0.append("抄袭作业型，低投入,低提交，低间隔，低通过次数，较高通过率，短首次AC时间，较高和最早间隔，低提交间隔")
    word1.append("投入忘我型，高投入,高提交，较高间隔，高通过次数，高通过率，高首次AC时间，低和最早间隔，高提交间隔")
    word2.append("学习困难型,高投入,较高提交，高间隔，中通过次数，低通过率，高首次AC时间，中和最早间隔，高提交间隔")
    word3.append("游刃有余型，中投入,中提交，中间隔，中通过次数，高通过率，中首次AC时间，中和最早间隔，中提交间隔")
    word=[word0,word1 ,word2, word3,word4]
    st=[a,b,c,d,e]
    stcol=['蓝','红','橙','绿',"黄"]
    print("各颜色各分段占自身百分比")
    for i in range(4):
        #i为颜色
        print(word[i])
        for j in range(4):
            #j为分段
            print(stcol[i],j,"比例",st[i][j]/sum(st[i]))
        print()

    print("各颜色占各分段百分比")
    for i in range(4):
        # i为颜色
        print(word[i])
        for j in range(4):
            # j为分段
            print(stcol[i], "占",j,"比例", st[i][j] / (st[0][j]+st[1][j]+st[2][j]+st[3][j]))
        print()


