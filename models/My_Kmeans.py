from matplotlib import pyplot
from numpy import unique, where
from sklearn import metrics
from sklearn.cluster import KMeans

import CONTROL
def my_kmeans(X=None,x_num=0,y_num=0):
    ways = "K-means"
    #    kmeans
    if CONTROL.Global.PROCESS_DETAIL:
        print("K-means begin")

    model = KMeans(n_clusters=CONTROL.Global.KMEANSCLUSTER)
    # 模型拟合
    model.fit(X)
    # 为每个示例分配一个集群
    yhat = model.predict(X)
    if CONTROL.Global.SCOREON:

        print(ways,metrics.calinski_harabasz_score(X, yhat))
    # 检索唯一群集
    clusters = unique(yhat)
    # 为每个群集的样本创建散点图
    for cluster in clusters:
        # 获取此群集的示例的行索引

        row_ix = where(yhat == cluster)
        # 创建这些样本的散布

        pyplot.scatter(X[row_ix, x_num], X[row_ix, y_num])

    # 绘制散点图
    pyplot.text(.99, .01, ('kmeans_score: %.2f' % metrics.calinski_harabasz_score(X, yhat)),
                transform=pyplot.gca().transAxes, size=10,
                horizontalalignment='right')
    name="N= " + (str)(CONTROL.Global.KMEANSCLUSTER) + " "+ CONTROL.Global.COLLIST[y_num + 5] + "-" +CONTROL.Global.COLLIST[x_num + 5]
    xname=CONTROL.Global.COLLIST[x_num + 5]
    yname=CONTROL.Global.COLLIST[y_num + 5]
    pyplot.title(name, fontproperties="STSong", fontsize=16)
    pyplot.xlabel(xname, fontproperties="STSong", fontsize=16)
    pyplot.ylabel(yname, fontproperties="STSong", fontsize=16)
    # my_x_ticks=np.arange(-2, 1, 0.1)
    # my_y_ticks=(0, 1, 0.01)
    # pyplot.xticks(my_x_ticks)
    # pyplot.yticks(my_y_ticks)

    print(CONTROL.Global.FIGSAVE_PATH+yname+"-"+xname+".png")
    pyplot.savefig(CONTROL.Global.FIGSAVE_PATH+yname+"-"+xname+".png")
    pyplot.show()