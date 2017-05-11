import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.externals import joblib
import numpy

X = []
Y = []
dataSet = []
for i in range(20,100):
    clf = joblib.load('mode_i_' + str(i) + '.pkl')
    centerCollection = clf.cluster_centers_
    within = clf.inertia_
    between = 0
    for j in range(len(centerCollection)):
        for k in range(j + 1, len(centerCollection)):
            dist = numpy.linalg.norm(centerCollection[j] - centerCollection[k]).item()
            between = dist + between

    ratio = between / (between + within)
    X.append(i)
    Y.append(ratio)
    dataSet.append((i, ratio))

plt.figure(figsize=(8,4)) #创建绘图对象
plt.plot(X,Y,"b--",linewidth=1)   #在当前绘图对象绘图（X轴，Y轴，蓝色虚线，线宽度）
plt.xlabel("K") #X轴标签
plt.ylabel("Sum of Squares for Error(ratio)")  #Y轴标签
plt.title("Sum of Squares for Error versus k(ratio)") #图标题
plt.grid(True)
plt.show()  #显示图
# print(X)
# print(Y)
# print(dataSet)