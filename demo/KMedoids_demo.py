from numpy import unique
from numpy import where
from sklearn import metrics
from sklearn.datasets import make_classification
from sklearn_extra.cluster import KMedoids
from matplotlib import pyplot

# 定义数据集
X, _ = \
    make_classification(n_samples=1000, n_features=2, n_informative=2, n_redundant=0, n_clusters_per_class=1, random_state=4)
# 定义模型，cluster是簇的含义，初始就需要定义
model = KMedoids(n_clusters=2)
#
# n_clustersint，可选，默认值：8
# 要形成的簇数以及要形成的中心点数 生成。
#
# 度量字符串，或可调用，可选，默认值：“欧几里得”
# 要使用的距离度量。参见 ：func：metrics.pairwise_distances 指标可以“预先计算”，然后用户必须输入 FIT 方法 使用预先计算的内核矩阵而不是设计矩阵 X。
#
# 方法{'alternate'， 'pam'}， default： 'alternate'
# 使用哪种算法。“替代”更快，而“PAM”更准确。
#
# init{'random'， 'heuristic'， 'k-medoids++'， 'build'}， 或类似数组的形状
# （n_clusters，n_features），可选，默认值：“启发式” 指定中心点初始化方法。“随机”选择n_clusters 元素。“启发式”选择n_clusters点 与其他点的总和距离最小。'k-中心点++' 遵循基于 k-means++_ 的方法，并且通常给出初始 中心点比其他方法生成的中心点更分离。 “build”是对原始PAM中使用的中心点的贪婪初始化 算法。通常“构建”效率更高，但比其他“构建”慢 在大数据集上进行初始化，它也非常不健壮， 如果数据集中存在异常值，请使用另一个初始化。 如果传递数组，它的形状应为 （n_clusters、n_features） 并给出初始中心。
#
# max_iterint，可选，默认值300
# 指定拟合时的最大迭代次数。它可以为零 在这种情况下，仅计算初始化，这可能适用于 初始化足够高效时的大型数据集 （即用于“构建”初始化）。
#
# random_stateint、随机状态实例或无，可选
# 指定随机数生成器的随机状态。习惯于 初始化中心点时初始化 init='random'。
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
pyplot.text(.99, .01, ('kmedioids_score: %.2f' % metrics.calinski_harabasz_score(X, yhat)),
            transform=pyplot.gca().transAxes, size=10,
            horizontalalignment='right')
pyplot.show()