import sklearn
print(sklearn.__version__)

# 综合分类数据集
from numpy import where
from sklearn.datasets import make_classification
from matplotlib import pyplot
# 定义数据集
X, y = make_classification(n_samples=1000, n_features=2, n_informative=2, n_redundant=0, n_clusters_per_class=1, random_state=4)
#可以看到在这里，               样本数量        总共的特征数量  信息特征数量        冗余特征数量      每个类的集群数目          复现的随机数，即随机数种子
#返回的X : ndarray(n_samples, n_features)生成的n+samples个样本
#返回的y : ndarray(n_samples)每个样本的类别成员的整数标签 shape_y=1000,1
#在这个样本中返回的是x，y值，如果要读取一个类别的话那么使用X[行索引，列索引（即信息特征x-->0,y-->1）]
# 为每个类的样本创建散点图
for class_value in range(2):
# 获取此类的示例的行索引,即如果y=class_value,那么输出对应的坐标，即index，保存在row_ix中,然后去X中索引，索引到 feature值
    row_ix = where(y == class_value)
# 创建这些样本的散布
    pyplot.scatter(X[row_ix, 0], X[row_ix, 1])
#忘了怎么画看这个https://www.runoob.com/matplotlib/matplotlib-scatter.html
# 绘制散点图
pyplot.show()