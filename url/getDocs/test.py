from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
import numpy as np

#%matplotlib inline
np.set_printoptions(precision=5, suppress=True)
# 生成两个集群: 集群 a 有100个数据点, 集群 b 有50个数据点:
np.random.seed(1029)
a = np.random.multivariate_normal([10, 0], [[3, 1], [1, 4]], size=[100,])
b = np.random.multivariate_normal([0, 20], [[3, 1], [1, 4]], size=[50,])
X = np.concatenate((a, b),)
plt.figure(figsize=(25, 10))
plt.scatter(X[:, 0], X[:, 1])
plt.show()