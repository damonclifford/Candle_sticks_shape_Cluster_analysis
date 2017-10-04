import os
import pickle


class SingleWick():
    def __init__(self, data):
        # all stock data 
        self.data = data
        # open
        self.open = data['open']
        # close
        self.close = data['close']
        # high
        self.high = data['high']
        # low
        self.low = data['low']
        # data file path
        # self.dirpath = dirpath

    # middle stick
    def get_middlewick_rate(self):

        middlewick = []

        for i in range(len(self.open) ):
            para1 = (self.close[i] - self.open[i]) / self.low[i]
            middlewick.append(para1)
        return middlewick

    # upper stick
    def get_upperwick_rate(self):
        upperwick = []
        for i in range(len(self.open) ):
            # ups
            if self.close[i] > self.open[i]:
                para2 = (self.high[i] - self.close[i]) / self.low[i]
                upperwick.append(para2)
            # downs
            else:
                para2 = (self.high[i] - self.open[i]) / self.low[i]
            upperwick.append(para2)
        return upperwick

    # down stick
    def get_lowerwick_rate(self):
        lowerwick = []
        for i in range(len(self.open)):
            # ups
            if self.close[i] > self.open[i]:
                para3 = (self.open[i] - self.low[i]) / self.low[i]
                lowerwick.append(para3)
            # downs
            else:
                para3 = (self.close[i] - self.low[i]) / self.low[i]
            lowerwick.append(para3)
        return lowerwick

    # the positive value of close_dif means ups tread while the negative value means downs trend
    # def get_close_dif_rate(self):
    #     close_dif = []
    #     for i in range(len(self.open) - 1):
    #         para4 = (self.close[i + 1] - self.close[i]) / self.close[i]
    #         close_dif.append(para4)
    #     return close_dif

    def get_singlewick(self):

        middlewick = self.get_middlewick_rate()
        upperwick = self.get_upperwick_rate()
        lowerwick = self.get_lowerwick_rate()
        # close_dif = self.get_close_dif_rate()
        singlewick = list(zip(middlewick, upperwick, lowerwick))
        # for i in singlewick:
        #     if i[3] >= 0.11 or i[3] <= -0.11:
        #         singlewick.remove(i)
        return singlewick


if __name__ == '__main__':
    global X
    X = []
    dirpath = r'C:\Users\lyzdsb\PycharmProjects\untitled3\data'
    code_list = os.listdir(dirpath + r'\raw_data')
    for code in code_list:
        file_path = dirpath + r'\raw_data' + '\\' + code
        pkl_file = open(file_path, 'rb')
        data = pickle.load(pkl_file)
        pkl_file.close()
        a = SingleWick(data)
        temp = a.get_singlewick()
        X = X + temp
    output = open(dirpath + r'\raw_data_integrate\raw_data_para3.pkl', 'wb')
    pickle.dump(X, output, -1)
    output.close()
