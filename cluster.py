from sklearn.cluster import KMeans
from sklearn.externals import joblib
import pickle
import numpy

file_path = 'C:/Users/lyzdsb/Desktop/' + 'finalProgrameraw_data_version2.pkl'
pkl_file = open(file_path, 'rb')
X = pickle.load(pkl_file)

# for i in range(5, 100, 1):
#     clf = KMeans(n_clusters=i)
#     s = clf.fit(X)
#     joblib.dump(clf, 'mode_i_'+str(i)+'.pkl')
#     print(i, clf.inertia_)

for i in range(20,24):
    clf = joblib.load('mode_i_' + str(i) + '.pkl')
    print(clf.cluster_centers_)



# 模型的保存和调用
# joblib.dump(clf, 'mode_i_25.pkl')
# clf = joblib.load('mode_i_35.pkl')
# centerCollection = clf.cluster_centers_
# print(clf.cluster_centers_)
# global result
# result = 0
# for i in range(len(centerCollection)):
#     for j in range(i + 1, len(centerCollection)):
#         dist = numpy.linalg.norm(centerCollection[i] - centerCollection[j]).item()
#         result = dist + result
# print(result)
# 簇内距离和
# print(clf.inertia_)



