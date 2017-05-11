# 导入需要的库
import tushare as ts
import matplotlib.pyplot as plt
import matplotlib.finance as mpf
from sklearn.cluster import KMeans
from sklearn.externals import joblib

clf = joblib.load('mode_i_60.pkl')
X = clf.cluster_centers_
# print(X[0][3]*10)
# 假设 前一日的收盘价和最低价都是10，也就是 close[i] = low[i] = 10

data_list = []

for i in range(len(X)):
    # 上涨
    if X[i][3] >= 0:
        close = X[i][3] * 10 + 10
        open = close - X[i][0] * 10
        high = X[i][1] * 10 + close
        low = open - X[i][2] * 10
        datas = (i * 2, open, high, low, close)
        data_list.append(datas)
    # 下跌
    else:
        close = X[i][3] * 10 + 10
        low = close - X[i][2] * 10
        open = X[i][0] * 10 + close
        high = X[i][1] * 10 + open
        datas = (i * 2, open, high, low, close)
        data_list.append(datas)
lista = range(0, len(data_list) * 2, 2)

# for i in range(len(data_list)):
#     data_list[i][0] = lista[i]

print(data_list)
#
# 创建一个子图
fig, ax = plt.subplots(facecolor=(0.5, 0.5, 0.5))
fig.subplots_adjust(bottom=0.2)
# 设置X轴刻度为日期时间
# ax.xaxis_date()
# X轴刻度文字倾斜45度
plt.xticks(rotation=45)
plt.title("股票代码：601558两年K线图")
plt.xlabel("时间")
plt.ylabel("股价（元）")
mpf.candlestick_ohlc(ax, data_list, width=1.5, colorup='r', colordown='green')
# plt.grid(True)
plt.show()
