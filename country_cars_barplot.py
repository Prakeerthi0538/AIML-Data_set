import matplotlib.pyplot as plt
a=open(r"C:\Users\prake\Desktop\AIML\cars_country.csv",'r')
s=a.readlines()
a.close()
c=[]
for i in s:
    c.append(i.split(','))
d={}
for i in c[1:]:
    if i[-1] not in d.keys():
             d[i[-1]]=1
    else:
             d[i[-1]]+=1
##print(d)
##v=['US','Europe']
x=[]
y=[]
for i in d:
    x.append(i[:-1])
for i in d:
    y.append(d[i])

plt.bar(x,y,color='purple')
plt.savefig(r'C:\Users\prake\Desktop\AIML\figures\cars_country.jpg')
plt.show()
