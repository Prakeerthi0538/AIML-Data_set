a=open(r'C:\Users\prake\Desktop\AIML\diabetes_data_upload.csv','r')
b=a.readlines()
a.close()
c=[]
for i in b:
    c.append(i.split(','))
d={}
for i in c:
    if i[1] not in d.keys():
        d[i[1]]=1
    else:
        d[i[1]]+=1
print(d)

##output:
##{'Gender': 1, 'Male': 328, 'Female': 192}
