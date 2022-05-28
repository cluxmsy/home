from die_visual import Die
from plotly.graph_objs import Bar, Layout
from plotly import offline

#创建两个D6
die1 = Die()
die2 = Die()

#掷几次色子并将结果存储到一个列表中
results = []
for roll_num in range(1000):
    result = die1.roll() + die2.roll()
    results.append(result)

#分析结果
frequencies = []
max_result = die1.num_sides + die2.num_sides
for value in range(2,max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

#对数据进行可视化
x_values = list(range(2,max_result+1))
data = [Bar(x=x_values,y=frequencies)]

x_axis_config = {'title':'结果','dtick':1}
y_axis_config = {'title':'结果的频率'}
my_layout = Layout(title='掷两个D6 1000次的结果',xaxis=x_axis_config,yaxis=y_axis_config)
offline.plot({'data':data,'layout':my_layout},filename='d6_d6.html')




#创建一个D6和一个D10
die1 = Die()
die2 = Die(10)

#掷几次色子并将结果存储到一个列表中
results = []
for roll_num in range(50_000):
    result = die1.roll() + die2.roll()
    results.append(result)

#分析结果
frequencies = []
max_result = die1.num_sides + die2.num_sides
for value in range(2,max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)



#对数据进行可视化
x_values = list(range(2,max_result+1))
data = [Bar(x=x_values,y=frequencies)]

x_axis_config = {'title':'结果','dtick':1}
y_axis_config = {'title':'结果的频率'}
my_layout = Layout(title='掷一个D6和一个D10 50000次的结果',xaxis=x_axis_config,yaxis=y_axis_config)
offline.plot({'data':data,'layout':my_layout},filename='d6_d10.html')