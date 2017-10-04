from sklearn.cluster import KMeans
from sklearn.externals import joblib
import pickle

file_path = r'C:\Users\lyzdsb\PycharmProjects\finalProject\data\raw_data_integrate' + r'\raw_data_para3.pkl'
mode_path = r'C:\Users\lyzdsb\PycharmProjects\finalProject\data\para3_data'
pkl_file = open(file_path, 'rb')
X = pickle.load(pkl_file)

# train and save models with different number of clusters
for i in range(10, 51, 2):
    clf = KMeans(n_clusters=i)
    s = clf.fit(X)
    # compress = 3
    joblib.dump(clf, mode_path + r'\mode_i_' + str(i) + '.pkl', compress=3)
    print(i, clf.inertia_)

# overall_distance = inner_distance + inter_distance

# load models
joblib.dump(clf, 'mode_i_25.pkl')
clf = joblib.load('mode_i_25.pkl')
centerCollection = clf.cluster_centers_

global result
result = 0
for i in range(len(centerCollection)):
    for j in range(i + 1, len(centerCollection)):
        dist = numpy.linalg.norm(centerCollection[i] - centerCollection[j]).item()
        result = dist + result

