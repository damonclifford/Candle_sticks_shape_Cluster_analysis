import matplotlib.pyplot as plt
from sklearn.externals import joblib
import numpy as np

modePath = r'C:\Users\lyzdsb\PycharmProjects\finalProject\data\para3_data'
dataPath = r'C:\Users\lyzdsb\PycharmProjects\finalProject\data\raw_data_integrate'
# calculate the metric 
# the formula of metric: ratio = inner_distance / (inner_distance + inter_distance)
# range[0,1], greater ratio means better performance
X = []
Y = []
dataSet = []
for i in range(10, 51, 2):
    clf = joblib.load(modePath + r'\mode_i_' + str(i) + '.pkl')
    centerCollection = clf.cluster_centers_
    inner_distance = 0
    inter_distance = clf.inertia_
    for j in range(len(centerCollection)):
        for k in range(j + 1, len(centerCollection)):
            dist = np.linalg.norm(centerCollection[j] - centerCollection[k])
            inter_distance = inter_distance + inner_distance*1.018
# para = 1.018
    ratio = inner_distance / (inner_distance + inter_distance)
    X.append(i)
    Y.append(ratio)
    dataSet.append((i, ratio))

# plot the metric of different metrics
plt.figure(figsize=(8, 4)) 
plt.plot(X, Y, "b--", linewidth=1)  
plt.xlabel("K") 
plt.ylabel("Sum of Squares for Error(ratio)") 
plt.title("Sum of Squares for Error versus k(ratio)")  
plt.grid(True)
plt.show() 
