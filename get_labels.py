import pickle
import os
from sklearn.externals import joblib

mode_path = r'C:\Users\lyzdsb\PycharmProjects\finalProject\data\para3_data'
file_path = r'C:\Users\lyzdsb\PycharmProjects\finalProject\data\raw_data_integrate' + r'\raw_data_para3.pkl'
dirpath = r'C:\Users\lyzdsb\PycharmProjects\finalProject\data'

# load data
# pkl_files = open(file_path, 'rb')
# data_integrate = pickle.load(pkl_files)
# pkl_files.close()

# get the number of data of every stock
# code_list = os.listdir(dirpath + r'\raw_data')
# data_len = []
# counter = 0
# for code in code_list:
#     file_path = dirpath + r'\raw_data' + '\\' + code
#     pkl_file = open(file_path, 'rb')
#     data = pickle.load(pkl_file)
#     pkl_file.close()
#     counter = counter + len(data)
#     data_len.append(len(data))
# result = open(dirpath + r'\data_len.pkl', 'wb')
# pickle.dump(data_len, result, -1)
# result.close()


# load model
clf = joblib.load(mode_path + r'\mode_i_30.pkl')
X = clf.labels_

# load labels_
pkl_files = open(dirpath + '\data_len.pkl', 'rb')
data_len = pickle.load(pkl_files)
pkl_files.close()

# get the list of labels
count = 0
result = []
for len in data_len:
    result.append(X[count:count + len])
    count = count + len

# save labels
label_file = open(dirpath + r'\labels.pkl', 'wb')
pickle.dump(result, label_file, -1)
label_file.close()
