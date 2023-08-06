import warnings

from matplotlib import pyplot
from numpy import unique, where
from sklearn import metrics
from sklearn.cluster import KMeans

import CONTROL



def draw(X,yhat,clusters, x_num, y_num,listnum):
    # 为每个群集的样本创建散点图
    rgb=CONTROL.Global.COLORLIST_RGB
    k=0
    for cluster in clusters:
        # 获取此群集的示例的行索引
        row_ix = where(yhat == cluster)
        # 创建这些样本的散布
        pyplot.scatter(X[row_ix, x_num], X[row_ix, y_num],c=rgb[listnum.index(row_ix[0].size)])

        k += 1


    # 绘制散点图
    pyplot.text(.99, .01, ('kmeans_score: %.2f' % metrics.calinski_harabasz_score(X[:,:7], yhat)),
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

    print(CONTROL.Global.FIGSAVE_PATH + yname + "-" + xname + ".png")
    pyplot.savefig(CONTROL.Global.FIGSAVE_PATH + yname + "-" + xname + ".png")
    pyplot.show()

def my_kmeans(X=None):
    ways = "K-means"
    #    kmeans
    if CONTROL.Global.PROCESS_DETAIL:
        print("K-means begin")



    with warnings.catch_warnings():
        warnings.filterwarnings("ignore",category=FutureWarning,module="sklearn",lineno=1412)
        model = KMeans(n_clusters=CONTROL.Global.KMEANSCLUSTER)
        model.fit(X[:, :7])
    # 模型拟合

    # 为每个示例分配一个集群
    yhat = model.predict(X[:,:7])
    if CONTROL.Global.SCOREON:
        print(ways,metrics.calinski_harabasz_score(X[:,:7], yhat))
    # 检索唯一群集
    clusters=unique(yhat)
    if CONTROL.Global.PROCESS_DETAIL:
        print("K-means end,draw begin")

    #calulate
    stdlist = []
    listnum=[]
    for cluster in clusters:
        # 获取此群集的示例的行索引
        row_ix = where(yhat == cluster)
        listnum.append(row_ix[0].size)
    listnum.sort()
    k = 0
    for cluster in clusters:
        # 获取此群集的示例的行索引
        row_ix = where(yhat == cluster)
        # 创建这些样本的散布
        stdlist.append(X[row_ix, 7])
        k += 1
    resultshow(stdlist,listnum)

    #draw
    for i in range(7):
        for j in range(i + 1, 7):
            draw(X,yhat,clusters,i,j,listnum)

def resultshow(stdlist,listnum):
        stdnum=0
        k=0
        for i in stdlist:
            if CONTROL.Global.STDID_SHOW:
                print("颜色为: ",CONTROL.Global.COLORLIST_NAME[listnum.index(i.size)]," 如下：")
                for j in i:
                    print(j)

            if CONTROL.Global.STDNUM_SHOW:
                print("颜色为: ", CONTROL.Global.COLORLIST_NAME[listnum.index(i.size)]," ",i.size,"人")
                stdnum+=i.size
            k += 1
        if CONTROL.Global.STDNUM_SHOW:
            print("总计 ",stdnum," 人")