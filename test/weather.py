
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('weather.csv')

# 提取Beijing的温度数据
beijing = data[data['City'] == 'Beijing']['Temperature']

# 绘制折线图
plt.plot(beijing)
plt.xlabel('Date')
plt.ylabel('Temperature')
plt.title('Beijing Temperature Change')
plt.show()
