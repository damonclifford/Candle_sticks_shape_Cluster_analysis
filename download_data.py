import tushare as ts
import pickle

# download and save the zz500
# code_zz500s = []
# code_zz500s = list(ts.get_zz500s()['code'])
# for code in code_zz500s:
#     file_path = r'C:\Users\lyzdsb\PycharmProjects\untitled3\data\raw_data\\'+code+".pkl"
#     df = ts.get_k_data(code)
#     df.to_pickle(file_path)



# download and save the hs300
code_hs300s = list(ts.get_hs300s()['code'])
for code in code_hs300s:
    file_path = r'C:\Users\lyzdsb\PycharmProjects\untitled3\data\raw_data\\'+code+".pkl"
    df = ts.get_k_data(code);
    df.to_pickle(file_path);


