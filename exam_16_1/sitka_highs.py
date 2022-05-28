import csv
from turtle import hideturtle

import matplotlib.pyplot as plt
# filename = 'exam\data\sitka_weather_07-2018_simple.csv'
filename = 'exam_16_1\data\sitka_weather_2018_simple.csv'

#查看第一行
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # print(header_row)


#获取每个值得索引及其值
for index,column_header in enumerate(header_row):
    print(index,column_header)

# with open(filename) as f:
#     reader = csv.reader(f)
#     header_row = next(reader)

#     #从文件中获得最高温度
#     highs = []
#     for row in reader:
#         high = int(row[5])
#         highs.append(high)
# print(highs)

# #根据最高温度绘制图形
# plt.style.use('seaborn')
# fig, ax = plt.subplots()
# ax.plot(highs,c='red')#将最高温度传给plot（），绘制为红色

from datetime import datetime
# first_date = datetime.strptime('2018-01-01','%Y-%m-%d')
# print(first_date)

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    #从文件中获得日期和最高温度
    dates, highs = [], []

    for row in reader:
        current_date = datetime.strptime(row[2],'%Y-%m-%d') #将第二行转化为datetime对象
        high = int(row[5])
        dates.append(current_date)
        highs.append(high)
       
       
#根据最高温度绘制图形
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates,highs,c='red')#将日期，最高温度传给plot（）


#设置图形格式
plt.rcParams['font.sans-serif'] = ['SimHei']
# ax.set_title("2018年7月每日最高温度",fontsize=24)
ax.set_title("2018年每日最高温度",fontsize=24)
ax.set_xlabel('',fontsize=16)
fig.autofmt_xdate()     #绘制倾斜日期标签
ax.set_ylabel("温度(F)",fontsize=16)
ax.tick_params(axis='both',which='major',labelsize=16)

plt.show()