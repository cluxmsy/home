from random import randint

from numpy import result_type

class Die:
    """表示一个骰子的类"""

    def __init__(self,num_sides=6) :
        """骰子默认为6面"""
        self.num_sides = num_sides

    def roll(self):
        """返回一个位于1到6之间的随机数值"""
        return randint(1,self.num_sides)

#创建一个D6
die = Die()

#掷几次色子并将结果存储到一个列表中
results = []
for roll_num in range(100):
    result = die.roll()
    results.append(result)
print(results)

results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

#分析结果
frequencies = []
for value in range(1,die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)
print(frequencies)

from plotly.graph_objs import Bar, Layout
from plotly import offline

#对数据进行可视化
x_values = list(range(1,die.num_sides+1))
data = [Bar(x=x_values,y=frequencies)]

x_axis_config = {'title':'结果'}
y_axis_config = {'title':'结果的频率'}
my_layout = Layout(title='掷一个D6 1000次的结果',xaxis=x_axis_config,yaxis=y_axis_config)
offline.plot({'data':data,'layout':my_layout},filename='D6.html')

