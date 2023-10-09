a=open(r'C:\Users\prake\Desktop\AIML\diabetes_data_upload.csv','r')
b=a.readlines()
a.close()
c=[]
for i in b:
    c.append(i.split(','))
d={}
for i in c:
    if i[-1] not in d.keys():
        d[i[-1][:-1]]=1
    else:
        d[i[-1][:-1]]+=1
print(d)
## output:
##{'class\n': 1, 'Positive\n': 320, 'Negative\n': 200}
##{'class': 1, 'Positive': 1, 'Negative': 1}  to remove \n keep [:-1]

##a=open(r'C:\Users\prake\Desktop\AIML\diabetes_data_upload.csv','r')
##b=a.readlines()
##c=[]
##for i in b:
##    c.append(i)
##a.close()
##pev=0
##nev=0
##for i in c:
##    if 'Positive' in i:
##        pev+=1
##    else:
##        nev+=1
##print(pev)
##print(nev)
