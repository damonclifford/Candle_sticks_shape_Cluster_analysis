import tushare as ts
import matplotlib.pyplot as plt
import matplotlib.finance as mpf
from sklearn.externals import joblib

mode_path = r'C:\Users\lyzdsb\PycharmProjects\finalProject\data\para3_data'
clf = joblib.load(mode_path + r'\mode_i_30.pkl')
X = clf.cluster_centers_
print(X)

# default value of low euqals 10

data_list = []

for i in range(len(X)):
    low = 10
    # ups stick
    if X[i][0] >= 0:
        open = X[i][2] * 10 + 10
        close = X[i][0] * 10 + open
        high = X[i][1] * 10 + close
        datas = (i * 2, open, high, low, close)
        data_list.append(datas)
    # downs stick
    else:
        close = X[i][2] * 10 + 10
        open = close - X[i][0] * 10
        high = X[i][1] * 10 + open
        datas = (i * 2, open, high, low, close)
        data_list.append(datas)
lista = range(0, len(data_list) * 2, 2)

# for i in range(len(data_list)):
#     data_list[i][0] = lista[i]
#
# create a subplot
fig, ax = plt.subplots(facecolor=(0.5, 0.5, 0.5))
fig.subplots_adjust(bottom=0.2)
plt.xticks(rotation=45)
plt.title("Visualization of the best model")
# plt.xlabel()
# plt.ylabel()
mpf.candlestick_ohlc(ax, data_list, width=1.5, colorup='r', colordown='green')
# plt.grid(True)
plt.show()
