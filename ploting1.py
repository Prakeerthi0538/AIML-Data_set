import matplotlib.pyplot as plt
x=[5,8,9,6]
s=['java','cpp','c','python']
c=['pink','blue','red','green']
plt.pie(x,labels=s,startangle=90,explode=(0.2,0,0,0),autopct='%1.2f',colors=c)
plt.legend()
plt.savefig(r'C:\Users\prake\Desktop\AIML\bar1.jpg')
plt.show()
