import csv
from datetime import datetime

from matplotlib import pyplot as plt

filename = 'exam_16_1\data\death_valley_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

     #从文件中获得日期和最高温度和最低温度
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:        #valueError异常
            high = int(row[4])
            low = int(row[5])
        except ValueError:
            print(f"Missing data for {current_date}")#打印缺少的日期
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

#根据最高温度和最低温度绘制图形
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)#将日期，最高温度传给plot（）绘制成红色
ax.plot(dates, lows, c='blue', alpha=0.5)#将最低温度绘制成蓝色，alpha为透明度
ax.fill_between(dates, highs, lows, facecolor='blue',alpha=0.1)#在最高和最低之间填充颜色

#设置图形格式
plt.rcParams['font.sans-serif'] = ['SimHei']
ax.set_title("2018年每日最高温度和最低温度\n 美国加利福尼亚州死亡谷",fontsize=24)
ax.set_xlabel('',fontsize=16)
fig.autofmt_xdate()     #绘制倾斜日期标签
ax.set_ylabel("温度(F)",fontsize=16)
ax.tick_params(axis='both',which='major',labelsize=16)

plt.show()