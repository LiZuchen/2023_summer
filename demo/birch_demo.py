from numpy import unique
from numpy import where
from sklearn.datasets import make_classification
from sklearn.cluster import Birch
from matplotlib import pyplot
# 定义数据集
X, _ = make_classification(n_samples=1000, n_features=2, n_informative=2, n_redundant=0, n_clusters_per_class=1, random_state=4)
# 定义模型
model = Birch(threshold=0.01, n_clusters=2)
#
#threshold float, default=0.5
#The radius of the subcluster obtained by merging a new sample and the closest subcluster should be lesser than the threshold.
# Otherwise a new subcluster is started. Setting this value to be very low promotes splitting and vice-versa.
#新样本与最近的子簇合并得到的子簇的半径应小于阈值。否则将启动一个新的子集群。将此值设置为非常低会促进拆分，反之亦然。
#branching_factor： int, default=50
#Maximum number of CF subclusters in each node.
# If a new samples enters such that the number of subclusters exceed the branching_factor then that node is split into two nodes with the subclusters redistributed in each. The parent subcluster of that node is removed and two new subclusters are added as parents of the 2 split nodes.
#每个节点中的最大 CF 子集群数。CF (聚类特征) 内部节点的最大CF数B
#n_clusters ：int, instance of sklearn.cluster model or None, default=3
#Number of clusters after the final clustering step, which treats the subclusters from the leaves as new samples.
#取值   None : the final clustering step is not performed and the subclusters are returned as they are.
#      sklearn.cluster Estimator : If a model is provided, the model is fit treating the subclusters as new samples and the initial data is mapped to the label of the closest subcluster.
#      int : the model fit is AgglomerativeClustering with n_clusters set to be equal to the int.
#即类别数K，在BIRCH算法是可选的，如果类别数非常多，我们也没有先验知识，则一般输入None，此时BIRCH算法第4阶段不会运行。但是如果我们有类别的先验知识，则推荐输入这个可选的类别值。默认是3，即最终聚为3类。
#compute_labelsbool, default=True
#Whether or not to compute labels for each fit.
#布尔值，表示是否标示类别输出，默认是True。一般使用默认值挺好，这样可以看到聚类效果。
#copybool, default=True
#Whether or not to make a copy of the given data. If set to False, the initial data will be overwritten.
# 适配模型
model.fit(X)
# 为每个示例分配一个集群
yhat = model.predict(X)
# 检索唯一群集
clusters = unique(yhat)
# 为每个群集的样本创建散点图
for cluster in clusters:
# 获取此群集的示例的行索引
    row_ix = where(yhat == cluster)
# 创建这些样本的散布
    pyplot.scatter(X[row_ix, 0], X[row_ix, 1])
# 绘制散点图
pyplot.show()