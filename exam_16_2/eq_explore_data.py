from fileinput import filename
import json

# 探索数据结构
filename = 'exam_16_2\data\eq_data_1_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)  #转换为python能处理的格式

all_eq_dicts = all_eq_data['features']
print(len(all_eq_dicts))

#创建一个文件，将数据一易读的形式存入
readable_file = "exam_16_2/data/readable_eq_data.json"
with open(readable_file, 'w') as f:
    json.dump(all_eq_data, f, indent=4)  # indent代表缩进

#创建一个数组存储地震等级
mags = []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    mags.append(mag)


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

