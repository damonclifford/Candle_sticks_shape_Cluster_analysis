import matplotlib.pyplot as plt
from sklearn import metrics
from sklearn.cluster import KMeans
from sklearn.externals import joblib
from sklearn.preprocessing import scale
import numpy as np
import pickle

modePath = r'C:\Users\lyzdsb\PycharmProjects\untitled3\data\para3_data'
dataPath = r'C:\Users\lyzdsb\PycharmProjects\untitled3\data\raw_data_integrate'
# 第一种评价方法
X = []
Y = []
dataSet = []
for i in range(10, 40):
    clf = joblib.load(modePath + r'\mode_i_' + str(i) + '.pkl')
    centerCollection = clf.cluster_centers_
    between = 0
    within = clf.inertia_
    for j in range(len(centerCollection)):
        for k in range(j+1, len(centerCollection)):
            dist = np.linalg.norm(centerCollection[j] - centerCollection[k])
            between = dist + between*1.01

    ratio = between / (between + within)
    X.append(i)
    Y.append(ratio)
    dataSet.append((i, ratio))
# 第二种评价方法
# for i in range(10, 40):
#     clf = joblib.load(modePath + r'\mode_i_' + str(i) + '.pkl')
#     pkl_file = open(dataPath+r'\raw_data_para3.pkl', 'rb')
#     data = scale(pickle.load(pkl_file))
#     X =np.asarray(data)
#     pkl_file.close()
# print(metrics.homogeneity_score(X, clf.labels_))
# sample_size = len(X)
# print(clf.labels_)
# metrics.silhouette_score(X, clf.labels_,
#                                       metric='euclidean',
#                                       sample_size=sample_size)
plt.figure(figsize=(8, 4))  # 创建绘图对象
plt.plot(X, Y, "b--", linewidth=1)  # 在当前绘图对象绘图（X轴，Y轴，蓝色虚线，线宽度）
plt.xlabel("K")  # X轴标签
plt.ylabel("Sum of Squares for Error(ratio)")  # Y轴标签
plt.title("Sum of Squares for Error versus k(ratio)")  # 图标题
plt.grid(True)
plt.show()  # 显示图

