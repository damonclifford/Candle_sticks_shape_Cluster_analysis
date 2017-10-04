from sklearn.externals import joblib
import pickle
import matplotlib.pyplot as plt
import matplotlib.finance as mpf
from matplotlib.pylab import date2num
import datetime

labels_path = r'C:\Users\lyzdsb\PycharmProjects\finalProject\data\labels.pkl'
mode_path = r'C:\Users\lyzdsb\PycharmProjects\finalProject\data\para3_data'
rawData_path = r'C:\Users\lyzdsb\PycharmProjects\finalProject\data\raw_data'

# read document to get label_list
labels_pkl = open(labels_path, 'rb')
labels_list = pickle.load(labels_pkl)
labels = labels_list[0]

# read the best model and get the data of center points
clf = joblib.load(mode_path + r'\mode_i_30.pkl')
centers = clf.cluster_centers_

# read 000001.pkl
stock_pkl = open(rawData_path + r'\000001.pkl', 'rb')
stock_data = pickle.load(stock_pkl)
# print(stock_data)

# convert raw_data into center_data
data_processed = []
for label in labels:
    data_processed.append(centers[label])

data_list_center = []

for i in range(len(stock_data)):
    low = stock_data['low'][i]
    #     # transform date format to numeric
    dates = str(stock_data['date'][i])
    date_time = datetime.datetime.strptime(dates, '%Y-%m-%d')
    t = date2num(date_time)
    # ups stick
    if data_processed[i][0] >= 0:
        open = data_processed[i][2] * low + low
        close = data_processed[i][0] * low + open
        high = data_processed[i][1] * low + close
        datas = (t, open, high, low, close)
        data_list_center.append(datas)
    # downs stick
    else:
        close = data_processed[i][2] * low + low
        open = close - data_processed[i][0] * low
        high = data_processed[i][1] * low + open
        datas = (t, open, high, low, close)
        data_list_center.append(datas)
        
# plot raw_data
# set the start date and end date
# format : (yyy,mmm,ddd)
date1 = (2014, 9, 24)  
date2 = (2017, 5, 12)  
# transform the data from TuShare to a available format of candlestick_ohlc()
data_list_raw = []
for dates, row in stock_data.iterrows():
    # transform datetime into string
    dates = str(row[0])
    date_time = datetime.datetime.strptime(dates, '%Y-%m-%d')
    t = date2num(date_time)
    open, close, high, low = row[1:5]
    datas = (t, open, high, low, close)
    data_list_raw.append(datas)
# create a subplot
fig, ax = plt.subplots(facecolor=(0.5, 0.5, 0.5))
fig.subplots_adjust(bottom=0.2)

ax.xaxis_date()
plt.xticks(rotation=45)
plt.title("Stock code：000001")
plt.xlabel("date")
plt.ylabel("price(yuan)")
mpf.candlestick_ohlc(ax, data_list_raw, width=2, colorup='r', colordown='g')
# mpf.candlestick_ohlc(ax, data_list_center, width=2, colorup='black', colordown='blue')
plt.grid(True)
plt.show()
