from sklearn.cluster import KMeans
from sklearn.externals import joblib
import pickle

file_path = r'C:\Users\lyzdsb\PycharmProjects\untitled3\data\raw_data_integrate' + r'\raw_data_para3.pkl'
mode_path = r'C:\Users\lyzdsb\PycharmProjects\untitled3\data\para3_data'
pkl_file = open(file_path, 'rb')
X = pickle.load(pkl_file)

# 训练模型并且保存
for i in range(10, 51, 2):
    clf = KMeans(n_clusters=i)
    s = clf.fit(X)
    # 需要设置参数 compress = 3， 否则保存的模型文件的同时会生成很多杂乱的文件
    joblib.dump(clf, mode_path + r'\mode_i_' + str(i) + '.pkl', compress=3)
    print(i, clf.inertia_)

# for i in range(20, 24):
#     clf = joblib.load('mode_i_' + str(i) + '.pkl')
#     print(clf.cluster_centers_)

# clf = joblib.load('mode_i_' + str(i) + '.pkl')

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
