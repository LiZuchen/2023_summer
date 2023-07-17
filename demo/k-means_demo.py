from numpy import unique
from numpy import where
from sklearn import metrics
from sklearn.datasets import make_classification
from sklearn.cluster import KMeans
from matplotlib import pyplot
# 定义数据集
X, _ = \
    make_classification(n_samples=1000, n_features=2, n_informative=2, n_redundant=0, n_clusters_per_class=1, random_state=4)
# 定义模型，cluster是簇的含义，初始就需要定义
model = KMeans(n_clusters=2,verbose=1)
# n_clusters：聚类的数量，默认为8。
# init：初始化聚类中心的方法，默认为"k-means++"，即使用k-means++算法。（初始化质心）
# n_init：初始化聚类中心的次数，默认为10。
# max_iter：最大迭代次数，默认为300。
# tol：收敛阈值，默认为1e-4。
# precompute_distances：是否预先计算距离矩阵，默认为"auto"，即自动选择。
# verbose：是否输出详细信息，默认为，不输出。
# random_state：随机数种子，默认为None。
# copy_x：是否复制数据，默认为True。
# algorithm：聚类算法，默认为"auto"，即自动选择。可选值为"k-means"、"elkan"。
# n_jobs：并行计算的数量，默认为None，即使用单线程计算。可选值为正整数。
# distance_metric：距离度量，默认为"euclidean"，即欧几里得距离。可选值为"cityblock"、"cosine"、"l1"、"l2"、"manhattan"、"precomputed"。
# metric_params：距离度量的参数，默认为None。
# init_size：初始样本集的大小，默认为None，即使用全部样本。
# batch_size：每次迭代使用的样本数量，默认为None，即使用全部样本。
# verbose_interval：输出详细信息的间隔，默认为10。
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
    pyplot.scatter(X[row_ix, 0], X[row_ix, 1])
# 绘制散点图
pyplot.text(.99, .01, ('kmeans_score: %.2f' % metrics.calinski_harabasz_score(X, yhat)),
            transform=pyplot.gca().transAxes, size=10,
            horizontalalignment='right')
pyplot.show()