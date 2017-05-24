# 导入需要的库
import tushare as ts
import matplotlib.pyplot as plt
import matplotlib.finance as mpf
from sklearn.externals import joblib

mode_path = r'C:\Users\lyzdsb\PycharmProjects\untitled3\data\para3_data'
clf = joblib.load(mode_path + r'\mode_i_30.pkl')
X = clf.cluster_centers_
print(X)
# print(X[0][3]*10)
# 3个para, 默认low[i] = 10

data_list = []

for i in range(len(X)):
    low = 10
    # 阳线
    if X[i][0] >= 0:
        open = X[i][2] * 10 + 10
        close = X[i][0] * 10 + open
        high = X[i][1] * 10 + close
        datas = (i * 2, open, high, low, close)
        data_list.append(datas)
    # 阴线
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
# 创建一个子图
fig, ax = plt.subplots(facecolor=(0.5, 0.5, 0.5))
fig.subplots_adjust(bottom=0.2)
# 设置X轴刻度为日期时间
# ax.xaxis_date()
# X轴刻度文字倾斜45度
plt.xticks(rotation=45)
plt.title("对经过训练后的K-means模型结果进行可视化")
# plt.xlabel()
# plt.ylabel()
mpf.candlestick_ohlc(ax, data_list, width=1.5, colorup='r', colordown='green')
# plt.grid(True)
plt.show()
