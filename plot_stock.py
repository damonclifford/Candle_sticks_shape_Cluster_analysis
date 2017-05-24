from sklearn.externals import joblib
import pickle
import matplotlib.pyplot as plt
import matplotlib.finance as mpf
from matplotlib.pylab import date2num
import datetime

labels_path = r'C:\Users\lyzdsb\PycharmProjects\untitled3\data\labels.pkl'
mode_path = r'C:\Users\lyzdsb\PycharmProjects\untitled3\data\para3_data'
rawData_path = r'C:\Users\lyzdsb\PycharmProjects\untitled3\data\raw_data'


# 读取文件，获得label_list
labels_pkl = open(labels_path, 'rb')
labels_list = pickle.load(labels_pkl)
labels = labels_list[0]

# 读取model ，得到centers的数据
clf = joblib.load(mode_path + r'\mode_i_30.pkl')
centers = clf.cluster_centers_

# 读取000001.pkl
stock_pkl = open(rawData_path + r'\000001.pkl', 'rb')
stock_data = pickle.load(stock_pkl)
# print(stock_data)

# 把raw_data 替换成 center_data
data_processed = []
for label in labels:
    data_processed.append(centers[label])

data_list_center = []

for i in range(len(stock_data)):
    low = stock_data['low'][i]
    #     # 将时间转换为数字
    dates = str(stock_data['date'][i])
    date_time = datetime.datetime.strptime(dates, '%Y-%m-%d')
    t = date2num(date_time)
    # 阳线
    if data_processed[i][0] >= 0:
        open = data_processed[i][2] * low + low
        close = data_processed[i][0] * low + open
        high = data_processed[i][1] * low + close
        datas = (t, open, high, low, close)
        data_list_center.append(datas)
    # 阴线
    else:
        close = data_processed[i][2] * low + low
        open = close - data_processed[i][0] * low
        high = data_processed[i][1] * low + open
        datas = (t, open, high, low, close)
        data_list_center.append(datas)



# # plot center_data
# # 创建一个子图
# fig, ax = plt.subplots(facecolor=(0.5, 0.5, 0.5))
# fig.subplots_adjust(bottom=0.2)
# # 设置X轴刻度为日期时间
# ax.xaxis_date()
# # X轴刻度文字倾斜45度
# plt.xticks(rotation=45)
# plt.title("股票代码：000001（平安银行）")
# plt.xlabel("时间")
# plt.ylabel("股价（元）")
# mpf.candlestick_ohlc(ax, data_list, width=2, colorup='r', colordown='g')
# plt.grid(True)
# plt.show()







# plot raw_data
# 设置历史数据区间
date1 = (2014, 9, 24)  # 起始日期，格式：(年，月，日)元组
date2 = (2017, 5, 12)  # 结束日期，格式：(年，月，日)元组
# 对TuShare获取到的数据转换成candlestick_ohlc()方法可读取的格式
data_list_raw = []
for dates, row in stock_data.iterrows():
    # 将时间转换为数字
    dates = str(row[0])
    date_time = datetime.datetime.strptime(dates, '%Y-%m-%d')
    t = date2num(date_time)
    open, close, high, low = row[1:5]
    datas = (t, open, high, low, close)
    data_list_raw.append(datas)
# 创建一个子图
fig, ax = plt.subplots(facecolor=(0.5, 0.5, 0.5))
fig.subplots_adjust(bottom=0.2)
# 设置X轴刻度为日期时间
ax.xaxis_date()
# X轴刻度文字倾斜45度
plt.xticks(rotation=45)
plt.title("股票代码：000001（平安银行）")
plt.xlabel("时间")
plt.ylabel("股价（元）")
mpf.candlestick_ohlc(ax, data_list_raw, width=2, colorup='r', colordown='g')
# mpf.candlestick_ohlc(ax, data_list_center, width=2, colorup='black', colordown='blue')
plt.grid(True)
plt.show()
