import matplotlib.pyplot as plt



input_values = [1,2,3,4,5]
squares = [1,2,3,4,5]       # 绘制折线图形，输出的值
fig,ax= plt.subplots()      #这里subplots(),返回的应该有两个返回值，需要有两个变量
plt.plot(input_values,squares,linewidth = 5) #linewidth 设置的是线的宽度
# 设置图标标题，并给坐标轴加上标签
plt.title("Square Numbers",fontsize = 12)
plt.xlabel("value",fontsize = 12)
plt.ylabel("Square of Value",fontsize = 12)

# 设置刻度标记的大小
plt.tick_params(axis='both',labelsize = 14)

fig.savefig("testOne.png")
plt.show()
