import matplotlib.pyplot as plt


x_values = list(range(1,101))
y_values = [x ** 2 for x in x_values]

fig,ax =  plt.subplots()
plt.scatter(x_values,y_values,c=x_values,cmap=plt.cm.Greens,edgecolors='none',s = 40)    #绘制散点图,edgecolors 绘制边缘颜色，none为取消边框颜色
plt.axis([0,110,0,11000])       # 使用函数 axis() 指定每个坐标的取值范围，x轴为0 ~ 110，y轴为 0 ~ 11000


plt.title('this is a title',fontsize = 12)
plt.xlabel('this is x ',fontsize = 12)
plt.ylabel('this is y',fontsize = 12)

plt.tick_params(axis='both',which = 'major',labelsize = 10)

fig.savefig("testFour.png",bbox_inches = 'tight')
plt.show()