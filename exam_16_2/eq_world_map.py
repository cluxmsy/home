#绘制震级散点图
import json
import plotly.express as px
import pandas as pd

# 探索数据结构
# filename = 'exam_16_2\data\eq_data_1_day_m1.json'
filename = 'exam_16_2\data\eq_data_30_day_m1.json'
with open(filename) as f:
    all_eq_data1 = json.load(f) #转换为python能处理的格式

all_eq_dicts = all_eq_data1['features']
print(len(all_eq_dicts))

#创建一个文件，将数据一易读的形式存入
readable_file = "exam_16_2/data/readable_eq_data.json"
with open(readable_file, 'w') as f:
    json.dump(all_eq_data1, f, indent=4)    #indent代表缩进

# #创建一个数组存储地震等级
# mags = []
# for eq_dict in all_eq_dicts:
#     mag = eq_dict['properties']['mag']
#     mags.append(mag)

mags, titles, lons, lats =[], [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    #title以及经纬度
    title = eq_dict['properties']['title']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    titles.append(title)
    lons.append(lon)
    lats.append(lat)


#将所有信息以键值对的形式存储在一个字典中
data = pd.DataFrame(
    data=zip(lons,lats,titles,mags),columns=['经度','纬度','位置','震级']
)
data.head()

fig = px.scatter(
    # x=lons,
    # y=lats,
    # labels={'x':'经度','y':'纬度'},
    data,
    x='经度',
    y='纬度',
    range_x=[-200,200], #轴范围
    range_y=[-90,90],   #y轴范围
    width=800,
    height=800,
    title='全球震级散点图',
    size='震级',    #标记的尺寸
    size_max=10,    #最大显示尺寸放大到10
    color='震级',
    hover_name='位置'
)
fig.write_html('global_earthquakes.html')
fig.show()

