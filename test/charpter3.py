
# 导入模块
import json
import folium

# 加载和处理数据
filename = "eq_data_1_day_m1.json" # 地震数据文件名
with open(filename) as f:
    all_eq_data = json.load(f) # 加载数据为一个字典
    all_eq_dicts = all_eq_data["features"] # 获取地震列表

mags = [] # 震级列表
lons = [] # 经度列表
lats = [] # 纬度列表

for eq_dict in all_eq_dicts:
    mag = eq_dict["properties"]["mag"] # 获取震级
    lon = eq_dict["geometry"]["coordinates"][0] # 获取经度
    lat = eq_dict["geometry"]["coordinates"][1] # 获取纬度
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)

# 创建地图对象
map = folium.Map(location=[0, 0], zoom_start=2) # 以全球为中心，缩放比例为2

# 添加散点图层
map.add_child(folium.features.CircleMarker( # 使用圆形标记
    location=[lat, lon], # 位置参数为纬度和经度
    radius=5*mag, # 半径参数为震级的5倍
    popup=f"Magnitude: {mag}", # 弹出框显示震级信息
    fill_color="red", # 填充颜色为红色
    color="None", # 边框颜色为无色
    fill_opacity=0.7 # 填充透明度为0.7
) for lat, lon, mag in zip(lats, lons, mags)) # 使用zip函数将三个列表打包

# 保存和显示地图
map.save("global_earthquakes.html") # 保存为html文件
map # 显示地图
